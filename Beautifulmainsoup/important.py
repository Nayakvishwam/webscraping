from bs4 import BeautifulSoup
import os
os.getcwd()
with open('main.html','rb') as dataall:
    content=dataall.read()
    soup=BeautifulSoup(content,'lxml')
    data=soup.find('div')
    dataall=soup.find_all('div',class_="a-cardui-footer")
    for data in dataall:
        # print(data.a.prettify())
        print(data.text)
