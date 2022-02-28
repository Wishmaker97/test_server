from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

@app.route("/api/config/L293EGS/")
def index():
    with open('data.json', 'r') as myfile:
        data=myfile.read()
    # parse file
    obj = json.loads(data)
    return obj

app.run(host="0.0.0.0", port=8080)