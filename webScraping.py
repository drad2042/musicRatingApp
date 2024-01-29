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


    def scrapeBySong(self):
        #THIS CHUNK OF CODE TAKES i ARTISTS AND SPLITS UP THE INDIVIDUAL ALBUMS
        URL = "https://api.deezer.com/artist/"
        for i in range(1,2):
            albumURL = URL + str(i) + "/albums"
            r = requests.get(albumURL)

            soup = BeautifulSoup(r.content, 'lxml').text
            #soup = json.loads(soup)
            soup = soup.replace("{\"data\":[{", "")
            albumList = soup.split("},{") # albumList is the individual block of code for each album.
            albumList[-1] = albumList[-1].split("}")[0]

            #TURNS THE ALBUMS INTO A LIST OF ALBUMS.
            for x in range(1, len(albumList)): #Various albums for range of artists
                albumList[x] = "{" + albumList[x] + "}"
                albumList[x] = json.loads(albumList[x])

                trackURL = "https://api.deezer.com/album/" + str(albumList[x]["id"])
                r2 = requests.get(trackURL)

                soup = BeautifulSoup(r2.content, 'lxml').text
                tracklist = soup.split("},{")
                
                for y in range(1, len(tracklist)):
                    print(tracklist[y] + '\n')

           

        #"https://api.deezer.com/album/428991547/"