from webScraping import Scraper
import time
s = Scraper()

## USES DEEZER API: https://developers.deezer.com/api/album

def main():
    start = time.time()
    s.scrapeByArtist()
    end = time.time()
    totalTime = end - start
    print(totalTime)

main()
    