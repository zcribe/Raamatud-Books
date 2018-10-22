#!/usr/bin/env python3

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


class ClientThread(Thread):
    def __init__(self, connection, ip, port):
        super().__init__()

    def run(self):
        pass


class Main:
    def __init__(self):
        self.ip = ""
        self.port = 2000
        self.buffer_size = 1024
        self.timeout = 10
        self.max_connections = 4
        self.socket = None

    def run(self):
        self.setup()

        while True:
            self.socket.listen(self.max_connections)
            print("Listening for connections.")
            connection, (ip, port) = self.socket.accept()
            client_thread = ClientThread(connection, ip, port)
            client_thread.start()

    def setup(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.settimeout(self.timeout)
        #self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.ip, self.port))


if __name__ == "__main__":
    Main().run()
