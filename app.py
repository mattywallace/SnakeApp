from flask import Flask, jsonify
import models
from resources.snakes import snakes
from resources.users import users 
from flask_cors import CORS 
from flask_login import LoginManager


DEBUG=True
PORT=8000






app = Flask(__name__)


app.secret_key = "Parseltounge"
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
	try:
		print('loading the following user')
		user = models.User.get_by_id(user_id)
		return user
	except models.DoesNotExist:
		return None

CORS(snakes, origins=['http://localhost:3000'], supports_credentials=True)
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)


app.register_blueprint(snakes, url_prefix='/api/v1/snakes')
app.register_blueprint(users, url_prefix='/api/v1/users')



@app.route('/')
def test_connect():
	return 'Connection Test'

@app.route('/test_json')
def test_json():
	return jsonify(['Matthew', 'Mark', 'Luke', 'John'])

if __name__ =='__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)