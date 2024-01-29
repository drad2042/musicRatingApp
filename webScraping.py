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
        for i in range(3000,3500):
            r = requests.get(URL + str(i) + "/albums")

            soup = BeautifulSoup(r.content, 'lxml').text
            #soup = json.loads(soup)
            soup = soup.replace("{\"data\":[{", "")
            albumList = soup.split("},{")
            albumList[-1] = albumList[-1].split("}")[0]

            for x in range(1, len(albumList)):
                albumList[x] = "{" + albumList[x] + "}"
                albumList[x] = json.loads(albumList[x])

                try:
                    print(albumList[x]["title"])
                except:
                    continue
            #for album in albumList:
            #    print(album + '\n')