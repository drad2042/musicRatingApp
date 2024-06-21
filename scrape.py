import requests
import pandas as pd
import secrets
from dotenv import load_dotenv
import os



class Data_Scrape:
    def __init__(self):

        load_dotenv()
        self.api_key = os.getenv("API_KEY")
        self.api_secret = os.getenv("API_SECRET")

    def main(self):
        return "HELLO"

c = Data_Scrape()

