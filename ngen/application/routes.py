from application import app
from flask import request, Response 
import random

@app.route('/prize/ngen', methods = ['GET'])
def lGen():
	return Response(random.randint(1,10), mimetype='text/plain')