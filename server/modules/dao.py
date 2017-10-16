import asyncio
import aiomysql
import logging
import hashlib
import time

from abc import ABC, abstractmethod

from .config import Config
from .exceptions import *

__all__ = ('UserDao', 'PinDao', 'ChatDao', 'ChatMessageDao', 'PinMessageDao')

log = logging.getLogger('application')


class Dao(ABC):

    loop = asyncio.get_event_loop()
    pool = loop.run_until_complete(
        aiomysql.create_pool(
            user=Config.get('mysql', 'user'),
            db=Config.get('mysql', 'db'),
            host=Config.get('mysql', 'host'),
            password=Config.get('mysql', 'password'),
            loop=loop
        )
    )

    async def make_query(self, query, fetchone=False, args=None, insert_fetch=False):
        async with self.pool.get() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                try:
                    await cur.execute(query, args)
                except Exception as e:
                    log.error("SQL Error %s", e)
                    res = e
                else:
                    if fetchone:
                        res = await cur.fetchone()
                    elif insert_fetch:
                        res = cur.lastrowid
                    else:
                        res = await cur.fetchall()
                        res = res or []
            await conn.commit()
        return res

    async def call_proc(self, procname, args):
        async with self.pool.get() as conn:
            async with conn.cursor() as cur:
                await cur.execute(procname, args)
                result = await cur.fetchall()
        return result

    @abstractmethod
    async def create_table(self):
        pass

    async def drop_table(self):
        logging.info('Deleting %s table', self.table_name)
        query = f"DROP TABLE IF EXISTS {self.table_name};"
        await self.make_query(query)
        logging.info('Done deleting %s table', self.table_name)
        # query = "DROP TABLE IF EXISTS %s;"  # todo why does escape don't work with DROP statement?
        # await self.make_query(query, args=[self.table_name])


class UserDao(Dao):

    def __init__(self):
        self.table_name = 'users'
        self.pk = 'user_id'

    async def create_table(self):
        query = (f"CREATE TABLE IF NOT EXISTS `{self.table_name}`("
                 "`user_id` INT NOT NULL AUTO_INCREMENT,"
                 "`email` VARCHAR(255) NOT NULL UNIQUE,"
                 "`password` CHAR(32) NOT NULL,"  # hashed with MD5
                 "`first_name` VARCHAR(255) NOT NULL DEFAULT '',"
                 "`second_name` VARCHAR(255) NOT NULL DEFAULT '',"
                 "`bio` TEXT,"
                 "`registered` INT(1) DEFAULT 0,"
                 "`register_link` VARCHAR(50) DEFAULT '',"
                 "`phone` VARCHAR(20) NOT NULL DEFAULT '',"
                 "`avatar_url` VARCHAR(255) NOT NULL DEFAULT '',"
                 f"PRIMARY KEY({self.pk}))"
                 )
        log.info('Creating table %s', self.table_name)
        try:
            await self.make_query(query=query, fetchone=True)
        except Exception as e:
            log.error('Error creating table %s with %s', self.table_name, e)
        else:
            log.info('Successfuly created table %s', self.table_name)

    async def create_new_user(self, email, password):
        query = (f"INSERT INTO `{self.table_name}` "
                 "(`email`, `password`, `register_link`) VALUES "
                 "(%s, %s, %s)"
                 )
        _hash = hashlib.md5()
        _hash.update(password.encode('utf-8'))
        _hash.update(email.encode('utf-8'))
        password = _hash.hexdigest()

        _hash = hashlib.blake2b()
        _hash.update(email.encode('utf-8'))
        _hash.update(password.encode('utf-8'))
        _hash.update(Config.get('application', 'salt').encode('utf-8'))
        _hash.update(str(time.time()).encode('utf-8'))

        register_link = _hash.hexdigest()[:50]

        res = await self.make_query(query=query, insert_fetch=True, args=[email, password, register_link])
        if isinstance(res, Exception):
            if res.args[0] == 1062:
                error = "User with this email already exists"
                return error, None
        else:
            log.info("Created new user with id of %s", res)
            return None, register_link

    async def confirm_registration(self, confirm_key):

        query = (f"SELECT `email`, `user_id` FROM `{self.table_name}` "
                 f"WHERE `register_link` = %s AND `registered` = 0"
                 )

        user = await self.make_query(query=query, args=[confirm_key], fetchone=True)

        if isinstance(user, Exception) or not user:
            error = "Registration link expired or have already been activated"
            return error
        else:
            query = (f"UPDATE `{self.table_name}` "
                     f"SET `registered` = 1 "
                     f"WHERE `user_id` = %s"
                     )
            await self.make_query(query=query, args=[user['user_id']])
            log.info("User %s successfuly confirmed registration", user['email'])
            return None

    async def get_user(self, _id):

        query = f"SELECT `user_id` FROM {self.table_name} WHERE `user_id` = %s AND `registered` = 1"
        user = await self.make_query(query=query, args=[_id], fetchone=True)

        if user:
            return user['user_id']
        else:
            return None

    async def authorize(self, email, password):

        query = f"SELECT `email`, `user_id`, `password` FROM {self.table_name} WHERE `email` = %s AND `registered` = 1"
        user = await self.make_query(query=query, args=[email], fetchone=True)

        if not user:
            raise UserDoesNotExist
        else:
            _hash = hashlib.md5()
            _hash.update(str(password).encode('utf-8'))
            _hash.update(email.encode('utf-8'))
            password = _hash.hexdigest()

            if password != user['password']:
                raise PasswordDoesNotMatch
            else:
                del user['password']
                return user


class PinDao(Dao):

    def __init__(self):
        self.table_name = 'map_pins'
        self.pk = 'id'

    async def create_table(self):
        query = (f"CREATE TABLE IF NOT EXISTS `{self.table_name}`("
                 "`id` INT NOT NULL AUTO_INCREMENT,"
                 "`user_id` INT REFERENCES `users`(`id`),"
                 "`position` CHAR(32) NOT NULL,"
                 "`private` BOOLEAN NOT NULL,"
                 f"PRIMARY KEY({self.pk}))"
                 )
        log.info('Creating table %s', self.table_name)
        try:
            await self.make_query(query=query, fetchone=True)
        except Exception as e:
            log.error('Error creating table %s with %s', self.table_name, e)
        else:
            log.info('Successfuly created table %s', self.table_name)


class ChatDao(Dao):

    def __init__(self):
        self.table_name = 'chat'

    async def create_table(self):
        query = (f"CREATE TABLE IF NOT EXISTS `{self.table_name}`("
                 "`id` INT NOT NULL AUTO_INCREMENT,"
                 "`user_1` INT REFERENCES `users`(`id`),"
                 "`user_2` INT REFERENCES `users`(`id`),"
                 "PRIMARY KEY(`id`),"
                 "KEY(`user_1`, `user_2`))"
                 )
        log.info('Creating table %s', self.table_name)
        try:
            await self.make_query(query=query, fetchone=True)
        except Exception as e:
            log.error('Error creating table %s with %s', self.table_name, e)
        else:
            log.info('Successfuly created table %s', self.table_name)


class ChatMessageDao(Dao):

    def __init__(self):
        self.table_name = 'chat_message'

    async def create_table(self):
        query = (f"CREATE TABLE IF NOT EXISTS `{self.table_name}`("
                 "`id` INT NOT NULL AUTO_INCREMENT,"
                 "`chat_id` INT NOT NULL REFERENCES `chat`(`id`),"
                 "`sender` INT REFERENCES `users`(`id`),"
                 "`message` TEXT,"
                 "`date` DATETIME DEFAULT NOW(),"
                 "PRIMARY KEY(`id`))"
                 )
        log.info('Creating table %s', self.table_name)
        try:
            await self.make_query(query=query, fetchone=True)
        except Exception as e:
            log.error('Error creating table %s with %s', self.table_name, e)
        else:
            log.info('Successfuly created table %s', self.table_name)


class PinMessageDao(Dao):

    def __init__(self):
        self.table_name = 'pin_message'

    async def create_table(self):
        query = (f"CREATE TABLE IF NOT EXISTS `{self.table_name}`("
                 "`id` INT NOT NULL AUTO_INCREMENT,"
                 "`chat_id` INT NOT NULL REFERENCES `chat`(`id`),"
                 "`sender` INT REFERENCES `users`(`id`),"
                 "`message` TEXT,"
                 "`date` DATETIME DEFAULT NOW(),"
                 "PRIMARY KEY(`id`))"
                 )
        log.info('Creating table %s', self.table_name)
        try:
            await self.make_query(query=query, fetchone=True)
        except Exception as e:
            log.error('Error creating table %s with %s', self.table_name, e)
        else:
            log.info('Successfuly created table %s', self.table_name)
