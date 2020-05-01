from flask import Flask, jsonify
import models
from resources.snakes import snakes


DEBUG=True
PORT=8000






app = Flask(__name__)
app.register_blueprint(snakes, url_prefix='/api/v1/snakes')





@app.route('/')
def test_connect():
	return 'Connection Test'

@app.route('/test_json')
def test_json():
	return jsonify(['Matthew', 'Mark', 'Luke', 'John'])

if __name__ =='__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)