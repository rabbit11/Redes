#biblioteca de socket em python
import socket

#definindo portas de entrada, ip e tamanho do buffer da comunicação
TCP_IP = '127.0.0.1'
TCP_PORT = 8080
BUFFER_SIZE = 1024

#mensagem a ser enviada
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)