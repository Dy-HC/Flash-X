import os, time
from colorama import Fore, Style, Back
from concurrent.futures import ThreadPoolExecutor
start_time = time.time()
bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
bgr = Back.GREEN
def screen_clear():
  _ = os.system('cls')

def v3(star):
 host = ''
 port = ''
 user = ''
 pwd = ''
 if "URL:" in star:
    star = fp.readline()
 if "METHOD:" in star:
    star = fp.readline()
 if "MAILHOST:" in star:
    star = star.replace(" ", "")
    star = star.replace('"', "")
    star = star.replace('\n', "")
    x = star.split(':', 1)
    host = x[1] + "|"
    star = fp.readline()
 if "MAILPORT:" in star:
    star = star.replace(" ", "")
    star = star.replace('"', "")
    star = star.replace('\n', "")
    x = star.split(':', 1)
    port = x[1] + "|"
    star = fp.readline()
 if "MAILUSER:" in star:
    star = star.replace(" ", "")
    star = star.replace('"', "")
    star = star.replace('\n', "")
    x = star.split(':', 1)
    user = x[1] + "|"
    star = fp.readline()
 if "MAILPASS:" in star:
    star = star.replace(" ", "")
    star = star.replace('"', "")
    star = star.replace("\n", "")
    x = star.split(':', 1)
    pwd = x[1]
    star = fp.readline()
 if "MAILFROM:" in star:
    star = fp.readline()
 if "FROMNAME:" in star:
    pass
 mrigel = open("Duplicated.txt", "a")
 mrigel.write(f'{host}{port}{user}{pwd}\n')
 mrigel.close()
 lines_seen = set() # holds lines already seen
 with open("successful.txt", "w") as output_file:
   for each_line in open("Duplicated.txt", "r"):
     if each_line not in lines_seen: # check if line is not duplicate
       output_file.write(each_line)
       lines_seen.add(each_line)
 output_file.close()      


screen_clear()
print (f"    {gr}XPROAD.")
print (f"         {wh}Formatting your file + Remove Duplicated {bl}2in1")
print(f"           {bgr}  https://t.me/DailyTools {Style.RESET_ALL}")
link = input("Enter your file.txt: ")
if not os.path.isfile(link):
    print(f'Enter a valid .txt file in the some folder')
with open(link) as fp:
  for star in fp:
    if not star:
       pass
    with ThreadPoolExecutor(max_workers=40) as executor:
        executor.map(v3, [star])
        executor.shutdown(wait=True)
print(f"--- %s seconds --- List Is {gr}READY To {bl}CHECK {Style.RESET_ALL}" % (time.time() - start_time))