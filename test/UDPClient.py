# -*- coding: UTF-8 -*-
from socket import *
serverName='127.0.0.1'
serverPort=12000
'''创建客户的套接字,AF_INET指示了地址蔟，表示底层网络使用了ipv4
SOCK_DGRAM代表是一个UDP套接字'''
clientSocket=socket(AF_INET,SOCK_DGRAM)
message=raw_input('input lowercase sentence:')
clientSocket.sendto(message,(serverName,serverPort))
'''当一个来自因特网的分组到达该客户套接字时，该分组的数据被放置到变量modifiedMessage中
源地址被放置到变量serverAddress中，2048缓存长度'''
modifiedMessage,serverAddress=clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()

