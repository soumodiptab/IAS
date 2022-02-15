from flask import Flask, request, jsonify
import json
import pickle
import pandas as pd
app = Flask(__name__)


def load_ai_files():
    global test_data
    global model
    global passengers
    test_data = pd.read_csv('testing_data.csv', index_col=[0])
    passengers = pd.read_csv('passenger.csv', index_col=[0])
    pickle_in = open("model.pickle", "rb")
    model = pickle.load(pickle_in)
    pickle_in.close()


def remove_pk(data):
    new_data = data.loc[:, data.columns != 'PassengerId']
    return new_data


def make_prediction(data):
    global model
    global test_data
    #global passengers

    search_data = test_data[test_data['PassengerId'].isin(data)]
    #search_data = test_data.iloc[indexes_to_search]
    search_pred = (model.predict(remove_pk(search_data)))
    return search_pred.tolist()


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
