import socket

s = socket.socket()
s.connect(("172.30.1.60", 21))

data = s.recv(1024).decode()

s.send("USER anonymous" .encode) # 로그인
data = s.recv(1024).decode()
print(data)

s.send("PASS anonymous" .encode) # 로그인
data = s.recv(1024).decode()
print(data)

s.send("PWD" .encode) # 데이터가 어디 있는지 위치 확인
data = s.recv(1024).decode()
print(data)

s.send("PORT 127,30,1,1,25,25" .encode()) # 25 * 255 + 25 -> 포트 설정 필요
data = s.recv(1024).decode()
print(data)

s.send("LIST" .encode) # 리스트 데이터 출력
data = s.recv(1024).decode()
print(data)