from sanic.response import json
from sanic import Blueprint

import bcrypt
import jwt

from config import Config
from models.user import User

bp = Blueprint('auth')

@bp.route('/', methods=['GET'])
async def index(request):
    with scoped_session() as session:
        users = [u.jsonify() for u in session.query(User).all()]
    return json({'users': users})
