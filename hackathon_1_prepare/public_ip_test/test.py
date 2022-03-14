from flask import Flask, request, jsonify
from requests import get
import json
app = Flask(__name__)


@app.route('/predict', methods=['GET'])
def service():
    return 'Hello world'


if (__name__ == '__main__'):
    ip = get('https://api.ipify.org').text
    print("IP:"+ip)
    app.run(port=8000, debug=True, use_debugger=False,
            use_reloader=False, passthrough_errors=True)
