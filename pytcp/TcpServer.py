import time
from socket import *

import lighton

lighton.setUP()

ctrCmd = ['UP', 'DOWN', 'VIEW']
message = "hello world"
HOST = '192.168.43.96'
PORT = 5555

BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    tcpCliSock, addr = tcpSerSock.accept()

    time.sleep(.05)
    data = ''
    data = tcpCliSock.recv(BUFSIZE).decode()

    print(data)

    if not data:
        print("there is no data")
        break

    if data == ctrCmd[0]:
        lighton.ledOn()

    if data == ctrCmd[1]:
        lighton.ledOff()

    if data == ctrCmd[2]:
        lighton.ledOn()
        # here I want to send String back to Android

tcpCliSock.close();
