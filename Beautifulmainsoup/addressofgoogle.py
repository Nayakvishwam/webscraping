from bs4 import BeautifulSoup
import requests
data=requests.get('https://www.google.com/maps/@23.0653952,72.548352,12z')
alldata=BeautifulSoup(data.content,'lxml')
getall=alldata.find_all('div',class_='DAdBuc')
for i in getall:
    print(i)