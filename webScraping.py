from bs4 import BeautifulSoup
import requests
import pandas as pd
import lxml
import json

class Scraper:
    def __init__(self):
        pass

    def scrapeByArtist(self): #Scrapes data off deezer by artist
        URL = "https://api.deezer.com/artist/"
        for i in range(1,100):
            r = requests.get(URL + str(i))
            
            soup = BeautifulSoup(r.content, 'lxml').text  
            soup = json.loads(soup)
            try:
                print(soup["name"])
            except:
                continue

    def scrapeByAlbum(self):
        URL = "https://api.deezer.com/artist/"
        for i in range(1, 2):
            r = requests.get(URL + str(i) + "/albums")

            soup = BeautifulSoup(r.content, 'lxml').text
            #soup = json.loads(soup)
            soup = soup.replace("{\"data\":[{", "")
            albumList = soup.split("},{")

            for album in albumList:
                print(album + '\n')