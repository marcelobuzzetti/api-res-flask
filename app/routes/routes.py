from app import app
from flask import jsonify
from ..views import users

@app.route('/', methods=['GET'])
def root():
    return jsonify({'message': 'Hello World!'})

@app.route('/users', methods=['POST'])
def post_users():
    return users.post_user()

@app.route('/users', methods=['GET'])
def get_users():
    return users.get_users()

@app.route('/users/<id>', methods=['PUT'])
def update_users(id):
    return users.update_user(id)