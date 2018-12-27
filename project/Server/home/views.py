from django.shortcuts import render
from .models import User
from .models import Admin
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup
from time import sleep
from locale import atoi

# Create your views here.

def list(request):
    users = User.objects.all()
    admins = Admin.objects.all()

    for admin_db in admins:
        admin_user = admin_db.email
        admin_password = admin_db.password
        lastindex = admin_db.lastindex

    student = []

    for user_db in users:
        student.append(user_db.email)

    #print(student)

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

        for user_send in users:
            mailServer.sendmail(admin_user, user_send.email, msg.as_string())

        mailServer.close()

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

    newindex = atoi(indexes[0].get_text())

    print("newindex: ", newindex)
    repeatnum=newindex-lastindex

    if(repeatnum!=0):
        for i in range(repeatnum):
            k=repeatnum-i-1
            gmail_send(admin_user, writers[0].get_text(), names[k].get_text(), contents[k].get_text())

        admins.update(lastindex=newindex)
        print('lastindex: ', lastindex)
    context = {'users': users, 'admins': admins,}

    return render(request, 'home/list.html', context)
