from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

@app.route("/api/config/202481587158093/")
def index():
    with open('data.json', 'r') as myfile:
        data=myfile.read()
    # parse file
    obj = json.loads(data)
    return obj


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=8080)