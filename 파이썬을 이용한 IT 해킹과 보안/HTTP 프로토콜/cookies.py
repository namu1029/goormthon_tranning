import requests, json

host = "http://www.virustotal.com"

my_header = {'my_header':'value'}
my_cookies = {'session_id':'cookie!!'} 

res = requests.get(host, headers=my_header, cookies=my_cookies)
print(res)

# get 요청 + 파라미터 / post + data / header + cookie