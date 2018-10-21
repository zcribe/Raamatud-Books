#!/usr/bin/env python3

import os.path as path
from socket import socket, AF_INET, SOCK_STREAM


class Main:
    def __init__(self):
        self.port = 2080
        self.listening_socket = None
        self.unaccepted_connections = 1
        self.buffer_size = 1024

    def run(self):
        self.listening_socket = socket(AF_INET, SOCK_STREAM)
        self.listening_socket.bind(('', self.port))
        self.listening_socket.listen(self.unaccepted_connections)
        print("Listening for connections.")
        while True:
            connection_socket = self.create_connection()
            with connection_socket as connection:
                self.handle_request(connection)

    def set_port(self, port: int):
        self.port = port

    def set_unaccepted_connections(self, connections: int):
        self.unaccepted_connections = connections

    # create a connection socket when contacted by a client
    def create_connection(self):
        connection_socket, host = self.listening_socket.accept()
        print("Connected by:", host[0])
        return connection_socket

    # receive HTTP request
    # parse the request to determine the specific file being requested
    # get the requested file from server file system
    # send the request over TCP connection to the requesting browser. If the file not in server respond with 404
    def handle_request(self, connection):
        request = connection.recv(self.buffer_size).decode("ascii")
        response = self.generate_response(request)
        connection.send(response.encode("ascii"))

        print("Request received:", request.rstrip())
        print("Responded with:", response.rstrip())

    # create HTTP response message consisting of the requested file preceded by the header lines
    def generate_response(self, request):
        assert not isinstance(request, bytes)
        components = request.split()
        print(components)
        if not components:
            return "No request"
        if components[0] == "GET":
            if path.isfile(components[1]):
                with open(components[1]) as f:
                    return f.read()
            return "404 - Not Found"
        return "Only Accepts GET requests"


if __name__ == "__main__":
    Main().run()
