from unittest.mock import patch

from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
	def create_app(self):
		#pass in cofigurations for test database
		return app

class TestViews(TestBase):
	def test_home_view(self):
		with patch('request.get') as g:
			g.return_value.text = "A"
		with patch('request.get') as g2:
			g2.return_value.text = "A"
			