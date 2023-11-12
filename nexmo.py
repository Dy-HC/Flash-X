from colorama import Fore, Style
import os, vonage
bl = Fore.BLACK
wh = Fore.WHITE
yl = Fore.YELLOW
red = Fore.RED
res = Style.RESET_ALL
gr = Fore.GREEN
ble = Fore.BLUE

def screen_clear():
    _ = os.system('cls')

screen_clear()
print(f'''
{red}
  ███████╗██╗░░░░░░█████╗░░██████╗██╗░░██╗  ██╗░░██╗
  ██╔════╝██║░░░░░██╔══██╗██╔════╝██║░░██║  ╚██╗██╔╝
  █████╗░░██║░░░░░███████║╚█████╗░███████║  ░╚███╔╝░
  ██╔══╝░░██║░░░░░██╔══██║░╚═══██╗██╔══██║  ░██╔██╗░
  ██║░░░░░███████╗██║░░██║██████╔╝██║░░██║  ██╔╝╚██╗
  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝  ╚═╝░░╚═╝
''')
link = input(f"\n{gr}Input Your Nexmo List :")
with open(link) as fp:
    for star in fp:
        try:
            check = star.rstrip()
            ch = check.split('\n')[0].split('|')
            Key = ch[0]
            Sec = ch[1]
            client = vonage.Client(key=Key, secret=Sec)
            result = client.get_balance()
            print(f"{yl} {Key}|{Sec} {gr} Working API!{ble} Balance : {result['value']:0.2f} EUR{res}")
            open("Result/Valid_Api.txt", "a").write(f"{Key}|{Sec} Balance: {result['value']:0.2f} EUR\n")
        except:
            print(f"{yl} {Key}|{Sec}  {red}DEAD API!{res}\n")
            pass
