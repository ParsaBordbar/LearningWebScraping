import requests 
from bs4 import BeautifulSoup
import re

def download(url):
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href = re.compile('index.mp4'))
    for info in links:
        link = info.get('href')
        with requests.get(link, stream=True) as r:
            with open('Lecture Video (720p).mp4', 'wb') as f:
                for video in r.iter_content(chunk_size= 1024):
                    f.write(video)
                
download('https://www.coursera.org/learn/python-network-data/lecture/SzYGn/welcome-to-python-guido-van-rossum')