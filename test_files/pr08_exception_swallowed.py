import requests

def call_api(endpoint):
    try:
        response = requests.get(endpoint)
        return response.json()
    except:
        pass