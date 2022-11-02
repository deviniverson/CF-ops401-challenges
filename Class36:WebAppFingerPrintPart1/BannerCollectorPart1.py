#!/usr/bin/env python3

# File Name: BannerCollectorPart1.py
# Author: Devin Iverson
# Date: 10/31/2022
# Purpose: 

import os

def netcat(address, port):
    os.system("nc " + address + " " + port)

def telnet(address, port):
    os.system("telnet " + address + " " + port)

def nmap(address, port):
    os.system("nmap " + address + " " + port)

def whatweb(address):
    os.system("whatweb " + "http://" + address)

def curl(address):
    os.system("curl -s -I " + address)

def target_address():
    target = input("Enter target URL or IP address: ")
    return str(target)

def target_port():
    port = input("Enter target port: ")
    return str(port)

def main():
    address = target_address()
    port = target_port()
    print("")
    netcat(address, port)
    print("")
    telnet(address, port)
    print("")
    nmap(address, port)
    print("")
    whatweb(address)
    print("")
    curl(address)

main()

 