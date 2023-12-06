from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy();

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    state = db.Column(db.String(80))
    town = db.Column(db.String(80))
    address = db.Column(db.String(80))
    phone = db.Column(db.String(80))
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, first_name, last_name, state, town, address, phone, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.state = state
        self.town = town
        self.address = address
        self.phone = phone
        self.email = email
        self.password = password

    def json(self):
        return {
            "first_name":self.first_name,
            "last_name":self.last_name,
            "state":self.state,
            "town":self.town,
            "address":self.address,
            "phone":self.phone,
            "email":self.email,
            "password":self.password
            }