import requests
@app.route
def sensor_recieve(api_name,**kwargs):
    response = requests.get('http://localhost:8000//recieve', json=json(kwargs)).json()
    return response

def controller_recieve(index,**kwargs):
    