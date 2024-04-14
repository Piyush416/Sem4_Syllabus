from flask import Flask

from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
db = PyMongo(app).db


@app.route("/")
def hello_world():
    db.table1.insert_one({"a":1})
    return "<h1>Hello, World!</h1>"

app.run(debug=True)