import asyncio
import aiomysql
import logging

from abc import ABC, abstractmethod

from .config import Config


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

    async def make_query(self, query, fetchone=False, args=None, no_fetch=False):
        async with self.pool.get() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(query, args)
                if fetchone:
                    res = await cur.fetchone()
                elif no_fetch:
                    res = True
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
        query = f"DROP TABLE IF EXISTS {self.table_name};"
        await self.make_query(query)
        # query = "DROP TABLE IF EXISTS %s;" todo why does escape don't work with DROP statement?
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
                 "(`email`, `password`) VALUES "
                 "(%s, %s)"
                 )
        user_id = await self.make_query(query=query, no_fetch=True, args=[email, password])
        return user_id
        # try:
        #     user_id = await self.make_query(query=query, no_fetch=True, args=[email, password])
        # except Exception as e:
        #     log.info("Error creating user %s, error %s", email, e)
        # else:
        #     log.info("Created user %s with id %s", email, user_id)

    async def get_all(self):
        query = f'SELECT * FROM {self.table_name}'
        res = await self.make_query(query)
        return res


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
