#!/bin/python
# coded by safazz
# https://github.com/safazz

try:
    import requests,sys,os,time,getpass,json,colorama
    from time import sleep
    from sys import exit
    from os import system
    from colorama import init, Fore, Back
except ImportError:
    exit("[!] please install 'requests', 'colorama'")

B = Fore.BLUE
W = Fore.WHITE
C = Fore.CYAN
M = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW

def load():
    load = [
     '','.','..','...','....']
    for o in load:
        print W+"\r["+Y+"+"+W+"] Loading"+G+""+o,
        sys.stdout.flush()
        sleep(1)

def login():
   try:
        os.system("clear;python3 banner.py")
        print(W+"[*] please login to facebook account")
        email = raw_input(W+"["+Y+"+"+W+"] "+W+"email"+M+": "+G)
        passw = getpass.getpass(W+"["+Y+"+"+W+"] "+W+"password"+M+": ")
        load()
        url = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+email+'&locale=en_US&password='+passw+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
        log = url.content
        asu = json.loads(log)
        if "session_key" in log:
            print W+"\n["+G+"+"+W+"] Your token"+M+": "+G+""+asu['access_token']
            print W+"["+G+"*"+W+"] "+W+"Token seved"+M+": "+G+"token.txt"
            open('token.txt','a').write(asu['access_token'])
        else:
            print W+"\n["+M+"!"+W+"] Login invalid please check email/password"
            exit()
   except KeyboardInterrupt:
        exit(M+"[!] "+W+"Exit : OK")

login()
