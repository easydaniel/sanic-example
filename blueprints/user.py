from sanic.response import json
from sanic.views import HTTPMethodView

from database import DB
from utils import parse_form, jsonify

import bcrypt
import jwt
import config

from models.user import User


class UserHandler(HTTPMethodView):

    async def get(self, request):
        users = await DB.select([User]).execute()
        return json({'users': jsonify(users)})

    async def post(self, request):
        form = parse_form(request.form, ['username', 'password'])
        user = await DB.select([User]).where(
            User.username == form['username']).execute()
        if len(user):
            return json({'msg': 'user exists'})
        else:
            form['password'] = bcrypt.hashpw(
                form['password'].encode(), bcrypt.gensalt()).decode()
            user = await DB.insert(User.__table__).values(form).execute()
            return json({'user': jsonify(user)[0]})


@bp.route('/login', methods=['POST'])
async def login(request):
    form = parse_form(request.form, ['username', 'password'])
    user = await DB.select([User]).where(
        User.username == form['username']).execute()
    obj = {'username': form['username']}
    if len(user):
        if bcrypt.checkpw(
                form['password'].encode(), user[0]['password'].encode()):
            return json({'token':
                         jwt.encode(obj, config.SECRET, algorithm='HS256')})
        return json({'msg': 'wrong password'})
    else:
        return json({'msg': 'user not exists'})


@bp.route('/refresh', methods=['GET'])
async def refresh(request):
    result = await DB.delete(User.__table__).execute()
    return json({'deleted': jsonify(result)})
