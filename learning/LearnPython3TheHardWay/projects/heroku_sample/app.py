from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello This is TamNguyen reading PyMi.vn!"
