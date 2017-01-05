from sanic.response import json
from sanic.views import HTTPMethodView

from database import DB
from utils.parser import parse_form, jsonify

import bcrypt

from models import Models


class UserHandler(HTTPMethodView):

    async def get(self, request):
        users = await DB.select([Models.User]).execute()
        return json({'users': jsonify(users)})

    async def post(self, request):
        form = parse_form(request.form, ['username', 'password'])
        user = await DB.select([Models.User]).where(
            Models.User.username == form['username']).execute()
        if len(user):
            return json({'msg': 'user exists'})
        else:
            form['password'] = bcrypt.hashpw(
                form['password'].encode(), bcrypt.gensalt()).decode()
            user = await DB.insert(Models.User).values(form).execute()
            return json({'user': jsonify(user)[0]})

    async def delete(self, request):
        result = await DB.delete(Models.User).execute()
        return json({'deleted': jsonify(result)})
