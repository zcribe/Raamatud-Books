from socket import *
serverName = "127.0.0.1"
serverPort = 12000
# Create client socket. AF_INET = ipv4. SOCK_DGRAM = UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("Input lowercase sentence:")
# Encode message into bytes and send to specific target location
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()