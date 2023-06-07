from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    html_text=requests.get('https://www.indeed.com/jobs?q=front+end+developer&l=Remote').text
    soup=BeautifulSoup(html_text, 'lxml')
    jobs=soup.find_all('div', class_='jobsearch-SerpJobCard')
    for index, job in enumerate(jobs):
        published_date=job.find('span', class_='date').text
        if 'Today' in published_date:
            company_name=job.find('span', class_='company').text.replace(' ','')
            title=job.find('h2', class_='title').text
            skills=job.find('div', class_='summary').text
            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f'Title: {title.strip()} \n')
                f.write(f'Published Date: {published_date} \n')
                f.write(f'Company Name: {company_name.strip()} \n')
                f.write(f'Required: {skills.strip()}')            
            print(f'File saved: {index}')    

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60)            

        