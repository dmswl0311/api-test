import requests

print("문장을 입력하세요")
query=input()

url='http://svc.saltlux.ai:31781'
headers={'Content-Type': 'application/json;'}
json_data={
    "key": "16eade6d-5298-4cdc-878c-3a23ee1d2479",
    "serviceId": "01551822500",
    "argument": {
        "text": query
    }
}

response=requests.post(url,json=json_data,headers=headers)
response_data = response.json()
print(response_data["normalized_text"])