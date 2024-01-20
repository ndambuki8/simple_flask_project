from flask import Flask  #import Flask class from flask module

#create an object from the Flask class
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world, from Flask!"