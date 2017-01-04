from sanic.response import json
from sanic.views import HTTPMethodView

from database import DB
from utils.parser import parse_form, jsonify

import bcrypt

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

    async def delete(self, request):
        result = await DB.delete(User.__table__).execute()
        return json({'deleted': jsonify(result)})
