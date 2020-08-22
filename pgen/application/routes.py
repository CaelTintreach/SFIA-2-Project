from flask import render_template, request, Response
from application import app
import requests

@app.route('/prize/pgen', methods=['GET','POST'])
def prize():
	data = request.get_json()
	prizeVal = ""
	if data["Letter Value"] == "A":
		if data["Number Value"] <= 5:
			prizeVal = "no prize!"
			return Response(prizeVal, mimetype='text/plain')
		if data["Number Value"]  > 5:
			prizeVal = "a small prize!"
			return Response(prizeVal, mimetype='text/plain')
	if data["Letter Value"] == "B":
		if data["Number Value"]  <= 5:
			prizeVal = "a small prize!"
			return Response(prizeVal, mimetype='text/plain')
		if data["Number Value"]  > 5:
			prizeVal = "a big prize!"
			return Response("You won" + prizeVal, mimetype='text/plain')