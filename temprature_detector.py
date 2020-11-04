#pip install requests
#pip install bs4

import requests
from bs4 import BeautifulSoup

#select the user agent
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}

#Take Input as the city name
city_name=input("Enter the Place name: ")
#generate the url
url=f'https://www.timeanddate.com/weather/india/{city_name}'

page=requests.get(url)      #Get the page from website
s=BeautifulSoup(page.text,'html.parser')        #parse the content
update=s.find('div',class_='h2').text


print(update)
temp=int(update[:2])


if temp>=25:
    print("Its sunny Day!")
elif temp<25 and temp>15:
    print("Its Cloudy Day,It may rain today!")
elif temp<15 and temp>0:
    print("Its Cold Today!")
else:
    print("Snow fall may occur today")


