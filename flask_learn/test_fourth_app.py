from flask import Flask


def create_app():
    app = Flask(__name__)
    return app


def test_create_app():
    assert create_app()  app