from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

from werkzeug.utils import secure_filename

import os


app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.imgdata

@app.route('/')
def home():
    return render_template('main.html')

@app.route("/photoImg", methods=['POST'])
def upload():
    img = request.files['image']
    img.save('./static/'+secure_filename(img.filename))
    return render_template('main.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)