import os
import sys
import logging
import argparse

from aiohttp import web

from modules.config import Config
from modules.app import application

LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), Config.get('logging', 'path'))
LOG_FILE = os.path.join(LOG_PATH, Config.get('logging', 'log_file'))

# Logging init
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)
    open(LOG_FILE, 'a').close()

LOG_LEVEL = int(Config.get('logging', 'log_level'))
logging.getLogger().setLevel(LOG_LEVEL)  # set root logger level to config's
log = logging.getLogger('application')
log.setLevel(LOG_LEVEL)
formatter = logging.Formatter('[%(asctime)s] [%(pathname)s:%(lineno)d] %(levelname)8s: %(message)s')
handler = logging.FileHandler(LOG_FILE)
stream_handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
log.addHandler(handler)
log.addHandler(stream_handler)

# Args parse
parser = argparse.ArgumentParser()
parser.add_argument("--port",
                    help="port to run server on",
                    type=int,
                    default=Config.get('application', 'port'))
parser.add_argument("--host",
                    help="host to run server on",
                    default='127.0.0.1')
args = parser.parse_args()

# Server start
try:
    web.run_app(application, port=args.port, host=args.host)
except KeyboardInterrupt:
    application.shutdown()
