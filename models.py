import os 
from peewee import *
from flask_login import UserMixin 
from playhouse.db_url import connect

if 'ON_HEROKU' in os.environ:
	DATABASE = connect(os.environ.get('DATABASE_URL'))
else:
	DATABASE = SqliteDatabase('snakes.sqlite')





class User(UserMixin, Model):
	username=CharField(unique=True)
	email=CharField(unique=True)
	password=CharField()
	occupation=CharField()

	class Meta:
		database = DATABASE


class Snake(Model):
	species = CharField() 
	habitat = CharField()
	family = CharField()
	average_size = CharField()
	venomous = CharField()
	description = TextField()
	picture = CharField()
	added_by = ForeignKeyField(User, backref='snakes')

	class Meta: 
		database = DATABASE




def initialize(): 
	DATABASE.connect()

	DATABASE.create_tables([User, Snake], safe=True)
	print('connected with the db and created tables if they werent there')
	DATABASE.close()
