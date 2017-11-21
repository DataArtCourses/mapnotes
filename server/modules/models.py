import asyncio
import aiomysql
import logging

from abc import ABC, abstractmethod

from . import utils

from .config import Config
from .exceptions import *

__all__ = ('UserBase', 'PinBase', 'ChatBase', 'ChatMessageBase', 'PinMessageBase')

log = logging.getLogger('application')


class Base(ABC):

    pool = None

    @staticmethod
    async def connect():
        log.info('Connecting to Database')
        try:
            Base.pool = await aiomysql.create_pool(
                user=Config.get('mysql', 'user'),
                db=Config.get('mysql', 'db'),
                host=Config.get('mysql', 'host'),
                password=Config.get('mysql', 'password'),
                loop=asyncio.get_event_loop()
            )
        except Exception as e:
            log.error("Error connecting to DB: %s", e)
        else:
            log.info('Connected to Database')

    @classmethod
    async def make_query(cls, query, fetchone=False, args=None, insert_fetch=False):
        async with cls.pool.get() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                try:
                    await cur.execute(query, args)
                except Exception as e:
                    log.error("SQL Error %s", e)
                    await conn.commit()
                    return e
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

    @classmethod
    @abstractmethod
    async def create_table(cls):
        pass

    @classmethod
    async def drop_table(cls):
        logging.info('Deleting %s table', cls.table_name)
        query = f"DROP TABLE IF EXISTS {cls.table_name};"
        await cls.make_query(query)
        logging.info('Done deleting %s table', cls.table_name)


class Users(Base):

    table_name = 'users'
    pk = 'user_id'
    fields = {'first_name', 'last_name', 'phone', 'bio', 'avatar_url'}

    @classmethod
    async def create_table(cls):
        query = (f"CREATE TABLE IF NOT EXISTS `{cls.table_name}`("
                 "`user_id` INT NOT NULL AUTO_INCREMENT,"
                 "`email` VARCHAR(255) NOT NULL UNIQUE,"
                 "`password` CHAR(32) NOT NULL,"  # hashed with MD5
                 "`first_name` VARCHAR(255) NOT NULL DEFAULT '',"
                 "`last_name` VARCHAR(255) NOT NULL DEFAULT '',"
                 "`bio` TEXT,"
                 "`registered` INT(1) DEFAULT 0,"
                 "`phone` VARCHAR(20) NOT NULL DEFAULT '',"
                 "`avatar_url` VARCHAR(255) NOT NULL DEFAULT "
                 "'http://dsi-vd.github.io/patternlab-vd/images/fpo_avatar.png',"
                 f"PRIMARY KEY({cls.pk}))"
                 )
        log.info('Creating table %s', cls.table_name)
        try:
            await cls.make_query(query=query, fetchone=True)
        except Exception as e:
            log.error('Error creating table %s with %s', cls.table_name, e)
        else:
            log.info('Successfuly created table %s', cls.table_name)

    @classmethod
    async def update_profile(cls, user_id, first_name, last_name, bio, phone, avatar_url):
        query = (f"UPDATE `{cls.table_name}`"
                 "SET `first_name` = %s, `last_name` = %s, `bio` = %s, `phone` = %s, `avatar_url` = %s "
                 "WHERE `user_id` = %s"
                 )
        await cls.make_query(query=query, args=[first_name, last_name, bio, phone, avatar_url, user_id])

    @classmethod
    async def get_profile(cls, user_id):
        query = (f"SELECT `first_name`, `last_name`, `bio`, `phone`, `avatar_url`"
                 f"FROM `{cls.table_name}` "
                 "WHERE `registered` = 1 AND `user_id` = %s"
                 )

        profile = await cls.make_query(query=query, args=[user_id], fetchone=True)

        return profile

    @classmethod
    async def create_new_user(cls, email, password):
        query = (f"INSERT INTO `{cls.table_name}` "
                 "(`email`, `password`) VALUES "
                 "(%s, %s)"
                 )

        password = utils.encrypt_password(password, email)
        register_link = utils.create_register_link(password, email, Config.get('application', 'salt'))

        res = await cls.make_query(query=query, insert_fetch=True, args=[email, password])
        if isinstance(res, Exception):
            if res.args[0] == 1062:
                error = "User with this email already exists"
                raise UserAlreadyExist(error)
            else:
                raise res
        else:
            log.info("Created new user with id of %s", res)
            return register_link

    @classmethod
    async def confirm_registration(cls, email):

        query = (f"SELECT `email`, `user_id` FROM `{cls.table_name}` "
                 "WHERE `registered` = 0 AND `email` = %s"
                 )

        user = await cls.make_query(query=query, args=[email], fetchone=True)

        if isinstance(user, Exception) or not user:
            error = "Registration link for this user has been already activated or user does not exist"
            raise UserAlreadyExist(error)
        else:
            query = (f"UPDATE `{cls.table_name}` "
                     f"SET `registered` = 1 "
                     f"WHERE `user_id` = %s"
                     )
            await cls.make_query(query=query, args=[user['user_id']])
            log.info("User %s successfuly confirmed registration", user['email'])
            return None

    @classmethod
    async def get_user(cls, _id):

        query = f"SELECT `user_id` FROM {cls.table_name} WHERE `user_id` = %s AND `registered` = 1"
        user = await cls.make_query(query=query, args=[_id], fetchone=True)

        if user:
            return user['user_id']
        else:
            return None

    @classmethod
    async def authorize(cls, email, password):

        query = f"SELECT `email`, `user_id`, `password` FROM {cls.table_name} WHERE `email` = %s AND `registered` = 1"
        user = await cls.make_query(query=query, args=[email], fetchone=True)

        if not user:
            raise UserDoesNotExist
        else:
            password = utils.encrypt_password(password, email)

            if password != user['password']:
                raise PasswordDoesNotMatch
            else:
                del user['password']
                return user


class Pins(Base):

    table_name = 'map_pins'
    pk = 'pin_id'
    fields = {'user_id', 'lat', 'lng'}

    @classmethod
    async def create_table(cls):
        query = (f"CREATE TABLE IF NOT EXISTS `{cls.table_name}`("
                 "`pin_id` INT NOT NULL AUTO_INCREMENT,"
                 "`user_id` INT REFERENCES `users`(`user_id`),"
                 "`lat` DECIMAL(10, 8) NOT NULL,"
                 "`lng` DECIMAL(11, 8) NOT NULL,"
                 f"PRIMARY KEY({cls.pk}))"
                 )
        log.info('Creating table %s', cls.table_name)
        try:
            await cls.make_query(query=query, fetchone=True)
        except Exception as e:
            log.error('Error creating table %s with %s', cls.table_name, e)
        else:
            log.info('Successfuly created table %s', cls.table_name)

    @classmethod
    async def create_pin(cls, user_id, lat, lng):
        query_insert = (f"INSERT INTO `{cls.table_name}`"
                 "(user_id, lat, lng) VALUES"
                 "(%s, %s, %s)"
                 )
        await cls.make_query(query=query_insert, args=[user_id, lat, lng])
        log.info("User %s successfuly add pin", user_id)
        query_recive = (f"SELECT LAST_INSERT_ID() as pin_id")
        res = await cls.make_query(query=query_recive, fetchone=True)
        return res

    @classmethod
    async def get_pins(cls, user_id):
        query = (
                f"SELECT pin_id, lat, lng FROM `{cls.table_name}` "
                 )
        pins = await cls.make_query(query=query)
        log.info("User %s successfuly get pins", user_id)
        return pins


class PinComments(Base):

    table_name = 'pin_comments'

    @classmethod
    async def create_table(cls):
        query = (f"CREATE TABLE IF NOT EXISTS `{cls.table_name}`("
                 "`comment_id` INT NOT NULL AUTO_INCREMENT,"
                 "`pin_id` INT NOT NULL REFERENCES `map_pins`(`pin_id`),"
                 "`photo_id` INT REFERENCES `pin_photos`(`photo_id`),"
                 "`sender` INT NOT NULL REFERENCES `users`(`user_id`),"
                 "`status` INT(1) DEFAULT 0,"
                 "`comment_body` VARCHAR(400) NOT NULL,"
                 "`date` DATETIME DEFAULT NOW(),"
                 "PRIMARY KEY(`comment_id`))"
                 )
        log.info('Creating table %s', cls.table_name)
        try:
            await cls.make_query(query=query, fetchone=True)
        except Exception as e:
            log.error('Error creating table %s with %s', cls.table_name, e)
        else:
            log.info('Successfuly created table %s', cls.table_name)

        @classmethod
        async def create_comment(cls, user_id, pin_id, comment_body, status, photo_id=None):
            query = (f"INSERT INTO `{cls.table_name}`"
                     "(user_id, pin_id, comment_body, status, photo_id) VALUES"
                     "(%s, %s, %s, %s, %s, %s)"
                     )
            await cls.make_query(query=query, args=[user_id, pin_id, comment_body, status, photo_id])
            log.info("User %s successfuly add comment", user_id)
            return None

class PinPhotos(Base):

    table_name = 'pin_photos'

    @classmethod
    async def create_table(cls):
        query = (f"CREATE TABLE IF NOT EXISTS `{cls.table_name}`("
                 "`photo_id` INT NOT NULL AUTO_INCREMENT,"
                 "`pin_id` INT NOT NULL REFERENCES `map_pins`(`pin_id`),"
                 "`sender` INT NOT NULL REFERENCES `users`(`user_id`),"
                 "`status` INT NOT NULL DEFAULT 0,"
                 "`photo_url` VARCHAR(400) NOT NULL,"
                 "`date` DATETIME DEFAULT NOW(),"
                 "PRIMARY KEY(`photo_id`))"
                 )
        log.info('Creating table %s', cls.table_name)
        try:
            await cls.make_query(query=query, fetchone=True)
        except Exception as e:
            log.error('Error creating table %s with %s', cls.table_name, e)
        else:
            log.info('Successfuly created table %s', cls.table_name)


class Chats(Base):

    table_name = 'chat'

    @classmethod
    async def create_table(cls):
        query = (f"CREATE TABLE IF NOT EXISTS `{cls.table_name}`("
                 "`chat_id` INT NOT NULL AUTO_INCREMENT,"
                 "`user_1` INT REFERENCES `users`(`user_id`),"
                 "`user_2` INT REFERENCES `users`(`user_id`),"
                 "PRIMARY KEY(`chat_id`),"
                 "KEY(`user_1`, `user_2`))"
                 )
        log.info('Creating table %s', cls.table_name)
        try:
            await cls.make_query(query=query, fetchone=True)
        except Exception as e:
            log.error('Error creating table %s with %s', cls.table_name, e)
        else:
            log.info('Successfuly created table %s', cls.table_name)



class ChatMessages(Base):

    table_name = 'chat_message'

    @classmethod
    async def create_table(cls):
        query = (f"CREATE TABLE IF NOT EXISTS `{cls.table_name}`("
                 "`id` INT NOT NULL AUTO_INCREMENT,"
                 "`chat_id` INT NOT NULL REFERENCES `chat`(`id`),"
                 "`sender` INT REFERENCES `users`(`id`),"
                 "`message` TEXT,"
                 "`date` DATETIME DEFAULT NOW(),"
                 "PRIMARY KEY(`id`))"
                 )
        log.info('Creating table %s', cls.table_name)
        try:
            await cls.make_query(query=query, fetchone=True)
        except Exception as e:
            log.error('Error creating table %s with %s', cls.table_name, e)
        else:
            log.info('Successfuly created table %s', cls.table_name)
