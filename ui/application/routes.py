from flask import render_template, jsonify
from application import app
import requests
import json

@app.route('/', methods=['GET'])
def home():
	return render_template('home.html', title='Home')

@app.route('/get/prize', methods=['GET','POST'])
def prize():
	try:
		letter = requests.get('http://lgen:5001/prize/lgen')
		number = requests.get('http://ngen:5002/prize/ngen')
		account = {"Letter Value":letter, "Number Value":number}
		jsonData = json.dumps(account)
		prize = requests.post('http://pgen:5003/prize/pgen', json=jsonData)
		print(prize.status_code)
	#prize = requests.get('http://pgen:5003/prize/pgen')
		return render_template('prize.html', title='Prize', prize=prize.text)
	except Exception as e:
		print(e)  