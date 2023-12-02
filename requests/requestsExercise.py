import requests 

requestsLogo = requests.get('https://requests.readthedocs.io/en/latest/_static/requests-sidebar.png')
with open('requestsLogo.png', 'wb') as r :
    r.write(requestsLogo.content)

url = 'https://requests.readthedocs.io/en/latest/'
#Test for response
response = requests.get(url)
print('\n', response.status_code)
print(response.text)