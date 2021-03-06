import models
from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
from flask_login import login_user, current_user, logout_user

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
				message=f"A user with {payload['email']} already exists",
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
		login_user(created_user)
		created_user_dict = model_to_dict(created_user)
		print(created_user_dict)
		print(type(created_user_dict['password']))
		created_user_dict.pop('password')
		return jsonify(
			data=created_user_dict,
			message=f"succefully registered {created_user_dict['username']}",
			status=201
		), 210



@users.route('/login', methods=['POST'])
def login():
	payload = request.get_json()
	payload['email'] = payload['email'].lower()
	payload['username'] = payload['username'].lower()
	try:
		user = models.User.get(models.User.email == payload['email'])
		user_dict = model_to_dict(user)
		password_is_good =check_password_hash(user_dict['password'], payload['password'])
		if(password_is_good):
			login_user(user)
			user_dict.pop('password')
			return jsonify(
				data=user_dict,
				message=f"successfully logged in {user_dict['email']}",
				status=200
				)
		else:
			print('password already exists')
			return jsonify(
				data={},
				message="Email or password is incorrect",
				status=401
			), 401

	except models.DoesNotExist:
		print('user name does not exist')
		return jsonify(
			data={},
			message="email or passwrod is incorrect",
			status=401
		), 401

			


@users.route('/all', methods=['GET'])
def user_index():
		users = models.User.select()
		user_dicts = [model_to_dict(user) for user in users]
		for user_dict in user_dicts:
			user_dict.pop('password')
		print(user_dicts)
		return jsonify(user_dicts), 200



@users.route('/logged_in_user', methods=['GET'])
def get_logged_in_user():
	print(current_user)
	user_dict = model_to_dict(current_user)
	user_dict.pop('password')
	if not current_user.is_authenticared:
		return jsonify(
			data={},
			message="No user is currently logged in ",
			status=401
		), 401
	else:
		user_dict =model_to_dict(current_user)
		user_dict.pop('password')
		return jsonify(
			data=user_dict,
			message=f"currently logged in as {user_dict['email']}.",
			status=200
		), 200


@users.route('/logout', methods=['GET'])
def logout():
	logout_user()
	return jsonify(
		data={},
		message="You have logged out of your account",
		status=200
	), 200 