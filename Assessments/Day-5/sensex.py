from requests import get
from bs4 import BeautifulSoup
url='https://www.moneycontrol.com/'
response=get(url)

soup=BeautifulSoup(response.text,'html.parser')

gainers = soup.find_all('div',attrs={'id':'tgNifty'})
print("Gainers Nifty")
for gainer in gainers:
    links = gainer.find_all('a')
    for link in links[:-1]:
        print(link.get('title'))
print("---------------------------------------------------")
losers = soup.find_all('div',attrs={'id':'tlNifty'})
print("Losers Nifty")
for loser in losers:
    links = loser.find_all('a')
    for link in links[:-1]:
        print(link.get('title'))
print ("--------------------------------------------------")
losers = soup.find_all('div',attrs={'id':'tlSensex'})
print("Losers-Sensex")
for loser in losers:
    links = loser.find_all('a')
    for link in links[:-1]:
        print(link.get('title'))
print("---------------------------------------------------")
gainers = soup.find_all('div',attrs={'id':'tgSensex'})
print("Gainers-Sensex")
for gainer in gainers:
    links = gainer.find_all('a')
    for link in links[:-1]:
        print(link.get('title'))