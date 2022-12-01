#!/usr/bin/python3

# Name: Devin Iverson
# Date: 11/30/22

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 5
sockmod.settimeout(timeout)

hostip = input("Enter target IP address: ")
portno = int(input("Enter port number to check: "))

def portScanner(portno):
    try:
        result = sockmod.connect((hostip, portno))
        print(f"Port {portno} open")
    except Exception as exception:
        print(f"Port {portno} closed")
    finally:
        sockmod.close()
portScanner(portno)