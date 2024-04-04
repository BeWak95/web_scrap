import requests
import pandas as pd
from bs4 import BeautifulSoup

response = requests.get('https://realpython.github.io/fake-jobs/')
# print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)

position_name=[]
company_name=[]
address=[]

job_name = soup.find_all('h2', attrs={'class':'title is-5'})
c_name = soup.find_all('h3', attrs={'class':'subtitle is-6 company'})
a_dd = soup.find_all('p', attrs={'class':'location'})

for item in job_name:
    position_name.append(item.text)

for i in c_name:
    company_name.append(i.text)

for j in a_dd:
    address.append(j.text)

print(address)

dic = {'Position_title': position_name,
       "Company_name": company_name,
       "Address": address}

# print(dic)
table=pd.DataFrame(dic)

table.to_excel('jon.xlsx')