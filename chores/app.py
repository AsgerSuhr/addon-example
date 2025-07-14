from flask import Flask
from flask_cors import CORS 

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, origins=['http://localhost:8000', 'https://home.asgerlanghoff.com'])

@app.route("/")
def hello_world():
    return "Hey, we have Flask in a Docker container!"

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
