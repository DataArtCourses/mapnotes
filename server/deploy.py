import asyncio
import logging
import argparse

from modules.models import (
    Base, Users, Pins, PinComments, PinPhotos, Chats, ChatMessages
)

log = logging.getLogger('application')
log.setLevel(0)
logging.root.setLevel(0)
log.addHandler(logging.StreamHandler())


async def db_import():
    await Base.connect()
    logging.debug('Creating database')
    await Users.create_table()
    await Pins.create_table()
    await Chats.create_table()
    await ChatMessages.create_table()
    await PinComments.create_table()
    await PinPhotos.create_table()
    log.info('Done creating database')


async def drop_tables():
    await Base.connect()
    logging.debug('Deleting all tables...')
    await asyncio.gather(
        Users.drop_table(),
        Pins.drop_table(),
        ChatMessages.drop_table(),
        Chats.drop_table(),
        PinComments.drop_table(),
        PinPhotos.drop_table()
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
