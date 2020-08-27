from application import db

class Prizes(db.method):
	id = db.Column(db.Integer, primary_key=True)
	prize = db.Column(db.String(20))
	prize = db.Column(db.String(20))