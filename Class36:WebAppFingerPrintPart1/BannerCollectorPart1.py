#!/usr/bin/env python3

# File Name: BannerCollectorPart1.py
# Author: Devin Iverson
# Date: 10/31/2022
# Purpose: 

import os
import time

def netcat(address, port):
    mode = os.system("nc " + address + " " + port)
    time.sleep(5)
    mode.terminate()


def telnet(address, port):
    mode = os.system("telnet " + address + " " + port)
    time.sleep(5)
    mode.terminate()

def nmap(address, port):
    mode = os.system("nmap " + address + " " + port)
    time.sleep(5)
    mode.terminate()

def whatweb(address):
    mode = os.system("whatweb " + "http://" + address)
    time.sleep(5)
    mode.terminate()

def curl(address):
    mode = os.system("curl -s -I " + address)
    time.sleep(5)
    mode.terminate()

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

 