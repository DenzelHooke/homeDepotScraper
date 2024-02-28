from bs4 import BeautifulSoup
import requests

from typing import TypedDict, Unpack


class Query(TypedDict):
    query: str
    filter: dict


toMatch = "2-inch x 4-inch x 8 ft. SPF Dimensional Lumber" or "2x4x8" 

# query: q=2x4 spf

# Example
# https://www.homedepot.ca/search?q=2x4%20spf&filter=1pz-4uf

# 1x4: htd
# 2x3: 5ca
# 2x4: 1pz
# 2x6: 280
# 2x8: v2w
# 2x10: gt7

# spf: 4uf


class Patterns:
    
    def __init__(self):
        self.patterns = {
            "2x4": {"initial": "2-inch x 4-inch x 8 ft. SPF Dimensional Lumber"},
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
            "2x": [{'query': "2x4 spf", 'dimension': "1pz"}],
            "1x": ["1x2", "1x4", "1x10"],
            "2xSTUD": ["2x4 92 1/4", "2x4 104 1/4", "2x6 92 1/4", "2x6 104 1/4"],
        }
    
    def commonScrape(self, url: str):
        print("Scraping")   
        return BeautifulSoup(requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text, 'lxml')  
        
    
    
    def parseResult(self, web_page: BeautifulSoup):
        pass

    def generateURL(self, query: str, dimension: str):
        
        # Join string with html ampersands. 
        queries = query.split()
        url_compatible_query = '%20'.join(queries)

        return f"https://www.homedepot.ca/search?q={url_compatible_query}&filter={dimension}"
        
    
    def scrape(self, mode="lumber"):
        
        if mode == "lumber":
            for query in self.queries['2x']:
                     
                # Scrape site 
                soup = self.commonScrape(self.generateURL(query=query["query"], dimension=query["dimension"]))

                print("Done scraping")
                # Scrape every result on page
                # Print each result
                results = soup.find('article')
                print(results)
                # print(soup.prettify)


                    
                
        


def main():

    Scraper().scrape(mode="lumber")
        




if __name__ == "__main__":
    main()
  
    