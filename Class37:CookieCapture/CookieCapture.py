#!/usr/bin/env python3

# File Name: CookieCapture.py
# Author: Devin Iverson
# Date: 11/03/2022
# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import requests
import webbrowser

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.
        ` ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ '    | o      |
         |                    \ - /  
        
        
        
        
        
        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Add here some code to make this script perform the following:
# - Send the cookie back to the site and receive a HTTP response
response = (requests.get(targetsite, cookies=cookie).text)
#print(response)
# - Generate a .html file to capture the contents of the HTTP response
f = open('webtext.html','w')
f.write(response)
f.close()

# - Open it with Firefox
webbrowser.open_new_tab('webtext.html')
#
# Stretch Goal
# - Give Cookie Monster hands