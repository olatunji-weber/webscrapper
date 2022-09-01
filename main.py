from bs4 import BeautifulSoup
import requests

htmlText = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python+Developer&txtLocation=&cboWorkExp1=0').text
soup = BeautifulSoup(htmlText, 'lxml')
job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
companyName = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
publishedDate = job.find('span', class_ = 'sim-posted').text

print(f''' 
Company Name: {companyName}
Required Skills: {skills}
Published Date: {publishedDate}
''')
