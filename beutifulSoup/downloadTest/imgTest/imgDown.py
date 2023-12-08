import requests 
from bs4 import BeautifulSoup
import re
import random 

def download(url):
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.findAll('img', src=re.compile('.jpg'))
    for info in links:
        link = info.get('src')
        name = random.randrange(1 , 1000)
        with requests.get(link, stream=True) as r:
            with open(str(name)+".jpg", 'wb') as f:
                for image in r.iter_content(chunk_size= 1024):
                    f.write(image)
                
download('https://par30games.net/playstation-4/')