import models
from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash
from playhouse.shortcuts import model_to_dict

users = Blueprint('users', 'users')


@users.route('/', methods=['GET'])
def test_user_resource():
	return "user resource works"


@users.route('/register', methods=['POST'])
def register():
	payload = request.get_json()
	payload['username'] = payload['username'].lower()
	payload['email'] = payload['email'].lower()
	try:
		models.User.get(models.User.email == payload['email'])
		return jsonify(
			data={},
			message="a user with that email already exists",
			status=401
		), 401
	except models.DoesNotExist:
		pw_hash = generate_password_hash(payload['password'])
		created_user = models.User.create(
			username=payload['username'],
			email=payload['email'],
			occupation=payload['occupation'],
			password=pw_hash
			)
		print(created_user)
		created_user_dict = model_to_dict(created_user)
		print(created_user_dict)
		print(type(created_user_dict['password']))
		created_user_dict.pop('password')
		return jsonify(
			data=created_user_dict,
			message='succefully registered user',
			status=201
		), 210




			