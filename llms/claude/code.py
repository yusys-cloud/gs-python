import os
from claude_api import Client

cookie = os.environ.get('cookie')
claude_api = Client(cookie)
