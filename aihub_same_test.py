import json
import requests

url='http://aiopen.etri.re.kr:8000/WiseWWN/Homonym'
key='7f4cd7c9-f504-47b0-b9d8-66a30176c5df'
word=input("단어를 입력하세요 ")

json_data={
	"access_key": key,
	"argument": {
		"word": word
	}
}

response=requests.post(url,headers={"Content-Type": "application/json; charset=UTF-8"},json=json_data)
response_data=response.json()
print("=============={0} 동음이의어===============".format(word))
for i in response_data["return_object"]["homonym"]:
    print(i["homonym_code"],i["description"])

# urllib3 사용====================================
# import urllib3
# http = urllib3.PoolManager()
# response = http.request(
#     "POST",
#     url,
#     headers={"Content-Type": "application/json; charset=UTF-8"},
#     body=json.dumps(json_data)
# )

# print("[responseCode]" + str(response.status))
# print("[responBody]")
# print(str(response.data,"utf-8"))