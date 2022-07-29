#!/usr/bin/env python3

# File Name: FileEncrypterPart3.py
# Author: Devin Iverson
# Date: 07/21/2022
# Purpose: Encrypt and decrypt messages and files
import os
from cryptography.fernet import Fernet
from pathlib import Path
import random
from tkinter import *
import sys
import time

# menu 
def menu():
    print("* MAIN MENU *\n")
    print("-------------\n")
    print("Mode 1. Encrypt a File\n")
    print("Mode 2. Decrypt a File\n")
    print("Mode 3. Encrypt a Message\n")
    print("Mode 4. Decrypt a Message\n")
    print("Mode 5. Encrypt all Files in a Folder\n")
    print("Mode 6. Decrypt all Files in a Folder\n")
    print("Mode 7. Ransomware Simulation\n")
    print("Mode 8. QUIT\n")
    print("-------------\n")
    menu_input = input("Enter Mode #: ")
    return menu_input

#depending on the users input, this will guide them 
def traffic_signal(menu_input):
    if menu_input == "1" or menu_input == "2":
        filepath = input("Provide FilePath to Target File: ")
        # confirm if filepath exists
        if PathCheck(filepath) == True:
            if menu_input == "1":
                load_key()
                key = load_key()
                file_encrypter(filepath, key)
            else:
                key = load_key()
                file_decrypter(filepath, key)
        else:
            print("Path does not exist. Please try again.")
    #Encrypt message, print to screen when done    
    elif menu_input == "3":
        string = input("Provide cleartext string to Encrypt: ").encode()
        load_key()
        string_key = load_key()
        message = message_encryter(string, string_key)
        print(message)
    #Decrypt message, print to screen when done
    elif menu_input == "4":
        string = input("Provide cleartext string to Decrypt: ").encode()
        string_key = load_key()
        message = message_decrypter(string, string_key)
        print(message)
    #Encrypt all files in a folder
    elif menu_input == '5':
        string = input("Provide Folder Name to Encrypt: ")
        load_key()
        string_key = load_key()
        folder_encrypter(string, string_key)
        #complete this part

    #Decrypt all files in a folder
    elif menu_input == '6':
        string = input("Provide Folder Name to Decrypt: ")
        load_key()
        string_key = load_key()
        folder_decrypter(string, string_key)

    #Malware Simulator
    elif menu_input == '7':
        malware_sim()
    
    #Exit script
    elif menu_input == "8":
        exit()
    #Number doesn't match menu
    else:
        print("Mode not available at this time, please try again.")

#function to check for a valid path
def PathCheck(file_path):
    path_string = os.path.abspath(file_path)
    path = Path(path_string)
    return path.exists()

#function to create and save encryption key if file is empty
def KeyGen():
    key = Fernet.generate_key()
    string_key = str(key)
    with open("key.key", "wb") as key_file:
        key_file.write(string_key)
    
#function to load key
def load_key():
    keyFile ="key.key"
    if Path(keyFile).exists():
        return open(keyFile, "rb").read()
    else:
        KeyGen()

#encrypt message
def message_encryter(message, key):
    #encoded_message = message.encode()
    fkey = Fernet(key)
    encryped_message = fkey.encrypt(message)
    return str(encryped_message)

#encrypt file
def file_encrypter(filename, key):
    fkey = Fernet(key)
    with open(filename, "rb") as f:
        file_data = f.read()
    #encrypt data
    encrypted_data = fkey.encrypt(file_data)
    #write encrypted data in original file
    with open(filename, "wb") as f:
        f.write(encrypted_data)

#decrypt message
def message_decrypter(encrypted, key):
    fkey = Fernet(key)
    message = fkey.decrypt(encrypted)
    return str(message)

#decrypt file
def file_decrypter(filename, key):
    fkey = Fernet(key)
    with open(filename, "rb") as f:
        encrypted_data = f.read()
    #decrypt data
    decrypted_data = fkey.decrypt(encrypted_data)
    #write decrypted data in original file
    with open(filename, "wb") as f:
        f.write(decrypted_data)

#encrypt all files of folder, use os.walk to recursivly complete this
def folder_encrypter(filename, key):
    fkey = Fernet(key)
    for root, dirs, files in os.walk("."):
        print(files)
        for filename in files:
            filepath = Path.join(root, files)
            #open and read file
            with open(filepath, 'rb') as f:
                data = f.read()
            #open and encrypt file
            with open(filepath, 'w') as f:
                print(len(data))
                f.write(fkey.encrypt(data).encode())
                print('Done!')
                
#decrypt all files of folder
def folder_decrypter(folder, key):
    fkey = Fernet(key)
    for root, dirs, files in os.walk("."):
        print(files)
        for filename in files:
            filepath = Path.join(root, files)
            #open and read file
            with open(filepath, 'rb') as f:
                data = f.read()
            #open and encrypt file
            with open(filepath, 'w') as f:
                print(len(data))
                f.write(fkey.decrypt(data).encode())
                print('Done!')

def color_change(virus):
    list1=["red", "blue", "pink", "yellow", "orange", "teal", "green"]
    virus.config(background=random.choice(list1))

#malware simulator
def malware_sim():
    root=Tk()
    root.geometry("700x250")
    virus=Label(root,text="WARNING! Hacker Detected!", font=("times",50,"bold"))
    virus.grid(row=2, column=0, pady=20, padx=20)
    color_change(virus)

# main function
def main():
    for i in range(5):
        input_num = menu()
        traffic_signal(input_num)
    
main()