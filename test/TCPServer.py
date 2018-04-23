# -*- coding: UTF-8 -*-
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
'''服务器聆听来自客户的TCP连接，参数定义了最大请求连接数（至少为1)'''
serverSocket.listen(1)
print 'The server is ready to receive'
while 1:
    '''客户敲门时，程序为serverSocket调用accept(),在服务器创建了一个称为connectionSocket的新套接字'''
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
