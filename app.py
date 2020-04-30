from flask import Flask, jsonify

DEBUG=True
PORT=8000

app = Flask(__name__)

@app.route('/')
def test_connect():
	return 'Connection Test'

@app.route('/test_json')
def test_json():
	return jsonify(['Matthew', 'Mark', 'Luke', 'John'])

if __name__ =='__main__':
	app.run(debug=DEBUG, port=PORT)