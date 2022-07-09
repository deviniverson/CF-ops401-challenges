#!/usr/bin/env python3

# File Name: UptimeSensorEmailer.py
# Author: Devin Iverson
# Date: 07/09/2022
# Purpose: Transmit single ICMP (ping) packet at a time to a specific IP, evaluates response as success or failure. Append result to Eventlogs.txt. Send email to administrator when response variable changes.

import datetime
from icmplib import ping

ip = "8.8.8.8"
#ping_attempts = input("How many ICMP attempts: ")
# function to collect date and time 
def Timestamp():
    now = datetime.datetime.now()
    return now

# function to define status variable
def Status(response):
    if response == True:
        return "Network Active"
    else :
        return "Network Inactive"

# function to send ICMP (ping) packet to target IP address
def PacketSender(ip):
    f = open("EventLogs.txt", "a")
    for i in range(10):
        host = ping(ip, count=1, interval=0.02, timeout=2)
        network = Status(host.is_alive)
        time = Timestamp()
        event = "{0}, {1} to {2} \n".format(time, network, ip)
        f.write(event)
    f.close()

# dictionary to show what the current status variable for each ip address  


# emailer


# Main
#ip = input("Enter target IP address: ")
PacketSender(ip)

