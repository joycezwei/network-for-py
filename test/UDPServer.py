# -*- coding: UTF-8 -*-
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
'''将端口号12000与服务器的套接字绑定'''
serverSocket.bind(('',serverPort))
print "This server is ready to receive"
while True:
    message,clientAddress=serverSocket.recvfrom(2048)
    modifiedMessage=message.upper()
    serverSocket.sendto(modifiedMessage,clientAddress)
