import requests 
from bs4 import BeautifulSoup
import re


def download(url):
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.findAll('a', href=re.compile('.jpg'))
    for info in links:
        link = info.get('href')
        with requests.get(link, stream=True) as r:
            with open("sonic.apk", 'wb') as f:
                for apk in r.iter_content(chunk_size= 1024):
                    f.write(apk)
                
download('https://par30games.net/98865/sonic-dash/')