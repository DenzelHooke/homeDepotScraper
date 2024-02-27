from bs4 import BeautifulSoup
import requests
import time
import re

toMatch = "2-inch x 4-inch x 8 ft. SPF Dimensional Lumber"

class Patterns:
    
    def __init__(self):
        self.patterns = {
            "2x4": {initial: "2-inch x 4-inch x 8 ft. SPF Dimensional Lumber"},
            "2x6": "",
            "2x8": "",
            "2x10": "",
            "2x12": ""
        }

class Scraper:
    main_url = "https://www.homedepot.ca/search"
    
    def __init__(self):
        self.soup = None
        self.queries = {
            "2x": ["2x4", "2x6", "2x8", "2x10", "2x12"],
            "1x": ["1x2", "1x4", "1x10"],
            "2xSTUD": ["2x4 92 1/4", "2x4 104 1/4", "2x6 92 1/4", "2x6 104 1/4"],
        }
    
    def commonScrape(self, url):
        return BeautifulSoup(requests.get(self.url).text, 'lxml')  
        
    
    def match(self):
        pass
        
    
    def scrape(self, mode="lumber"):
        
        if mode == "lumber":
            for query in self.queries['2x']:
                
                length = 8
                while length <= 16:
                    # self.soup = self.commonScrape(url=f'{Scraper.main_url}?q={query}x{length}')
                    
                    # print(self.soup.find())
                    length += 2
                    
                
        


def main():

    Scraper().scrape(mode="lumber")
        




if __name__ == "__main__":
    main()
  
    