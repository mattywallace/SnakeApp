from peewee import *
from flask_login import UserMixin 

DATABASE = SqliteDatabase('snakes.sqlite')


# class User(UserMixin, Model):
# 	username=CharField(unique=True)
# 	email=CharField(unique=True)
# 	password=CharField()
# 	occupation=CharField()

# 	class Meta:
# 		datbase = DATABASE


class Snake(Model):
	species = CharField() 
	habitat = CharField()
	family = CharField()
	average_size = IntegerField()
	venomous = BooleanField()
	description = TextField()
	picture = CharField()
	added_by = CharField()

	class Meta: 
		database = DATABASE




def initialize(): 
	DATABASE.connect()

	DATABASE.create_tables([Snake], safe=True)
	print('connected with the db and created tables if they werent there')
	DATABASE.close()
