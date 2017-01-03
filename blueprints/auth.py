from sanic.response import json
from sanic import Blueprint
from database import DB

import bcrypt
import jwt

import config
from models.user import User

from utils import parse_form

bp = Blueprint(__name__)

@bp.route('/', methods=['GET'])
async def index(request):
    users = await DB.select([User]).execute()
    return json({'users': users})

@bp.route('/new', methods=['POST'])
async def new(request):
    form = parse_form(request.form, ['username', 'password'])
    user = await DB.select([User]).where(User.username == form['username']).execute()
    if len(user):
        return json({'msg': 'user exists'})
    else:
        form['password'] = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
        await DB.insert(User.__table__).values(form).execute()
        user = await DB.select([User]).where(User.username == form['username']).execute()
        return json({'user': user[0]})

@bp.route('/login', methods=['POST'])
async def login(request):
    form = parse_form(request.form, ['username', 'password'])
    user = await DB.select([User]).where(User.username == form['username']).execute()
    if len(user):
        if bcrypt.checkpw(form['password'].encode(), user[0]['password'].encode()):
            return json({'token': jwt.encode({'username': form['username']}, config.SECRET, algorithm='HS256')})
        return json({'msg': 'wrong password'})
    else:
        return json({'msg': 'user not exists'})

@bp.route('/refresh', methods=['GET'])
async def refresh(request):
    await DB.delete(User.__table__).execute()
    return json({'msg': 'all users deleted'})
