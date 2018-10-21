#!/usr/bin/env python3

import time
import argparse
from socket import socket, AF_INET, SOCK_DGRAM


class Main:
    def __init__(self):
        argument_parser = argparse.ArgumentParser()
        argument_parser.add_argument("-pings", "-pc", default=10, type=int,
                                     help="How many pings to send (default 10)")
        argument_parser.add_argument("-host", "-ho", default="localhost", type=str,
                                     help="Who to ping (default localhost)")
        argument_parser.add_argument("-port", "-p", default=12000, type=int,
                                     help="Port to use (default 2000)")
        argument_parser.add_argument("-buffer_size", "-bs", default=2048, type=int,
                                     help="How many bytes do you want to buffer? (default: 2048)")

        self.arguments = argument_parser.parse_args()
        self.socket = None
        self.message = "Pong me back!"
        self.results = []

    def run(self):
        while self.arguments.pings > 0:
            self.socket = socket(AF_INET, SOCK_DGRAM)
            self.ping()
            self.arguments.pings -= 1
            self.socket.close()
        print(self.results)

    def ping(self):
        start = time.time()
        self.socket.sendto(self.message.encode(), (self.arguments.host, self.arguments.port))
        response, other_host = self.socket.recvfrom(self.arguments.buffer_size)
        end = time.time()
        result = end - start
        self.results.append(result)
        if response:
            print("Response:", response.decode(), " (", result,  ")")
        else:
            print("Didn't get a Pong!")



if __name__ == "__main__":
    Main().run()