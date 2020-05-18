#!/usr/bin/python

import socket

target_host = "0.0.0.0"
target_port = 9999

# create a socket object
# AD_INET is saying we are going to use a standar IPv4 address
# SOCK_STREAM indicate that this will be a TCP clint
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
#client.send("GET / HTTP/1.1\r\n Host:google.com \r\n\r\n")
client.send("ABCDEF")
# recive data
response = client.recv(1024)

print response

