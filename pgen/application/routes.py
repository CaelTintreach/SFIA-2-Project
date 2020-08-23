from flask import render_template, request, Response
from application import app
import requests

@app.route('/prize/pgen', methods=['GET','POST'])
def prize():
	data = request.get_json()
	prizeVal = ""
	if data["Letter"] == "A":
		if data["Number"] == "A":
			prizeVal = "no prize!"
			return Response("You won" + prizeVal, mimetype='text/plain')
		if data["Number"]  == "B":
			prizeVal = "a small prize!"
			return Response("You won" + prizeVal, mimetype='text/plain')
	if data["Letter"] == "B":
		if data["Number"]  == "A":
			prizeVal = "a small prize!"
			return Response("You won" + prizeVal, mimetype='text/plain')
		if data["Number"]  == "B":
			prizeVal = "a big prize!"
			return Response("You won" + prizeVal, mimetype='text/plain')