from bs4 import BeautifulSoup
import requests
import pandas as pd

class Scraper:
    def __init__(self):
        pass

    def scrapeByArtist(self): #Scrapes data off deezer by artist
        URL = "https://api.deezer.com/artist/"
        for i in range(1,2):
            r = requests.get(URL + str(i))
            soup = BeautifulSoup(r.content, 'html5lib')
        