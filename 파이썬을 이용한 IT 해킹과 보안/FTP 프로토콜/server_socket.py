import socket

with socket.socket() as s:
    addr = ("0.0.0.0", 80) # 80번으로 개통
    s.bind(addr)
    s.listen() 
    print("start server..")

    # conn -> 새로운 접속이 들어올 때마다 새로운 소켓 생성 (1:1 통신)
    conn, addr = s.accept() # 전화 수락
    print("accept {}:{}" .format(addr[0], addr[1]))
    data = conn.recv(1024)
    conn.send("Hi This is Web" .encode())
