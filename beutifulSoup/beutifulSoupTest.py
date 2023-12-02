import requests
from bs4 import BeautifulSoup

#Gets all the href's from the a tags in url.
url='https://python.org'
response = requests.get(url)
soup = BeautifulSoup(response.text ,'html.parser')

pythonSiteLinks = []
show = soup.findAll('a')
for i in show:
    pythonSiteLinks.append(i['href'])
print(pythonSiteLinks)
print(len(pythonSiteLinks))

show2 = soup.select_one('p.click-these')
print((show2.text).lstrip())

#if we don't use .text after show3 below it show us html...
show3 = soup.find('p', {'class': 'click-these'})
print('\nThis is with find', show3.text)