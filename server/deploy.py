import asyncio
import logging
import argparse

from modules.dao import (
    UserDao, PinDao, ChatDao, ChatMessageDao, PinMessageDao
)

log = logging.getLogger('application')
log.setLevel(0)
logging.root.setLevel(0)
log.addHandler(logging.StreamHandler())


user_dao = UserDao()
pin_dao = PinDao()
chat_dao = ChatDao()
chat_message_dao = ChatMessageDao()
pin_message_dao = PinMessageDao()


async def db_import():
    logging.debug('Creating database')
    await user_dao.create_table()
    await pin_dao.create_table()
    await chat_dao.create_table()
    await chat_message_dao.create_table()
    await pin_message_dao.create_table()
    log.info('Done creating database')


async def drop_tables():
    logging.debug('Deleting all tables...')
    await asyncio.gather(
        user_dao.drop_table(),
        pin_dao.drop_table(),
        chat_message_dao.drop_table(),
        chat_dao.drop_table(),
        pin_message_dao.drop_table()
    )
    logging.debug('Done deleting tables')

# Args parse
parser = argparse.ArgumentParser()
parser.add_argument("--action",
                    help="action to perform with DB",
                    default='db_import')
args = parser.parse_args()

namespace = {
    'db_import': db_import,
    'drop_tables': drop_tables
}

loop = asyncio.get_event_loop()
loop.run_until_complete(namespace.get(args.action, 'db_import')())
