from flask import Flask, request, jsonify
import json
import pickle
import pandas as pd
app = Flask(__name__)


def load_ai_files():
    global test_data
    global model
    global passengers
    test_data = pd.read_csv('testing_data.csv')
    passengers=pd.read_csv('passengers.csv')
    pickle_in = open("model.pickle", "rb")
    model = pickle.load(pickle_in)
    pickle_in.close()


def make_prediction(data):
    global test_data
    global model
    global passengers
    query=test_data[passengers[]]
    y_pred = model.predict(data)
    return y_pred


@app.route('/predict', methods=['POST'])
def service():
    info = request.get_json()
    passengers = info['passenger_ids']
    values = make_prediction(passengers)
    return jsonify({'prediction': values})


if (__name__ == '__main__'):
    load_ai_files()
    app.run(port=8000, debug=True, use_debugger=False,
            use_reloader=False, passthrough_errors=True)
