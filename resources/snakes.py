import models 

from flask import Blueprint, request

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
	return " We have hit the snake create route -- check terminal"


