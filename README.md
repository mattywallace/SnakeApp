


---------------MODELS----------------- 

User Model

class User(UserMixin, Model):
	username=CharField(unique=true)
	email=CharField(unique=true)
	password=CharField()
	occupation=CharField()




Snake Model 

class Snake(Model):
	species = charField() 
	location = CharField()
	family = CharFeild()
	average_size = IntegerFeild()
	venomous = BooleanField()
	description = TextField()
	added_by = ForeignKeyField( User, backref='snakes')


----------------ROUTES-----------------

SNAKE ROUTES 


<!-- Test Route

@app.route('/test_route/username')
	def say_hello(username)
	return "Hello {}".format(username)



Snakes DUMMY Route 

@app.route('/', methods=['GET'])
def snakes_index():
	return 'Snakes resource working' -->



Snakes Routes 

POST /api/v1/snakes/<owner_id>

GET /api/v1/snakes

DELETE /api/v1/snakes/<id>

PUT /api/v1/snakes/<id>

GET /api/v1/snakes/<id>

User Routes

POST /api/v1/users/register

GET /api/v1/users/<id>

GET /api/v1/users/logged_in_user


<!-- @snakes.route('/<owner_id>', methoda=['POST'])
@login_required
def create_snake(owner_id):
""" Creates a snake in the database """
	payload = request.get_json()
	print(payload)
	new_snake = models.Snake.create(
		species=payload['species'],
		locaiton=payload['locaiton'],
		family=payload['family'],
		average_size=payload['average_size'],
		venomous=payload['venomous'],
		description=payload['description'],
		added_by=current_user.id
	)
	snake_dict['owner'].pop('password')
	return jsonify(
		data=snake_dict,
		message='A SSSerpent has slithered into the database'
		status=201
	), 201



snakes INDEX Route 

@snakes.route('/', methods=['GET'])
@login_required
def snakes_index():
	current_user_snake_dicts = [model_to_dict(snake) for dog in current_user.snakes]
	snake_dicts = [model_to_dict(snake) for snake in result]
	return jsonify({
		'data': current_user_snake_dicts,
		'message': f"We found {len(current_user_snakes_dicts)} snakes",
		'status': 200
 	}), 200




snakes DELETE route 

@snakes.route('/<id>', methods=['DELETE'])
@login_required
def delete_snake(id):
	try:
		snake_to_delete = models.Snake.get_by_id(id)
		if snake_to_delete.owner.id == current_user.id:
			snake_to_delete.delete_instance()
			return jsonify(
				data={},
				message="Successfully deleted snake with id {}". format(id)
				status=200
			), 200
		else:
			return jsonify(
				data={'error': '403 Forbidden'},
				message='Snake creaters id does not match the snakes id.',
				status=403
			), 403
	except models.DoesNotExist:
		return jsonify(
			data={'error': '404 not found'},
			messsage='There is no snake with that id',
			status=404
		), 404





snakes UPDATE route 

@snakes.route('/<id>', methods['PUT'])
@login_required
	def update_snake_description(id)
	snake_to_update = models.Snake.get_by_id()id
	if snake_to_update.owner.id == current_user.id:
		if 'description' in payload:
			snake_to_update.description = payload['description']
			snake_to_update.save()
			updated_snake_dict = model_to_dict(snake_to_update)
			update_snake_dict['added_by'].pop('password')
			return jsnonify(
				data=updated_snake_dict,
				message=f"Successfully updated dog with id {id}",
				status=200
		  	), 200
		else:
			return jsonify(
				data{'error': '403 Forbidden'}
				message='Snake creators id does not match snakes id',
				status=403
			), 403


Snakes SHOW route 

@snakes.route('/<id>', methods=['GET'])
def show_snake(id):
	snake = models.Snake.get_by_id(id)
	if not current_user.is_authenticated:
		return jsonify(
			data={
				'species': snake.species,
				'location': snake.location,
				'family': snake.family,
				'average_size': snake.average_size,
				'venomous': snake.venomouse,
				'description': snake.description
			},
			message='Registered user can see more info about this snake'
			status=200
		), 200
	else:
		snake_dict = model_to_dict(snake)
		dog_dict['added_by'].pop('password')
		if snake.added_by.id != current_user.id:
			snake_dict.pop('created_at')
		return jsonify(
			data=snake_dict,
			message=f"Found snake with id {id}"",
			status=200
		), 200



----------------------------------------------------------

USER ROUTES

User Register Route 

@users.route('/register', methods=['POST'])
def register():
	payload = request.get_json()
	payload['email'] = payload['email'].lower()
	payload['username'] = payload['userman'].lower()
	print(payload)
	try:
		models.User.get(models.User.email == payload['email'])
		return jsonify(
			data={},
			message="A user with that email already exists",
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
		login_user(created_user)
		created_user_dict = model_t_dict(created_user)
		print(created_user_dict)
		print(type(created_user_dict['password']))
		created_user_dict.pop('password')
		return jsonify(
			data=created_user_dict,
			message='Successfully registed user',
			status=201
		), 201



User Loader Route

@login_manager.user_loader
def load_user(user_id):
	try:
		return models.User.get(user_id)
	except models.DoesNotExist:
		return None 




User Current_User Route

@users.route('/logged_in_user', methods=['GET'])
def get_logged_in_user():
	print(current_user)
	prtin(type(current_user))
	if not current_user.is_authenticated:
		return jsonify(
			data={},
			message'No user is currently logged in",
			status=401,
		), 401
	else:
		user_dict = model_to_dict(current_user) 
		user_dict.pop('password')
		return jsonify(
			data=user_dict,
			message=f"Currently logged in as {user_dict['email']}.",
			status=200
		), 200



Custom Authentication Route 

@login_manager.unathorized_handler
def unauthorized():
	return jsonify(
		data={'Error':'User not logged in'},
		message'You must be logged in to access this",
		status=401
	), 401 -->
	























