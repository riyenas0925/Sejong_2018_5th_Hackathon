import requests
import time
from bs4 import BeautifulSoup
from locale import atoi
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

start_time = time.time()

admin_user = 'swnotice01@gmail.com'
admin_password = 'interface518'

def gmail_send(user, to, subject, text):

    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text))

    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(admin_user, admin_password)
    mailServer.sendmail(admin_user, 'riyenas0925@gmail.com', msg.as_string())
    mailServer.close()

def notice_parse():
    req_list = requests.get('http://board.sejong.ac.kr/boardlist.do?bbsConfigFK=333')

    html_list = req_list.text
    soup_list = BeautifulSoup(html_list, 'html.parser')

    names = soup_list.select('a')
    indexes = soup_list.find_all('td', {'class': 'index'})

    names = names[:10]
    indexes = indexes[:10]

    lastindex = 935
    newindex = atoi(indexes[0].get_text())
    repeatnum=newindex-lastindex

    for n in names[0:repeatnum]:
        link = n.get('href')

        contents = []
        writers = []

        req_content = requests.get('http://board.sejong.ac.kr' + link)

        html_content = req_content.text
        soup_content = BeautifulSoup(html_content, 'html.parser')

        contents_temp = soup_content.find_all('td', {'class': 'content'})
        writers_temp = soup_content.find_all('td', {'class': 'writer'})

        contents.append(contents_temp[0])
        writers.append(writers_temp[0])

        gmail_send(admin_user, writers[0].get_text(), names[0].get_text(), contents[0].get_text())

notice_parse()

print("--- 전송시간 %s seconds ---" %(time.time() - start_time))