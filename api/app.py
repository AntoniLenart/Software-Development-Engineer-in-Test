# https://www.youtube.com/watch?v=qbLc5a9jdXo

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy\


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drinks.db'
db = SQLAlchemy(app)


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'Drink {self.name} - {self.price}'


@app.route('/')
def index():
    return 'Hello, World! This is a Flask API running in a Docker container.'


@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    return {'drinks': [{'id': drink.id, 'name': drink.name, 'price': drink.price} for drink in drinks]}


@app.route('/drinks/<int:drink_id>')
def get_drink(drink_id):
    drink = Drink.query.get_or_404(drink_id)
    return {'name': drink.name, 'price': drink.price}


@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], price=request.json['price'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id, 'name': drink.name, 'price': drink.price}, 201


@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
def delete_drink(drink_id):
    drink = Drink.query.get(drink_id)
    if not drink:
        return {'error': 'Drink not found'}, 404
    db.session.delete(drink)
    db.session.commit()
    return {"message": "Drink deleted successfully"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
