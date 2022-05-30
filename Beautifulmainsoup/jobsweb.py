import requests
import time
from bs4 import BeautifulSoup
skill=input('Enter your skill\n')
data=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=Ahmedabad&cboWorkExp1=0')
alldata=BeautifulSoup(data.content,'lxml')
jobs=alldata.find_all('li',class_='clearfix job-bx wht-shd-bx')
def find_jobs():
    for index,job in enumerate(jobs):
        publisheddate=job.find('span',class_='sim-posted').span.text
        if 'few' in publisheddate:
            companyname=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills=job.find('span',class_='srp-skills').text.replace(' ','  ')
            linkofjob=job.header.h2.a['href']
            if skill not in skills:
                print(f'Comapny name :- {companyname.strip()}\n Required skill :- {skills.strip()}\n More Info :- {linkofjob.strip()}\n')
                
find_jobs()