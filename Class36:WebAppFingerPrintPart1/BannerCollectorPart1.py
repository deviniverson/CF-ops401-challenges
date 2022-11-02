#!/usr/bin/env python3

# File Name: BannerCollectorPart1.py
# Author: Devin Iverson
# Date: 10/31/2022
# Purpose: 

import subprocess

#netcat
def netcat(address, port):
    mode = subprocess.Popen(["nc " + address + " " + port], shell=True)
    mode.terminate()

#telnet 
def telnet(address, port):
    mode = subprocess.Popen(["telnet " + address + " " + port], shell=True)
    mode.terminate()

#nmap
def nmap(address, port):
    mode = subprocess.Popen(["nmap " + address + " " + port], shell=True)
    mode.terminate()

#whatweb
def whatweb(address):
    mode = subprocess.Popen(["whatweb " + "http://" + address], shell=True)
    mode.terminate()

#cURL
def curl(address):
    mode = subprocess.Popen(["curl -s -I " + address], shell=True)
    mode.terminate()

#Prompt user to enter URL or IP address
def target_address():
    target = input("Enter target URL or IP address: ")
    return str(target)

#Prompt user to enter port
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
