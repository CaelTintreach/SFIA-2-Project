from application import app
from flask import request, Response 
import random

'''
@app.route('/prize/ngen', methods = ['GET'])
def nGen():
	number = random.randint(1,10)
	print(number)
	return Response(number, mimetype='text/plain')

print(nGen())
'''

@app.route('/prize/ngen', methods = ['GET'])
def nGen():
	prizePool = ["A", "B"]
	return Response(random.choice(prizePool), mimetype='text/plain')
	#return Response("B", mimetype='text/plain')