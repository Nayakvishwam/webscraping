from bs4 import BeautifulSoup
import requests
data = requests.get(
    'https://www.amazon.in/?tag=msndeskabkin-21&hvadid=72705283629710&hvqmt=e&hvbmt=be&hvdev=c&ref=pd_sl_7qhce485bd_e')
formatdata = BeautifulSoup(data.content, 'html.parser')
alldata = formatdata.prettify()
takeiamges = formatdata.select('img')
for i in takeiamges:
    imagesrc = i.get('src')
    imagesalt = i.get('alt')
    print(imagesrc)
    print(imagesalt)
# gettdata=formatdata.find('div',class_='navFooterLinkCol navAccessibility')
# content=gettdata.find_all('ul')
# print(content)
# important=formatdata.find('div',class_='navFooterLinkCol navAccessibility')
# mainalldaa=important.find_all('ul')
# for i in mainalldaa:
#     pre=i.find_all('a')
#     for j in pre:
#         print(j.text)
# formatadataall = formatdata.find('div', class_='a-cardui-header')
# aal=formatadataall.find_all('h2')
# for i in aal:
#     print(i)
# for i in aal:
#     print(i.text)
# with open('main.html', 'w') as data:
#     data.write(formatdata.prettify())