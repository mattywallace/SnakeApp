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
	return " We have hit the snake create route -- check terminal"