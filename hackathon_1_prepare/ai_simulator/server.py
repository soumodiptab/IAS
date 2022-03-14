from flask import Flask, request, jsonify
from requests import get
from random import randint
import json
app = Flask(__name__)


@app.route('/predict', methods=['GET'])
def service():
    return jsonify({"output": randint(1, 2000)})


if (__name__ == '__main__'):
    app.run(port=8001, debug=True, use_debugger=False,
            use_reloader=False, passthrough_errors=True)
