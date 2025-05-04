from flask import Blueprint, request, jsonify
from .db import mongo

users_bp = Blueprint('users', __name__)


@users_bp.route('/users', methods=['GET'])
def get_users():
    users = list(mongo.db.users.find({}, {'_id': 0}))
    return jsonify(users), 200


@users_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Missing "name" field'}), 400

    mongo.db.users.insert_one({'name': data['name']})
    return jsonify({'message': 'User added'}), 201
