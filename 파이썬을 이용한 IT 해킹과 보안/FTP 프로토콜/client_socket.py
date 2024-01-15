import socket

# s = socket.socket() -> 소켓을 잘 닫지 않는다면 불필요한 데이터들로 가득 채울 수 있는 코드가 될 수 있음
with socket.socket() as s:
    addr = ("www.daum.net", 80) # 443 web
    s.connect(addr) # 통신 시작
    s.send("GET /\n" .encode()) # 데이터 보내기 : 웹 요청 (문자를 인코딩)
    data = s.recv(1024) # 1024바이트 데이터 받기
    print(data.decode()) # 인코딩된 문자를 돌려놓기

