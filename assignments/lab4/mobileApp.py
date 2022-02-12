import requests
import pandas as pd
#data_test = pd.read_csv('passenger.csv')
#actual = pd.read_csv('gender_submission.csv')


def load_batch_data(file_name):
    print("Implementation uses pandas, Please specify column name >>")
    col_name = str(input())
    df = pd.read_csv(file_name)
    query = df[f'{col_name}'].tolist()
    return query


def request_prediction(query):
    jsondata = {'passenger_ids': query}
    response = requests.post(
        'http://localhost:8000//predict', json=jsondata).json()
    y_pred = response['prediction']
    return y_pred


def start():
    print('Specify single/Batch mode >>\n')
    print('1. Single - single passenger id input')
    print('2. Batch - Read from csv file [specify file-name]')
    opt = int(input())
    query = []
    if opt == 1:
        query.append(input('Enter valid passenger id >>'))
    else:
        file_name = str(input('Enter file-name\n'))
        query = load_batch_data(file_name)
    survive = request_prediction(query)
    df = pd.DataFrame(zip(query, survive), columns=['Passenger Id', 'Survive'])
    print(df.to_string())


if (__name__ == '__main__'):
    start()
