import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup
from time import sleep

k = 0

while(True):
    user = 'swnotice01@gmail.com'
    password = 'interface518'

    student = ['riyenas0925@gmail.com', 'rlagksml99@gmail.com','nhk9680@gmail.com']

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
        mailServer.login(user, password)

        for n in range(3):
            mailServer.sendmail(user, student[n], msg.as_string())

        mailServer.close()


    # 홈페이지

    contents = []
    writers = []

    req_list = requests.get('http://board.sejong.ac.kr/boardlist.do?bbsConfigFK=333')

    html_list = req_list.text
    soup_list = BeautifulSoup(html_list, 'html.parser')

    names = soup_list.select('a')
    indexes = soup_list.find_all('td', {'class': 'index'})

    names = names[:10]

    for n in names:
        # print(n.get_text()
        test = n.get('href')

        req_content = requests.get('http://board.sejong.ac.kr' + test)
        # print(req_content)
        html_content = req_content.text

        # print(test2)

        soup_content = BeautifulSoup(html_content, 'html.parser')

        contents_temp = soup_content.find_all('td', {'class': 'content'})
        writers_temp = soup_content.find_all('td', {'class': 'writer'})

        contents.append(contents_temp[0])
        writers.append(writers_temp[0])

        #print(contents)

        '''
        for m in contents:
            print(m.get_text())
        '''

    print(names[k].get_text())
    print(writers[0].get_text())
    print(contents[k].get_text())

    gmail_send(user, writers[0].get_text(), indexes[k].get_text() + names[k].get_text(), contents[k].get_text())

    print('전송했다아아ㅏㅏㅏ')

    sleep(10)