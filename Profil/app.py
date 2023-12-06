from flask import Flask
from flask_restful import Api

from models import db
from users import UsersView

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db.init_app(app)


@app.before_request
def create_table():
    db.create_all()


api.add_resource(UsersView, '/users')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
