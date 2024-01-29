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
        for i in range(300,400):
            albumsURL = URL + str(i) + "/albums" #Navigates to the URL for an artist's albums.
            r = requests.get(albumsURL)

            soup = BeautifulSoup(r.content, 'lxml').text
            #soup = json.loads(soup)
            soup = soup.replace("{\"data\":[{", "")
            albumList = soup.split("},{") # albumList is the individual block of code for each album.
            albumList[-1] = albumList[-1].split("}")[0]

            #TURNS THE ALBUMS INTO A LIST OF ALBUMS.
            for x in range(0, 1): #List of albums for each artist. len(albumList)
                albumList[x] = "{" + albumList[x] + "}"
                albumList[x] = json.loads(albumList[x])

                albumID = str(albumList[x]["id"])
                trackURL = "https://api.deezer.com/album/" + albumID + "/tracks"
                r2 = requests.get(trackURL)

                soupAlbum = BeautifulSoup(r2.content, 'lxml').text
                songList = soupAlbum.split("},{") #Tracklist splits tge songs up into individual blocks.
                
                for y in range(1, len(songList) - 1):
                    songList[y] = "{" + songList[y] + "}"
                    #print(songList[y])
                    songList[y] = json.loads(songList[y])
                    print(songList[y])

           

        #"https://api.deezer.com/album/428991547/"