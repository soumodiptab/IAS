from flask import Flask, request, jsonify
import json
import pickle
import pandas as pd
app = Flask(__name__)


def remove_pk(data):
    new_data = data.loc[:, data.columns != 'PassengerId']
    return new_data


def pre_process(dat):
    data = dat.copy(deep=True)
    data['Age'].fillna(data['Age'].mean(), inplace=True)
    data['Fare'].fillna(data['Fare'].mean(), inplace=True)
    data['Embarked'].fillna(data['Embarked'].bfill(), inplace=True)
    data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
    data['Embarked'] = data['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})
    test = data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
    return test


def load_ai_files():
    global test_data
    global model
    #global passengers
    #test_data = pd.read_csv('testing_data.csv', index_col=[0])
    #passengers = pd.read_csv('passenger.csv', index_col=[0])
    pickle_in = open("model.pickle", "rb")
    model = pickle.load(pickle_in)
    pickle_in.close()


def make_prediction(data):
    global model
    global test_data
    #global passengers
    #search_data = test_data[test_data['PassengerId'].isin(data)]
    #search_data = test_data.iloc[indexes_to_search]
    processed=pre_process(data)
    search_pred = model.predict(processed)
    return search_pred.tolist()


@app.route('/predict', methods=['POST'])
def service():
    info = request.get_json()
    #passengers = json.loads(info)
    data= pd.read_json(info,orient="table")
    values = make_prediction(data)
    return jsonify({'prediction': values})


if (__name__ == '__main__'):
    load_ai_files()
    app.run(port=8000, debug=True, use_debugger=False,
            use_reloader=False, passthrough_errors=True)
