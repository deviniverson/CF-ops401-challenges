#!/usr/bin/env python3

# File Name: FileEncrypter.py
# Author: Devin Iverson
# Date: 07/21/2022
# Purpose: 
import os
from cryptography.fernet import Fernet


# menu 
def menu():
    print("* MAIN MENU *\n")
    print("-------------\n")
    print("Mode 1. Encrypt a File\n")
    print("Mode 2. Decrypt a File\n")
    print("Mode 3. Encrypt a Message\n")
    print("Mode 4. Decrypt a Message\n")
    #print("Mode 5. Encrypt all Files in a Folder\n")
    #print("Mode 6. Decrypt all Files in a Folder\n")
    #print("Mode 7. Ransomware Simulation\n")
    print("Mode 8. QUIT\n")
    print("-------------\n")
    menu_input = input("Enter Mode #: ")
    return menu_input

#depending on the users input, this will guide them 
def traffic_signal(menu_input):
    if menu_input == "1" or "2":
        filepath = input("Provide FilePath to Target File: ")
        # confirm if filepath exists
        if PathCheck(filepath) == True:
            if menu_input == "1":
                key = KeyGen()
                file_encrypter(filepath, key)
            else:
                key = load_key()
                file_decrypter(filepath, key)
        else:
            print("Path does not exist. Please try again.")
    #Encrypt message, print to screen when done    
    elif menu_input == "3":
        string = input("Provide cleartext string to Encrypt: ").encode()
        string_key = KeyGen()
        message = message_encryter(string, string_key)
        print(message)
    #Decrypt message, print to screen when done
    elif menu_input == "4":
        string = input("Provide cleartext string to Decrypt: ").encode()
        string_key = load_key()
        message = message_decrypter(string, string_key)
        print(message)
    #Exit script
    elif menu_input == 8:
        exit
    
    #Number doesn't match menu
    else:
        print("Mode not available at this time, please try again.")

#function to check for a valid path
def PathCheck(file_path):
    exists = os.path.exists(file_path)
    return exists

#function to create and save encryption key
def KeyGen():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

#function to load key
def load_key():
    return open("key.key", "rb").read()


#encrypt message
def message_encryter(message, key):
    encoded_message = message.encode()
    f = Fernet(key)
    encryped_message = f.encrypt(encoded_message)

#encrypt file
def file_encrypter(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)

#decrypt message
def message_decrypter(encrypted, key):
    f = Fernet(key)
    message = f.decrypt(encrypted)
    return message

#decrypt file
def file_decrypter(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    #decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    #write decrypted data in original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)

# main function
i = 0

for i in range(3):
    input_num = menu()
    traffic_signal(input_num)
    

