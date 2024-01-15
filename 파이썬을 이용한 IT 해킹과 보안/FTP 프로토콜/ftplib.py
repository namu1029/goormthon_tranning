from ftplib import FTP

ftp = FTP("172.30.1.23")
print('banner: ', ftp.getwelcome())
print('login:', ftp.login())
print(ftp.pwd()) # 현재 위치

print('List: ', ftp.retrlines('LIST')) # 리스트 받아오기 -> 어떤 포트를 통신 할 건지 명시 필요 X
print('RETR: ', ftp.retrbinary('RETR boanproject.txt', open('boan.txt', 'wb').write))
print('STOR: ', ftp.storbinary('STOR boanproject2.txt', open('boanproject2.txt', 'rb')))
