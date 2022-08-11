#!/usr/bin/env python3

# File Name: ScapyScanner.py
# Author: Devin Iverson
# Date: 08/08/22
# Purpose: Encrypt and decrypt messages and files

import pyfiglet
from rich.console import Console
from tqdm import tqdm
import time
from scapy.all import TCP, IP, ICMP
from scapy.sendrecv import sr, sr1
import random

con = Console()
port_list = []

# Hacker tool banner with fake loading bar for dramatic pause
def script_banner():
    banner = pyfiglet.figlet_format("Scapy Scanner",font="banner3-D",justify="center")
    con.print(banner, "A TCP Port Scanner used by all Green Hat Hackers",style="bold green")
    for i in tqdm(range(100)):
        time.sleep(0.2)

# Define target ip address
def ip():
    while True:
            target = input("Enter Host IP address: (input in IPv4 format '***.***.***.***') ")
            return target
        
# Define TCP port range
def port_range():
   while True:
        selection = input("Enter 'range' to target a set of specific ports or ",
        "enter 'common' for ports [22,23,80,443,3389] or ",
        "enter 'all' for all 65534 target ports)")
        if selection == 'common':
            port_list = [22, 23, 80, 443, 3389]
            return port_list
        elif selection == 'all':
            all_ports = range(65534)
            return all_ports
        elif selection == 'range':
            port_list = []
            while True:
                port = input("Enter one port number: (submit one number at a time, enter 'done' when all numbers have been submitted)")
                #Removes spaces from input
                port.replace(" ", "")
                if port == 'done':
                    print(port_list)
                    return port_list
                try:
                    # Convert input into integer, appends to port_list else reprompts user for input.
                    val = int(port)
                    port_list.append(val)
                except ValueError:
                    print("Input was not a valid port number, try again")
        else:
            print("Value entered is invalid, try again")

# Send SYN from random source port for each target port
def send_SYN(ip, port_range):
    for target_port in port_range:
        source_port = random.randint(1035, 65534)
        response = sr1(IP(dst = ip)/TCP(sport = source_port, dport = target_port, flags = "S"), timeout = 1, verbose = 0)

        if (response.haslayer(TCP)):
            if(response.getlayer(TCP).flags == 0x12):
                # Send RST to close connection
                send_rst = sr(IP(dst = ip)/TCP(sport = source_port, dport = target_port, flags = "R"),timeout = 1, verbose = 0)
                print(f"{ip}:{target_port} is open")

            elif (response.getlayer(TCP).flags == 0x14):
                print(f"{ip}:{target_port} is closed")

        elif (response.haslayer(ICMP)):
            if(int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                print(f"{ip}:{target_port} is filtered and dropped")

        elif response is None:
            print(f"{ip}:{target_port}is filtered and dropped")

# main function
def main():
    script_banner()
    targetIP = ip()
    port_list = port_range()
    send_SYN(targetIP, port_list)
