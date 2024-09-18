# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Render! This is a simple Flask app."

if __name__ == "__main__":
    app.run(debug=True)
