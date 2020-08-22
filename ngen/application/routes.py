from application import app
from flask import request, Response 
import random

@app.route('/prize/ngen', methods = ['GET'])
def lGen():
	number = random.randint(1,10)
	return Response(number, mimetype='text/plain')

