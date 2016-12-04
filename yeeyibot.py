from robobrowser import RoboBrowser
from time import sleep, localtime, ctime, mktime
from random import randint

browser = RoboBrowser(history=True, parser='html.parser')

url = 'http://www.yeeyi.com/bbs/thread-XXXXXX-X-X.html'

login_field = 'email'  # 'email' or 'username'
username = 'XXXX@gmail.com'  # username or email
password = '********' 

browser.session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'
button = None

def login():
    # login
    browser.open('http://www.yeeyi.com/bbs/forum.php')
    form = browser.get_form(id='lsform')
    form['fastloginfield'] = login_field   # username or email
    form['username'] = username   # username or email
    form['password'] = password
    browser.submit_form(form)

while True:
    browser.open(url)
    button = browser.get_link('提升帖子')
    if not button:
        login()
        browser.open(url)
        button = browser.get_link('提升帖子')
    browser.follow_link(button)
    delay = 1800 + randint(0, 120)
    print('Button clicked, next click:', ctime(mktime(localtime())+delay))
    sleep(delay)