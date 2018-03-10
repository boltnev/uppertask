import os

API_TOKEN = 'API_TOKEN'
API_TOKEN_SECRET = 'API_TOKEN_SECRET'
TOKEN = 'TOKEN'
BOARD = 'BOARD'
FULLSCREEN = False
FONT = None
ALL_DONE_MESSAGE = "DONE!!!"

if os.path.exists(os.path.join(os.path.dirname(__file__), 'cfg_local.py')):
    exec(open(os.path.join(os.path.dirname(__file__), 'cfg_local.py' )).read())
