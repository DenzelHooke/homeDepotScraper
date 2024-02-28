import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import undetected_chromedriver as uc



options = Options()
# Keeps browser open
# options.add_experimental_option("detach", True)


# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver = uc.Chrome()

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
    wait = WebDriverWait(driver=driver, timeout=10)
    
    # Scraper().scrape(mode="lumber")
    driver.get(r"https://www.homedepot.ca/search?q=2x4%20spf&filter=1pz-4uf")
    # links = driver.find_elements("xpath", "//a[@href]")
    
    # for link in links:
    #     print(link.get_attribute("innerHTML"))
    
    # product_cards = driver.find_elements("xpath", 
    #                                      "//article[contains(@class, acl-product-card)][.//h2[contains(@class, acl-product-card__title)]]")
    
    # product_cards = driver.find_elements("xpath", 
    #                                      "//article[contains(@class, acl-product-card)][.//a[contains(@class, acl-product-card__title-link)][.//span[text()[contains(., '2-inch x 4-inch x 8 ft. SPF Dimensional Lumber')]]]]//h2//span") 
    
    time.sleep(3)
    
    product_cards = driver.find_elements("xpath", 
                                         "//article[contains(@class, acl-product-card)][.//a[contains(@class, acl-product-card__title-link)]]")

    for card in product_cards: 
        # print(card.)
        product_name = card.find_element(By.XPATH, ".//h2//span")
        print(product_name.text)
        
        # product_price = card.find_element(By.XPATH, './/div[contains(@class, "acl-product-card__price")]')
        # product_dollar = wait.until(EC.visibility_of(product_price.find_element('.//div[contains(@class, "acl-product-card__price-dollars")]//span'))).text
        
        prod_cent_waited = wait.until(EC.visibility_of(card.find_element(By.XPATH, "//div[contains(@class, 'acl-product-card__price-cents')]//span")))
        prod_dollar_waited = wait.until(EC.visibility_of(card.find_element(By.XPATH, ".//div[contains(@class, 'acl-product-card__price-dollars')]//span")))
        
        # print(f'${product_dllr}')
        
        pieceCost = float(f"{prod_dollar_waited.text.split('$')[1]}.{prod_cent_waited.text.split("\n")[0]}")
       
        print("Cost: $", pieceCost)
        # print(pieceCost)
        
        # print(product_price.get_attribute("innerHTML"))
        
        
        


if __name__ == "__main__":
    main()
  
    