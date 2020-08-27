from flask import render_template, jsonify
from application import app, db
from application.models import Prizes
import requests
import json

@app.route('/', methods=['GET'])
def home():
	return render_template('home.html', title='Home')

@app.route('/get/prize', methods=['GET','POST'])
def prize():
	letter = requests.get('http://lgen:5001/prize/lgen')
	number = requests.get('http://ngen:5002/prize/ngen')
	prize = requests.post('http://pgen:5000/prize/pgen', json={'Letter':letter.text, 'Number':number.text})
	db.session.add(prize.text)
	db.session.commit
	return render_template('prize.html', title='Prize', prize=prize.text)