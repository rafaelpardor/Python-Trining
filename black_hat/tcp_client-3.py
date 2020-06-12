#!/usr/bin/python3

import socket

target_host = "www.google.com"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

st = "GET / HTTP/1.1\n Host:google.com \n\n"
byt=st.encode()
client.send(byt)

response = client.recv(4096)

print(response)
