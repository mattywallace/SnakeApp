import models 

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

from flask_login import current_user, login_required

snakes = Blueprint('snakes', 'snakes')

@snakes.route('/', methods=['GET'])
@login_required
def snakes_index():
	""" Shows all the snakes that belong to the current user """
	
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
@login_required
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




@snakes.route('/<id>', methods=['GET'])
def show_snake(id):
	snake = models.Snake.get_by_id(id)
	if not current_user.is_authenticated:
		return jsonify(
			data={
			'species': snake.species,
			'picture': snake.picture, 
			},
			message='Login or register to learn more about each snake',
			status=200
		), 200
	else:
		snake_dict = model_to_dict(snake)
		snake_dict['added_by'].pop('password')
		return jsonify(
			data=snake_dict,
			message=f"Found dog with id {id}",
			status=200
		), 200
	






@snakes.route('/<id>', methods=['DELETE'])
@login_required
def delete_snake(id):
	try:
		snake_to_delete = models.Snake.get_by_id(id)
		if snake_to_delete.added_by.id == current_user.id:
			return jsonify(
				data={},
				message=f"Successfully deleted snake with id {id}",
				status=200
			), 200 
		else:
			return jsonify(
				data={
				'error': '403 forbidden'
				},
				message='This snake was not added by you. Only the creator of this article can remove it.',
				status=403
			), 403
	except models.DoesNotExist:
		return jsonify(
		      data={
		        'error': '404 Not found'
		      },
		      message="There is no dog with that ID.",
		      status=404
		    ), 404





@snakes.route('/<id>', methods=['PUT'])
@login_required
def update_snake(id):
	payload = request.get_json()
	snake_to_update = models.Snake.get_by_id(id)
	if snake_to_update.added_by.id == current_user.id:
		if 'description' in payload:
			snake_to_update.descrption = payload['description']
		if 'picture' in payload:
			snake_to_update.picture = payload['picture']
		snake_to_update.save()
		updated_snake_dict = model_to_dict(snake_to_update)
		updated_snake_dict['added_by'].pop('password')
		return jsonify(
        	data=updated_snake_dict,
        	message=f"Successfully updated snake with id {id}",
        	status=200
      	), 200
	else:
		return jsonify(
			data={
			'error':'403 Forbidden'
			},
			message="Only the user who created the article can update the snake",
			status=403
		), 403 

      



		


		
