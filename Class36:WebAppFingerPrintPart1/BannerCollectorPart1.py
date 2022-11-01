#!/usr/bin/env python3

# File Name: BannerCollectorPart1.py
# Author: Devin Iverson
# Date: 10/31/2022
# Purpose: 
import socket

# Prompt for user to enter target URL or IP address
def target_address():
    target = string(input("Enter target URL or IP address: "))
    return target

# Prompt user to enter target port
def target_port():
    port = int(input("Enter target port: "))
    return port
# Netcat banner grabbing technique
def netcat(address, port):
    s = socket.socket()
    s.connect((address,port))
    

# telnet banner grabbing technique

# Nmap banner grabbing technique

# WHatWeb banner grabbing technique

# cURL banner grabbing technique

# Main function


