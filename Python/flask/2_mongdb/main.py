import pymongo
# from flask import Flask


client = pymongo.MongoClient("mongodb://localhost:27017")

mydb = client['drama']
mycol = mydb['tvd']


new = {
    'actor': 'kol',
    'character':'mikaelson',
    'gender':'male',
    'age':42
}
print(mycol.find_one())

# app = Flask(__name__)

# @app.route('/')
# def home():
    # return "<h1> Home Page </h1>"

# app.run()