from urllib import response
import mechanize
import os
import time 
import datetime
import sys
browser =mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent','Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36')]

browser.set_handle_refresh(False)

Url = "https://m.facebook.com/login.php"

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

def sp(stri):
    for letter in stri:
        print(letter, end="")
        sys.stdout.flush()
        time.sleep(0.01)
      

clear()

def login():
  browser.open(Url)
  browser.select_form(nr=0)
  browser.form['email'] = USERNAME
  browser.form['pass'] = PASSWORD
  r = browser.submit()
  f = open("login.htm" , "wb")
  f.write(r.read())
  
  f.close()
  browser.select_form(nr=0)
  print("\033[1;33;40m",end = "")
  sp("\nEnter two factor code : \n")
  print("\033[1;33;40m")
  apr = str(input())
  print()
  try:
    browser.form['approvals_code'] = apr
  except mechanize._form_controls.ControlNotFoundError:
    print("wrong password or some shit ,check generated file")
    f =open("epage_" + str(USERNAME) + "html","wb")
    f.write(r.read())
    f.close()
    exit(1)
  r = browser.submit()
  browser.select_form(nr=0)
  try:
    browser.form['name_action_selected'] = ['save_device']
  except mechanize._form_controls.ControlNotFoundError:
    print("some gone down,check generated file")
    f = open("epage_" +str(USERNAME) + "html","wb")
    f.write(r.read())
    f.close()
    exit(1)
  r = browser.submit()
  f = open("full_login_" + str(USERNAME) + "html","wb")
  f.write(r.read())
  f.close()

def findfbchat(curl):
  r = browser.open(curl)
  x = browser.title()
  if x == "review recent login":
    print("\nFacebook wants to review your recent actions,\nPlease fix that and then re run the program.")
    exit(1)
  if x == "Login approval neende":
    print("\nYour account is stuck on verification \nplease do it and then re run the program.")
    exit(1)
  if x == "Epsilon":
    print("\nYour account got locked,recover it kindly and re run the script.")
    exit(1)
    
def sendtextchat(comment):
  try:
    browser.select_form(nr=1)
  except mechanize.mechanize.FormNotFoundError:
    print("\033[1;31;40m",end ="")
    print("»»",comment, "\n")
  try:
    browser.form['body'] = comment
  except mechanize._form_controls.ControlNotFoundError:
    print("\033[1;31;40m",end ="")
    print("»»",comment, "\n")
    r = browser.submit()
    print("\003[1;32;40m" ,end ="")
    e = datetime.datetime.now()
    print(e.strftime("»» %d%m%Y %I%M%S%p"))
logo = ("""\033[97;1m
  /$$$$$$  /$$   /$$  /$$$$$$  /$$   /$$ /$$$$$$$    
 /$$__  $$| $$$ | $$ /$$__  $$| $$$ | $$| $$__  $$   
| $$  \ $$| $$$$| $$| $$  \ $$| $$$$| $$| $$  \ $$   
| $$$$$$$$| $$ $$ $$| $$$$$$$$| $$ $$ $$| $$  | $$   
| $$__  $$| $$  $$$$| $$__  $$| $$  $$$$| $$  | $$   
| $$  | $$| $$\  $$$| $$  | $$| $$\  $$$| $$  | $$   
| $$  | $$| $$ \  $$| $$  | $$| $$ \  $$| $$$$$$$/   
|__/  |__/|__/  \__/|__/  |__/|__/  \__/|_______/    
                                                     
                                                     
                                                     
 /$$      /$$ /$$$$$$$$ /$$   /$$ /$$$$$$$   /$$$$$$ 
| $$$    /$$$| $$_____/| $$  | $$| $$__  $$ /$$__  $$
| $$$$  /$$$$| $$      | $$  | $$| $$  \ $$| $$  \ $$
| $$ $$/$$ $$| $$$$$   | $$$$$$$$| $$$$$$$/| $$$$$$$$
| $$  $$$| $$| $$__/   | $$__  $$| $$__  $$| $$__  $$
| $$\  $ | $$| $$      | $$  | $$| $$  \ $$| $$  | $$
| $$ \/  | $$| $$$$$$$$| $$  | $$| $$  | $$| $$  | $$
|__/     |__/|________/|__/  |__/|__/  |__/|__/  |__/
                                                     
                                                     

                                                   
/033[1;32m""")
os.system("clear")
print(logo)



    



print("[-[ MADE BY KING AN9ND M3HR9]-]")

print("\033[1;37;40m",end ="")
sp("\nEnter your email or mob no... : \n")
print("\033[1;33;40m")
USERNAME = str(input())
print("\033[1;33;40m",end ="")
sp("\nEnter your password :\n")
print("\033[1;37;40m")
PASSWORD = str(input())
print("\033[1;33;40m",end ="")
sp("Enter the Conversation link :\n")
print("\033[1;37;40m")
conversation = str(input())
curl = "https://m.facebook.com/message/t/" + str(conversation)
print("\033[1;33;40m",end ="")
sp("Enter kidx name : \n")
print("\033[1;37;40m")
np1 = str(input())
print("\033[1;33;40m",end ="")
sp("Enter notepad file: \n")
print("\033[1;33;40m")
np = str(input())
f = open(np,"r")
lines = f.readlines()
f.close()
print()
print("\033[1;33;40m",end ="")
sp("Enter time delay insecond :\n")
print("\033[1;37;40m")
t = int(input())

clear()
print("\033[1;37;40m")
e = datetime.datetime.now()
print(e.strftime("»» %d%m%Y %I%M%S%p"))
print()
count = 0
while True:
  for line in lines:
    if len(line) > 0:
      if count != 0:
        time.sleep(t)
        findfbchat(curl)
        sendtextchat(str(np1) + line)
        count += 1
        if count % 50 == 0:
          time.sleep(1)
          clear()