import models 

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

snakes = Blueprint('snakes', 'snakes')

@snakes.route('/', methods=['GET'])
def snakes_index():
	result = models.Snake.select()
	print('')
	print('result of snake select query')
	print(result)
	snake_dicts= [model_to_dict(snake) for snake in result]
	print('this is snake dicts')
	print(snake_dicts)
	return jsonify({
		'data': snake_dicts,
		'message': f" Successfully found {len(snake_dicts)} snakes",
		'status': 200
	}) 


@snakes.route('/', methods=['POST'])
def create_snake():
	payload = request.get_json()
	print(payload)
	try:
		snake = models.Snake.get(models.Snake.species == payload['species'])
		print('this is the snake on try')
		print(snake)
		return print('this snake is already created')
	except models.DoesNotExist:
		new_snake = models.Snake.create(**payload)
		print('this is the snake on except')
		print(new_snake)
		print(new_snake.__dict__)
		print(dir(new_snake))
		snake_dict = model_to_dict(new_snake)
		return jsonify(
			data=snake_dict,
			message='You have created a snake',
			status=201
			), 201


