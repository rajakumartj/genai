# python -m flask --app .\sampleflaskapp\app.py run <-- run this command in Terminal
# Open the app in browser --->http://127.0.0.1:5000

from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "Hello world, from flask!"