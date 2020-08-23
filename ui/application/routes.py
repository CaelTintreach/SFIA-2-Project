from flask import render_template, jsonify
from application import app
import requests
import json

@app.route('/', methods=['GET'])
def home():
	return render_template('home.html', title='Home')

@app.route('/get/prize', methods=['GET','POST'])
def prize():
	letter = requests.get('http://lgen:5001/prize/lgen')
	number = requests.get('http://ngen:5002/prize/ngen')
	prize = requests.post('http://pgen:5003/prize/pgen', json={"Letter":letter.text, "Number":number.text})
	#prize = requests.post('http://pgen:5003/prize/pgen', json={"Letter":"A", "Number":"A"})
	return render_template('prize.html', title='Prize', prize=prize.text)