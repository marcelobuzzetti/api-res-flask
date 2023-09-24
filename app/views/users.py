from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.users import Users, user_schema, users_schame

def post_user():
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']
    pass_hash = generate_password_hash(password)
    user = Users(username, pass_hash, name, email)

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'successfully registered', 'data': result.data}), 201
    except Exception as erro:
        print(erro)
        print(type(erro))
        return jsonify({'message': 'unable to create', 'data': {}}), 500   

