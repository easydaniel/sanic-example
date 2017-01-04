from sanic.response import json
from sanic.views import HTTPMethodView

from database import DB
from utils import parse_form, jsonify

import config
import jwt
import bcrypt

from models.user import User


class AuthHandler(HTTPMethodView):

    async def post(self, request):
        form = parse_form(request.form, ['username', 'password'])
        user = await DB.select([User]).where(
            User.username == form['username']).execute()
        obj = {'username': form['username']}
        if len(user):
            if bcrypt.checkpw(
                    form['password'].encode(), user[0]['password'].encode()):
                return json({'token':
                             jwt.encode(obj,
                                        config.SECRET, algorithm='HS256')})
            return json({'msg': 'wrong password'})
        else:
            return json({'msg': 'user not exists'})