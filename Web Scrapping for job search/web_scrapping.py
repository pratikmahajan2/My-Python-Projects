from bs4 import BeautifulSoup
import requests

site = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=pune&cboWorkExp1=14'
html_text=requests.get(site).text

output_file = 'C:\\Users\\Pratik Mahajan\\Documents\\GitHub\\My-Python-Projects\\Web Scrapping for job search\\results.txt'
file = open(output_file,'a')

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
  company = str(job.find('h3', class_ = 'joblist-comp-name').text).strip()
  title = str(soup.find('h2').text).strip()
  temp = job.find('ul', class_ = 'top-jd-dtl clearfix')
  exp1 = temp.find('li').text.replace('card_travel','')
  skills = str(job.find('span', class_='srp-skills').text).strip()
  string = company + ' Job Role: ' + title + ' Experience: ' + exp1 + ' Skills: ' + skills + '\n'
  file.write(string)

file.close()