import requests
from bs4 import BeautifulSoup

url= 'https://skybooks.ir/categories/%D9%87%D9%88%D8%B4-%D9%85%D8%B5%D9%86%D9%88%D8%B9%DB%8C'

linksList = list()
catagories = ['هوش-مصنوعی', 'Machine-Learning', 'Deep-Learning']

for page in catagories:
    page = requests.get(url+page)
    soup = BeautifulSoup(page.text ,'html.parser')
    show = soup.select('a>p')
    for i in show:
        print((i.text).replace('\n', ''))
