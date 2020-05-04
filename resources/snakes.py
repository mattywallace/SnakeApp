import models 

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

from flask_login import current_user

snakes = Blueprint('snakes', 'snakes')

@snakes.route('/', methods=['GET'])
def snakes_index():
	current_user_snake_dicts = [model_to_dict(snake) for snake in current_user.snakes]
	
	for snake_dict in current_user_snake_dicts:
		snake_dict['added_by'].pop('password')
	print('this is snake dicts')
	print(current_user_snake_dicts)
	return jsonify({
		'data': current_user_snake_dicts,
		'message': f" Successfully found {len(current_user_snake_dicts)} snakes",
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
		return jsonify(
			data={},
			message='this snake already exists',
			status=400
		), 400
	except models.DoesNotExist:
		new_snake = models.Snake.create(
			species=payload['species'],
			family=payload['family'],
			average_size=payload['average_size'],
			habitat=payload['habitat'],
			venomous=payload['venomous'],
			description=payload['description'],
			added_by=current_user.id,
			picture=payload['picture']
		)
		snake_dict = model_to_dict(new_snake)
		print(snake_dict)
		snake_dict['added_by'].pop('password')
		return jsonify(
			data=snake_dict,
			message='You have created a snake',
			status=201
			), 201

@snakes.route('/<id>', methods=['DELETE'])
def delete_snake(id):
	delete_query = models.Snake.delete().where(models.Snake.id == id)
	num_of_rows_deleted = delete_query.execute()
	print(num_of_rows_deleted)
	return jsonify(
		data={},
		message="Successfully deleted {} snake with id {}".format(num_of_rows_deleted, id),
		status=200,
	), 200




@snakes.route('/<id>', methods=['PUT'])
def update_snake(id):
	payload = request.get_json()
	update_query = models.Snake.update( 
		description=payload['description'],
		picture=payload['picture']
	).where(models.Snake.id == id)
	num_of_rows_modified = update_query.execute()
	updated_snake = models.Snake.get_by_id(id)
	updated_snake_dict = model_to_dict(updated_snake)
	return jsonify(
		data=updated_snake_dict, 
		message=f"Successsfully updated snake with id {id}",
		status=200
	), 200



		


		
