from flask import Flask
import flask
import pytest

app = Flask(__name__)


@app.route('/')
def index():
    return "Index Page"


@app.route('/hello')
def hello():
    return 'Hello World'


def test_index():
    assert index() == "Index Page"


def test_hello():
    with app.test_request_context('/hello'):
        assert flask.request.path == '/hello'
        assert hello() == 'Hello World'