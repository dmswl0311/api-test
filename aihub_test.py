
#-*- coding:utf-8 -*-
import urllib3
import json

# 언어 분석 기술 문어/구어 중 한가지만 선택해 사용
# 언어 분석 기술(구어)
openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU_spoken"

accessKey = "7f4cd7c9-f504-47b0-b9d8-66a30176c5df"
analysisCode = "ner"

#  // 언어 분석 기술(구어)
text = "네 안녕하세요 홍길동 교숩니다"

requestJson = {
    "access_key": accessKey,
    "argument": {
        "text": text,
        "analysis_code": analysisCode
    }
}

http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)

# print("[responseCode] " + str(response.status))
# print("[responBody]")
print(str(response.data,"utf-8"))