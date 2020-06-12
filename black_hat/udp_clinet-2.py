#!/usr/bin/python

import socket

target_host = "127.0.0.1"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("AAABBBCCC", (target_host, target_port))

# For best match with hardware and network realities,
# the value of bufsize should be a relatively small power of 2, for example, 4096.
data, addr = client.recvfrom(4096)

print data, addr
