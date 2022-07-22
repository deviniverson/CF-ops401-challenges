#!/usr/bin/env python3

# File Name: UptimeSensorEmailer.py
# Author: Devin Iverson
# Date: 07/09/2022
# Purpose: Transmit single ICMP (ping) packet at a time to a specific IP, evaluates response as success or failure. Append result to Eventlogs.txt. Send email to administrator when response variable changes.

import datetime
from icmplib import ping
import smtplib
import ssl
from email.message import EmailMessage

ip = "8.8.8.8"
#ping_attempts = input("How many ICMP attempts: ")
# function to collect date and time 
def Timestamp():
    now = datetime.datetime.now()
    return now

# function to define status variable
def Status(response):
    if response == True:
        return "Active"
    else :
        return "Inactive"

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
time = Timestamp()
def status_change(time, ip):
    #do something

#emailer
email_sender = 'cake.is.a.lie404@gmail.com'
email_password = 'qwkxwovnywebuqfk'
email_receiver = 'deviniverson@duck.com'

subject = 'Seattle-ops401n2:OpsChallenge#3'
body = "{0}, On {1} Network changed to {2} \n".format(time, ip, network)


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


# Main
#ip = input("Enter target IP address: ")
#PacketSender(ip)

