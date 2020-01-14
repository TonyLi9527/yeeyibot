#!/usr/bin/env python3

import re
from robobrowser import RoboBrowser
from time import sleep, localtime, ctime, mktime
from random import randint

browser = RoboBrowser(history=True, parser='html.parser')

url = 'your_url'
log_path = 'path_to_log.log'

login_field = 'username'  # 'email' or 'username'
username = 'your_username'  # username or email
password = 'your_password'

browser.session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'
button = None


def login():
    # login
    browser.open('http://www.yeeyi.com/bbs/forum.php')
    form = browser.get_form(id='lsform')
    form['fastloginfield'] = login_field   # username or email
    form['username'].value = username.encode('GBK')   # username or email
    form['password'].value = password
    browser.submit_form(form)


#delay = randint(0, 600)
#sleep(delay)
browser.open(url)
button = browser.get_link('提升帖子')
if not button:
    login()
    browser.open(url)
    button = browser.get_link('提升帖子')
browser.follow_link(button)
response = browser.find(id="messagetext").find("p")
with open(log_path, 'a') as log:
    log.write('Button clicked, at ' + ctime(mktime(localtime())) + ' ')
    if response is None:
        log.write('No response, please check')
    else:
        log.write(response.text)
# print(response.text)


