from socket import *

server_name = "127.0.0.1"
server_port = 12000

# Client socket creation. AF_INET = ipv4, SOCK_STREAM = TCP socket
client_socket = socket(AF_INET, SOCK_STREAM)
# Establish a connention with specific host and perform the TCP three way handshake
client_socket.connect((server_name, SOCK_STREAM))

sentence = input("Input a sentence")
# Encode into bytes and send. Since connection is established target location is not needed
client_socket.send(sentence.encode())
# Answer is accumalated until CR character (Carriage return)
returned_sentence = client_socket.recv(1024)
print("From server:", returned_sentence.decode())

client_socket.close()