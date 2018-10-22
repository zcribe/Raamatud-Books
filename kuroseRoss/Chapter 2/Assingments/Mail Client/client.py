#!/usr/bin/env python3

import base64
from socket import socket, AF_INET, SOCK_STREAM
import ssl


class Main:
    def __init__(self):
        self.port = 587
        self.mail_server = "mail.gmx.com"
        self.buffer = 1024
        self.socket = None
        self.user_password = base64.b64encode(b"\0USERNAME\0PASSWORD") + "\r\n".encode()

    def run(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.settimeout(10)
        self.start_connection()
        self.helo()
        self.tls_wrap()
        self.helo()
        self.authenticate()
        self.send_mail()
        self.socket.close()

    def helo(self):
        self.socket.send("EHLO Alice \r\n".encode())
        print(self.socket.recv(self.buffer))

    def tls_wrap(self):
        self.socket.send("STARTTLS\r\n".encode())
        print(self.socket.recv(self.buffer))
        self.socket = ssl.wrap_socket(self.socket)

    def start_connection(self):
        self.socket.connect((self.mail_server, self.port))
        print(self.socket.recv(self.buffer))

    def authenticate(self):
        self.socket.send("AUTH PLAIN\r\n".encode())
        print(self.socket.recv(self.buffer))
        self.socket.send(self.user_password)
        print(self.socket.recv(self.buffer))

    def send_mail(self):
        self.socket.send("MAIL FROM:<megax1@gmx.com>\r\n".encode())
        self.socket.send("RCPT TO: <tafgwdzv@10mail.org>\r\n".encode())
        self.socket.send(("DATA" + '\r\n').encode())
        self.socket.send(("Subject: Test!" + '\r\n').encode())
        self.socket.send("TEST".encode())
        self.socket.send("\r\n.\r\n".encode())
        print(self.socket.recv(self.buffer))
        self.socket.send(("QUIT" + '\r\n').encode())


if __name__ == "__main__":
    Main().run()
