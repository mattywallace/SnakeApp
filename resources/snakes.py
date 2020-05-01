import models 

from flask import Blueprint

snakes = Blueprint('snakes', 'snakes')

@snakes.route('/', methods=['GET'])
def snakes_index():
	return 'snakes resource and index route hitting'

@snakes.route('/', methods=['POST'])
def create_snake():
	return " We have hit the snake create route"