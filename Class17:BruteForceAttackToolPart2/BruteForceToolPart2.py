#!/usr/bin/env python3

# File Name: BruteForceWordlistTool.py
# Author: Devin Iverson
# Date: 08/23/2022
# Purpose: Custom tool that performs brute force attacks

import pyfiglet
from rich.console import Console
from rich.table import Table
from tqdm import tqdm, trange
import time

con = Console()
# menu between two modes
def menu():
    con.print("* Main Menu *")
    con.print("-------------")
    con.print("Mode #1: Offensive Tool - Dictionary Iterator", style="red1")
    con.print("Mode #2: Defensive Tool - Password Recognized", style="blue")
    con.print("Mode #3: Defensive Tool - Password Complexity", style="blue")
    con.print("Mode #9: Exit Tool")
    con.print("-------------")
    
    menu_input = input("Enter Mode #: ")
    return menu_input

def traffic_signal(mode):
    if mode == '1':
        mode1()
    elif mode == '2':
        mode2()
    elif mode == '3':
        mode3()
    elif mode == '9':
        exit
    else:
        print("Mode is not available at this time, please try again.")
        return 0

# script banner with interesting loading bars
def script_banner():
    banner = pyfiglet.figlet_format("Brute Force",font="banner3-D",width=100,justify="center")
    con.print(banner, "A Brute Force Wordlist Tool used by all the cool hackers!",style="bold green1")
    for i in tqdm(range(1), desc='Root Privileges Acquired',colour='GREEN'):
        for j in trange((100), desc='Searching for Exploits',colour='WHITE'):
            time.sleep(0.05)  
        for k in trange((100), desc='Deploying Exploit',colour='RED'):
            time.sleep(0.1)
    print('\n')

# locate wordlist and access it
def wordlist_finder():
    txtfile = input("Enter path to wordlist: ")
    with open(txtfile) as f:
        lines = f.readlines()
    
    #remove new line characters
    word_list = [line.strip() for line in lines]
    f.close()
    return list(word_list)

# mode1: Offensive, Dictionary Iterator
def mode1():
    wordlist = wordlist_finder()
    for word in wordlist:
        print(word)

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

# main function
def main():
    script_banner()
    while True:
        mode = menu()
        if mode in '123':
            traffic_signal(mode)
        elif mode == '9':
            break
        else:
            con.print("Mode not available at this time, try again", style='red1')
            continue
main()

# test wordlist file path
# /Users/deviniverson/GitHub/CF-ops401-challenges/Class16:BruteForceAttackToolPart1/wordlist.txt