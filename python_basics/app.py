from flask import Flask
import DICE
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Witaj, świecie!'

if __name__ == 'DICE'
    app.run()