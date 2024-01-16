from base64 import b64encode
from threading import Thread
from colorama import *
from pystyle import *
import hashlib
import tls_client, json, os, ctypes, time, time, random, base64, threading, re, sys

System.Title("Reaction Tool | Made By Jimo")
axi = """
  _____                 _   _          _______          _ 
 |  __ \               | | (_)        |__   __|        | |
 | |__) |___  __ _  ___| |_ _  ___  _ __ | | ___   ___ | |    
 |  _  // _ \/ _` |/ __| __| |/ _ \| '_ \| |/ _ \ / _ \| |        
 | | \ \  __/ (_| | (__| |_| | (_) | | | | | (_) | (_) | |      
 |_|  \_\___|\__,_|\___|\__|_|\___/|_| |_|_|\___/ \___/|_|
                                                                                                                                                           
                   [+]Created By Jimo

                    › Press Enter...
"""
Anime.Fade(Center.Center(axi), Colors.rainbow, Colorate.Vertical, interval=0.020, enter=True)

os.system("cls" if os.name == "nt" else "clear")

__useragent__ = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9013 Chrome/108.0.5359.215 Electron/22.3.2 Safari/537.36" 
build_number = 198318  
cv = "108.0.5359.215"
__properties__ = b64encode(json.dumps({
  "os": "Windows",
  "browser": "Discord Client",
  "release_channel": "stable",
  "client_version": "1.0.9013",
  "os_version": "10.0.19045",
  "os_arch": "x64",
  "system_locale": "en-US",
  "client_build_number": build_number,
  "native_build_number": 32266,
  "client_version_string": "1.0.9013"
},separators=(',', ':')).encode()).decode()


def get_headers(token):
  headers = {
    "Authorization": token,
    "Accept-Encoding": "gzip, deflate",
    "Origin": "https://discord.com",
    "Accept": "*/*",
    "X-Discord-Locale": "en-US",
    "X-Super-Properties": __properties__,
    "User-Agent": __useragent__,
    "Referer": "https://discord.com/channels/@me",
    "X-Debug-Options": "bugReporterEnabled",
    "Content-Type": "application/json",
    "X-Discord-Timezone": "Asia/Calcutta",

  }
  return headers

reacted = 0 
def title():
    ctypes.windll.kernel32.SetConsoleTitleW("[Exploit Reactor] | Reacted: %s" % (reacted))

def add_reaction(tk, channel, message, emoji, emoji_name):
    while True:
      try:
        global reacted
        headers = get_headers(tk)
    
        client = tls_client.Session(client_identifier="chrome110")
        client.headers.update(headers)
        r2 = client.put(f"https://discord.com/api/v9/channels/{channel}/messages/{message}/reactions/{emoji}/%40me?location=Message&burst=false")
            
        if r2.status_code in (200, 201, 204):
                reacted += 1
                title()
                print(f"[+] Successfully reacted to message {message} in channel {channel} with emoji {emoji_name} with token {tk[:30]}")
                break
        else:
                print(f"[-] Failed to react ", r2.text)
                break
          
      except Exception as e:
          continue




def url_encode(string1):
    return string1.replace(":", "%3A").replace("/", "%2F").replace("<", "").replace(">", "")



emoji1 = input("[!] URL Emoji: ")
emoji = url_encode(emoji1)
try:
  emoji_name = emoji1.split(":")[0]
except:
  emoji_name = emoji1

channel = input("[!] ID Channel: ")
message = input("[!] ID Message: ")

amount = int(input("[!] Amount: "))
amount = amount + 1
f = open("tokens.txt", "r").readlines()

print("[!] Starting....")
time.sleep(3)
os.system("cls" if os.name == "nt" else "clear")
count = 0 
for token in f:
    token = token.strip()
    
    count += 1
    if count > amount:
        break
    time.sleep(0.1)
    Thread(target=add_reaction, args=(token, channel, message, emoji,emoji_name,)).start()


#╔═════════════════════════════════════════════════════╗
#║    || - ||        Code By Jimo            || - ||   ║
#╚═════════════════════════════════════════════════════╝

