from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'yo'

@app.route('/candy')
def candy():
    return 'chocolate'

@app.route('/greeting')
def greeting():
    return 'hello!'