import requests

url = 'https://www.python.org/'
response = requests.get(url) #Gives a Response from source which is a URL(It has get method)
print('\n response:', response  ,'\n') #Response gives back a Response code like 200 or 404
print('Headers:', response.request.headers,'\n') #Gives us general data about 
print('Status code:', response.status_code ,'\n') #Just gives us The Code from response i.g. 200 if it's OK
print('reason:', response.reason ,'\n') # Gives us 
print('Text:', response.text ,'\n') #Gives Us the source code of the URL

#Downloading a File With requests
url2 = requests.get('https://www.python.org/static/img/python-logo@2x.png')
with open('pythonLogo.jpg', 'wb') as r:
    r.write(url2.content)
    