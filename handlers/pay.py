from sanic.response import json
from sanic.views import HTTPMethodView

from sqlalchemy import and_, or_

from database import DB
from utils.parser import parse_form, jsonify

from models import Models


class PayHandler(HTTPMethodView):

    async def get(self, request, profile):
        ingress = await DB.select([Models.Pay]).where(Models.Pay.owner == profile['username']).execute()
        egress = await DB.select([Models.Pay]).where(Models.Pay.borrower == profile['username']).execute()
        return json({'ingress': jsonify(ingress), 'egress': jsonify(egress)})

    async def post(self, request, profile):
        form = parse_form(request.form, ['owner', 'borrower', 'money'])
        form['money'] = int(form['money'])
        if form['money'] < 0:
            form['money'] *= -1
            form['owner'], form['borrower'] = form['borrower'], form['owner']
        pays = await DB.select([Models.Pay]).where(
            or_(
                and_(
                    Models.Pay.owner == form['owner'],
                    Models.Pay.borrower == form['borrower']),
                and_(
                    Models.Pay.owner == form['borrower'],
                    Models.Pay.borrower == form['owner']))).execute()
        if len(pays):
            pay = jsonify(pays)[0]
            _id = pay.pop('id')
            if pay['owner'] == form['owner']:
                pay['money'] += int(form['money'])
            else:
                pay['money'] -= int(form['money'])

            if pay['money'] == 0:
                await DB.delete(Models.Pay).where(Models.Pay.id == _id).execute()
                return json({'msg': 'clear debt'})
            if pay['money'] < 0:
                pay['money'] *= -1
                pay['owner'], pay['borrower'] = pay['borrower'], pay['owner']
            pays = await DB.update(Models.Pay).where(Models.Pay.id == _id).values(pay).execute()
            return json(jsonify(pays)[0])
        else:
            pays = await DB.insert(Models.Pay).values(form).execute()
            return json(jsonify(pays)[0]))
