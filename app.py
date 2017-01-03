import os
from sanic import Sanic
from sanic.response import json
import asyncio
import uvloop

import config

from blueprints import Blueprints

from database import init_db

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

loop = asyncio.get_event_loop()

app = Sanic(__name__)

app.blueprint(Blueprints.auth, url_prefix='/api/auth')

loop.create_task(init_db())

app.go_fast(port=config.PORT, debug=config.DEBUG, workers=1, loop=loop)
