#-*- coding:utf-8 -*-
import urllib3
import json
import base64
import json
import os

openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
accessKey = "198b2f86-c3a3-409c-b524-3f065eb25dd7"
audioFilePath = "./hobby_00000001.wav"
languageCode = "korean"

fn = 'hobby_00000001'
file_name = os.path.join(os.path.dirname(__file__), 'aihub_data', 'hobby_01', '001', fn + '.wav')
 
file = open(file_name, "rb")
file = open(file_name, "rb")
audioContents = base64.b64encode(file.read()).decode("utf8")
file.close()
 
requestJson = {
    "access_key": accessKey,
    "argument": {
        "language_code": languageCode,
        "audio": audioContents
    }
}
 
http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)
 
print("[responseCode] " + str(response.status))
print("[responBody]")
print("===== 결과 확인 ====")
data = json.loads(response.data.decode("utf-8", errors='ignore'))    
print(data['return_object']['recognized'])