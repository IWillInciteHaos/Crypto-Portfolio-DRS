from flask import request
from flask_restful import Resource
from models import UserModel, db

class UsersView(Resource):
    def get(self):
        users = UserModel.query.all()
        return {'Users':list(u.json() for u in users)}

    def post(self):
        data = request.get_json()
        new_user = UserModel(data['first_name'], data['last_name'], data['state'], data['town'], data['address'], data['phone'], data['email'], data['password'])
        db.session.add(new_user)
        db.session.commit()
        db.session.flush()

        return new_user.json(), 201



