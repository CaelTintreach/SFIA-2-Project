from flask import render_template, request, Response
from application import app
import requests

@app.route('/prize/pgen', methods=['GET','POST'])
def prize():
	data = request.get_json()
	prizeVal = ""
	if data[letter.text] == "A":
		if data[number.text] == "A":
			prizeVal = "no prize!"
			return Response(prizeVal, mimetype='text/plain')
		if data[number.text]  == "B":
			prizeVal = "a small prize!"
			return Response(prizeVal, mimetype='text/plain')
	if data[letter.text] == "B":
		if data[number.text]  == "A":
			prizeVal = "a small prize!"
			return Response(prizeVal, mimetype='text/plain')
		if data[number.text]  == "B":
			prizeVal = "a big prize!"
			return Response("You won" + prizeVal, mimetype='text/plain')