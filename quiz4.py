import time
from bs4 import BeautifulSoup
import requests
import sqlite3

conn = sqlite3.connect('jobs.sqlite3')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS jobs (
       company VARCHAR(15), req_skills VARCHAR(100))''')
for i in range(1, 6):
    url = f'https://www.timesjobs.com/candidate/job-search.html?from=submit&searchType=Home_Search&luceneResultSize=25&postWeek=60&cboPresFuncArea=35&pDate=Y&sequence={i}&startPage=1'
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        comp_name = job.find('h3', class_='joblist-comp-name').text.strip()
        if "(More Jobs)" in comp_name:
            comp_name.replace("(More Jobs)", "")
        skills = job.find('span', class_='srp-skills').text.strip()
        cur.execute('''INSERT INTO jobs (company,req_skills) VALUES (?,?)''', (comp_name, skills))
        conn.commit()
    time.sleep(15)

conn.close()
