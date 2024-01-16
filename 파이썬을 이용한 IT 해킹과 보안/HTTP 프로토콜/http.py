import requests

host = "http://www.virustotal.com"

res = requests.get(host)
print(res)

print(res.url)
print(res.status_code) # 응답 상태
res.raise_for_status # 오류 확인
res.content # 본문에 대한 내용 쭉 전달 ( = res.text)

my_params = {'id':'gasbugs', 'pass':'password'} # 딕셔너리 형식으로 변경
requests.get(host, params = my_params)

import json
my_data = json.dumps({'id':'gasbugs', 'pass':'password'})
print(my_data)
response = requests.get(host, data = my_data)
print(response)