from flask import Flask

app = Flask(__quiambao__)

@app.route('/')
def home():
    return "Hello! Your cloud server is working!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)