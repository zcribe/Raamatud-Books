from socket import *

server_name = "localhost"
server_port = 2080

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, SOCK_STREAM))

request = '''GET /robots.txt HTTP/1.1
HOST: localhost

'''

client_socket.send(request.encode('ascii'))

returned_sentence = client_socket.recv(1024)
print("From server:", returned_sentence.decode('ascii'))

client_socket.close()