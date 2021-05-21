from flask import Flask
import pytest


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def test_hello_world():
    assert hello_world() == "<p>Hello, World!</p>"