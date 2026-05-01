from flask import Flask

app = Flask(__quiambao__)

@app.route('/')
def home():
    return "Hello! Your cloud server is working!"
