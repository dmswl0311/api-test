import requests
import json
import base64
import cv2

url="http://aiopen.etri.re.kr:8000/ObjectDetect"
key=""
image_path='./img/stand.jpg'
image=cv2.imread(image_path,cv2.IMREAD_UNCHANGED)
type='jpg'
file = open(image_path, "rb")
imageContents = base64.b64encode(file.read()).decode("utf8")
file.close()

json_data={
		"access_key": key,
		"argument": {
			"file": imageContents,
			"type": type
		}
}

response=requests.post(url,headers={"Content-Type": "application/json; charset=UTF-8"},json=json_data)
response_data=response.json()
for i in range(0,len(response_data["return_object"]["data"])):
    if response_data["return_object"]["data"][i]["class"]=="person":
        now_x=int(response_data["return_object"]["data"][i]["x"])
        now_y=int(response_data["return_object"]["data"][i]["y"])
        width=int(response_data["return_object"]["data"][i]["width"])
        height=int(response_data["return_object"]["data"][i]["height"])
        cv2.rectangle(image,(now_x,now_y),(now_x+width,now_y+height),(255,255,255),4)
        image_crop=image[now_y:now_y+height,now_x:now_x+width]
        cv2.putText(image,"Person",(now_x+width-20,now_y+height-20),cv2.FONT_HERSHEY_SIMPLEX ,1,(255,255,255))
        cv2.imshow("image_crop",image_crop)
        cv2.imwrite('./img/crop.jpg',image_crop)
        cv2.waitKey(0)
    else:
        continue