import models 

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

snakes = Blueprint('snakes', 'snakes')

@snakes.route('/', methods=['GET'])
def snakes_index():
	return 'snakes resource and index route hitting'

@snakes.route('/', methods=['POST'])
def create_snake():
	payload = request.get_json()
	print(payload)
	new_snake = models.Snake.create(
					species=payload['species'],
					family=payload['family'],
					habitat=payload['habitat'],
					venomous=payload['venomous'],
					average_size=payload['average_size'],
					picture=payload['picture'],
					description=payload['description'],
					added_by=payload['added_by']
				)
	print(new_snake)
	print(new_snake.__dict__)
	print(dir(new_snake))
	snake_dict = model_to_dict(new_snake)
	return jsonify(
		data=snake_dict,
		message='You have created a snake',
		status=201
	), 201


