from bs4 import BeautifulSoup
import requests

htmlText = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python+Developer&txtLocation=&cboWorkExp1=0').text
soup = BeautifulSoup(htmlText, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    publishedDate = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in publishedDate:
        companyName = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')

        print(f''' 
        Company Name: {companyName}
        Required Skills: {skills}
        Published Date: {publishedDate}
        ''')
        print()
