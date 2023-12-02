import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations'
response = requests.get(url)

states = list()

soup = BeautifulSoup(response.text , 'html.parser')
tbodyEl = soup.find('tbody')
rows = tbodyEl.find_all('tr')
for row in rows:
    elements = row.find_all('td')
    state = list()
    for element in elements:
            state.append(element.text.strip())
            states.append(state)
print(*states, sep="\n")
