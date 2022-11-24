#!/usr/bin/python3

# Name: Devin Iverson
# Date: 11/21/22

import nmap

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) OS Detection \n""") 
print("You have selected option: ", resp)

# set range
rangeMin = str(input("Port Range start point: "))
rangeMax = str(input("Port Range end point: "))
total_range = rangeMin+'-'+rangeMax

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    scanner.scan(ip_addr, total_range, '-v -sU')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print("Protocols: ", scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print(scanner.scan(ip_addr, arguments="-O")['scan'][ip_addr]['osmatch'][1])
elif resp >= '4':
    print("Please enter a valid option")
