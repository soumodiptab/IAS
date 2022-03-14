import requests,json
def model_call(api_name,**kwargs):
    response = requests.post('http://localhost:8000//predict', json=json(kwargs)).json()
    return response