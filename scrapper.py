import random
from bs4 import BeautifulSoup
import requests

def WebScrapeNewUniversity():
    listofarticles = []
    url = "https://www.newuniversity.org/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    access = soup.find_all('h3')
    for a in access[:5]:
            listofarticles.append(a.text)
    return listofarticles

def weather():
        url = "https://forecast.weather.gov/MapClick.php?lat=33.638513800000055&lon=-117.83767549999999#.YjU7g-rMK5c"
        response = requests.get(url)
        soup = BeautifulSoup(response.text,'lxml')
        #print(soup)
        access = soup.find(class_ = "myforecast-current-lrg")

        return access.text

def GetRandomNumber():
        return random.randrange(1,15)

