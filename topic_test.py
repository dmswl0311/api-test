import requests

url='http://svc.saltlux.ai:31781'
headers={'Content-Type': 'application/json;'}
json_data={
    "key": "16eade6d-5298-4cdc-878c-3a23ee1d2479",
    "serviceId": "11951939767",
    "argument": {
        "category": "it",
        "count": "1"
    }
}
response=requests.post(url,json=json_data,headers=headers)
response_data = response.json()
print(response_data['document'][0]["content"])