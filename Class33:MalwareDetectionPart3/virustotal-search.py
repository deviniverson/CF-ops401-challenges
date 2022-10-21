#!/usr/bin/env python

"""
Copyright (C) 21 Feb 20: Eduard Marian

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    https://EduardMarian.xyz
    eduard_marian@protonmail.com
    Use at your own risk
"""

import requests, argparse, os, time

# ERROR PROOF FUNCTION TO SEE IF API IS A 64 ALPHANUMERIC CODE
def checkkey(ckey):
	try:
		if len(ckey) == 64:
			return ckey
		else:
			print("Your VirusTotal API must have 64 Alpha Numeric characters.")
			exit()

	except Exception as Error:
			print(Error)

# ERROR PROOF FUNCTION TO SEE IF HASH PARAMETER IS MD5 SHA1 or SHA256
def checkhash(chash):
	try:
		if len(chash) == 32:
			return chash
		elif len(chash) == 40:
			return chash
		elif len(chash) == 64:
			return chash
		else:
			print ("Your HASH must have 32, 40 or 64 Alpha Numeric characters.")
			exit()

	except Exception as Error:
			print(Error)

# ERROR PROOF FUNCTION TO SEE IF INPUT FILE EXISTS	
def checkfile(cfile):
	try:
		if os.path.isfile(cfile):
			return cfile
		else:
			print ("File %s is missing in your script directory." % (cfile))
			exit()
	except Exception as Error:
			print(Error)

# REQUEST FUNCTION
def VT_Request(key, hash, output):
	parameters = {"apikey": key, "resource": hash}
	url = requests.get("https://www.virustotal.com/vtapi/v2/file/report", params=parameters)
	json_response = url.json()
	response = int(json_response.get("response_code"))
	
	# DOES THE HASH EXISTS IN VT DATABASE?
	if response == 0:
		print(hash + ": UNKNOWN")
		file = open(output,"a")
		file.write(hash + " 0")
		file.write("\n")
		file.close()

	# DOES THE HASH EXISTS IN VT DATABASE?
	elif response == 1:
		positives = int(json_response.get("positives"))
		if positives >= 3:
			print(hash + ": MALICIOUS")
			file = open(output,"a")
			file.write(hash + " " + str(positives))
			file.write("\n")
			file.close()
		else:
			print(hash + ": NOT MALICIOUS")
			file = open(output,"a")
			file.write(hash + " 0")
			file.write("\n")
			file.close()
	else:
		print(hash + ": CAN NOT BE SEARCHED")

def Main():
	parser = argparse.ArgumentParser(description="Search VirusTotal reports with search terms (MD5, SHA1, SHA256) for single hash or multiple hash array found in the argument file.")
	parser.add_argument("-i", "--input", type=checkfile, required=False, help="Input File Location (EX: /Path/To/input.txt)")
	parser.add_argument("-o", "--output", required=False, help="Output File Location (EX: /Path/To/output.txt)")
	parser.add_argument("-m", "--md5", type=checkhash, required=False, help="Single Hash (EX: D41D8CD98F00B204E9800998ECF8427E)")
	parser.add_argument("-k", "--key", type=checkkey, required=True, help="Virus Total API Key (EX: 0FC73BF7E721EDF60E58C65F50D287A6DC1EEA81C281CC796810C08ED49DF67D)")
	parser.add_argument("-p", "--premium", action="store_const", const=1, required=False, help="Changes the 16s query delay to 1s. Made for better APIs.")
	args = parser.parse_args()

	localTime = time.localtime()
	output = "virustotal-search-%04d%02d%02d-%02d%02d%02d.txt" % localTime[0:6]

	# SINGLE HASH FUNCTION
	if args.md5 and args.key:
		file = open((args.output or output),"w+")
		file.close()
		VT_Request(args.key, args.md5.rstrip(), (args.output or output))

	# MULTI LIST HASH FUNCTION
	elif args.input and args.key:
		file = open((args.output or output),"w+")
		file.close()
		with open(args.input) as o:
			for line in o.readlines():
				VT_Request(args.key, line.rstrip(), (args.output or output))
				if args.premium == 1:
					time.sleep(1)
				else:
					time.sleep(16)
	

if __name__ == "__main__":
	Main()
