from flask import render_template, request, Response
from application import app
import requests

@app.route('/get/prize', methods=['GET','POST'])
def prize():
	data = request.get_json()
	prizeVal = str
	if data[letterVal] == "A":
		if numberVal <= 5:
			prizeVal = "no prize!"
			return Response(prizeVal, mimetype='text/plain')
		if numberVal > 5:
			prizeVal = "a small prize!"
			return Response(prizeVal, mimetype='text/plain')
	if data[letterVal] == "B":
		if numberVal <= 5:
			prizeVal = "a small prize!"
			return Response(prizeVal, mimetype='text/plain')
		if numberVal > 5:
			prizeVal = "a big prize!"
			return Response("You won" + prizeVal, mimetype='text/plain')