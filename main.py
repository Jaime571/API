from flask import Flask, app
from flask_cors import CORS, cross_origin
from app.api.v1 import blu_api

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(blu_api)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port = 5000)

from app.api.v1 import api

apiResource = api