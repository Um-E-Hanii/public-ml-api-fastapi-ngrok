import json 
import requests 

url = 'https://dancing-yapping-crucial.ngrok-free.dev/insurance_prediction'


input_data_for_model = { 
    'age' : 20,
    'sex' : 0,
    'bmi' : 67.77,
    'children' : 2,
    'smoker' : 0,
    'region' : 2
    }

input_json = json.dumps(input_data_for_model)
response = requests.post(url, json=input_data_for_model)
print(response.text) 

