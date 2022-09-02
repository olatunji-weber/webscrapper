from bs4 import BeautifulSoup
import requests
import time

print(f"Put some skill that you are not familiar with... ")
unfamiliarSkill = input('>')
print(f"Filtering out {unfamiliarSkill}")

def findJobs():
    htmlText = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python+Developer&txtLocation=&cboWorkExp1=0').text
    soup = BeautifulSoup(htmlText, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        publishedDate = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in publishedDate:
            companyName = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            jobLink = job.header.h2.a['href']
            if unfamiliarSkill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {companyName.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f"More Details: {jobLink}")
                print(f"File Saved: {index}")
            
if __name__ == '__main__':
    while True:
        findJobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)
