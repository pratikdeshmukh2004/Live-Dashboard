from datetime import datetime

from app import database


class Meals(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100))
    image = database.Column(database.String(100))
    content = database.Column(database.String(500), default='')

database.create_all()
database.session.commit()