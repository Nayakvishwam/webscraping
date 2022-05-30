from bs4 import BeautifulSoup
import requests
data=requests.get('https://www.amazon.in/?tag=msndeskabkin-21&hvadid=72705283629710&hvqmt=e&hvbmt=be&hvdev=c&ref=pd_sl_7qhce485bd_e')
formatdata=BeautifulSoup(data.content,'html.parser')
changetypedata=formatdata.encode()
with open('main.html','wb') as writedata:
    writedata.write(changetypedata)
