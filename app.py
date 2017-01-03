import os
from sanic import Sanic
from sanic.response import json

from asyncpg import create_pool

from config import Config
from blueprints import Blueprints

app = Sanic(__name__)

app.register_blueprint(Blueprints.auth, url_prefix='/api/auth')

app.go_fast(port=Config.PORT, debug=Config.DEBUG, workers=os.cpu_count())
