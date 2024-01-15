import socket

addr = ("0.0.0.0", 4444)

with socket.socket() as s :
    s.bind(addr)
    s.listen()
    print("Server is started...")

    conn, addr = s.accept()
    print("client = {}:{}" . format(addr[0], addr[1]))

    while(1):
        data = conn.recv(1024)
        if data.decode() == "quit": # decode 한게 quit와 같다면
            print("quit connection")
            exit() # 프로그램 종료
        conn.send(data)
        print(data.decode())