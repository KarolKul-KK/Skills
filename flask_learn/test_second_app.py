import flask
from flask import Flask
import pytest


app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

def test_hello():
    with app.test_request_context('/?name=Peter'):
        assert flask.request.path == '/'
        assert flask.request.args['name'] == 'Peter'