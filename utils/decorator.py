from sanic.response import json

import config
import jwt

from models.user import User

def authenticated(func):
    """Checks whether user is logged in"""
    def decorator(request, *args, **kwargs):
        profile = None
        try:
            token = request.headers['Authorization'].split(' ')[1]
            profile = jwt.decode(token, config.SECRET, algorithms='HS256')
            return func(request, profile, *args, **kwargs)
        except:
            if profile:
                return json({'err': 'unknown token'}, 401)
            else:
                return json({'err': 'token not provided'}, 401)
    return decorator
