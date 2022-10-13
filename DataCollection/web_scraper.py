
from gettext import Catalog
from lib2to3.pgen2 import driver
from unicodedata import name
from xml.etree.ElementPath import xpath_tokenizer
import json
import time 
import uuid
import boto3
from sqlalchemy import create_engine
import pandas as pd
import uuid
from unittest.main import main
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException , TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service

 
from selenium.common.exceptions import WebDriverException

class Scraper:

    '''
    
    This class is used to scrape data from websites.

    '''  


            
    def __init__(self): 

       
        self.link_list = []
        self.image_list = []   
        self.dictionary = []   
        self.url = "https://www.gog.com"
       # service = Service(r'C:\Users\Admin\Downloads\chromedriver_103\chromedriver.exe')
       
        options = Options()

        #options.binary_location(r"C:\Program Files\LibreWolf\librewolf.exe")
    # options.headless = True 
        #defines the webdriver used
        #fp = webdriver.FirefoxProfile()
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options) #service=service)
        self.driver.get(self.url)     
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        time.sleep(5)
        self.enable_cookies()
 
   
    
    ''' Disables cookies on the website
    ''' 

    print("Scraper ready")
    def enable_cookies(self):
        cookie_banner = self.driver.find_element(By.ID, 'cookiebanner')
        cookies_button = cookie_banner.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
        time.sleep(1)
        cookies_button.click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div[2]' )

    
    ''' Stores file inforation and places them into a dictionary
    ''' 
    def store_files(self, path_to_store: str, storage):
        with open(f"{path_to_store}/data.json", "w") as outfile:
            json.dumps(storage,  outfile)
        product_dict = {'name': [], 'price':[],'url':[],'uuid4':[]}
        self.dictionary = product_dict
        

    def generate_uuid_info(self):
        unique_id = str(uuid.uuid4())
        return unique_id    

    def get_container_links(self, 
        xpath_to_container:str, 
        #max_index: int, 
        xpath_container_elem: str
        ):
        container = self.driver.find_element(by=By.XPATH, value=xpath_to_container)
        products = container.find_elements(By.XPATH, value=xpath_container_elem)
        self.link_list = []
         
        for product in products:
            
            self.link_list.append(product.get_attribute('href'))
            
        return self.link_list
        


    def scroll_page(self, items_to_scroll, no_of_scrolls:int):
        self.driver.execute_script()

    ''' def add_dic(self):
        for item in self.link_list:
            self.target_link = item
            self.driver.get(item)

            self.dictionary['name'].append(self.product_name)
        pass
    '''

    def get_product(self, product_page):
        self.driver.get(product_page)
        product_name = self.driver.find_element(by=By.XPATH, value='//h1[@class="productcard-basics__title"]').get_attribute("text")
        product_price = self.driver.find_element(by=By.XPATH, value='//span[@class="product-actions-price__final-amount _price ng-binding"]').get_attribute("text")
        product_url = self.driver.current_url
        product_id = self.generate_uuid_info()
        product_dict = {'name': product_name, 'price':product_price,'url':product_url,'uuid4':product_id}
        
        return product_dict

    def check_top_bar(self):
        ''' #, bar_button
        Finds and clicks the store button
        '''
        all_products = self.driver.find_element(By.LINK_TEXT,"STORE")
        read_community = self.driver.find_element(By.LINK_TEXT,"COMMUNITY")
        support_page = self.driver.find_element(By.LINK_TEXT,"SUPPORT")
        time.sleep(1)
        all_products.click()
        time.sleep(1)
        
        #bar_button 
        #for i in range(3):
        #    self.check_top_bar()
    


    def get_all_products(self):
        prod = 0
        for prod in self.link_list:
            print(self.get_product().product_dict)
            prod+=1
        return self.get_product


    def run(self):
        self.driver.get(self.url)
        pass
    

if __name__ == '__main__':
    webscraper = Scraper()

    webscraper.check_top_bar()
    print(webscraper.get_container_links(xpath_to_container='//div[@class="paginated-products-grid grid"]', xpath_container_elem='//a[@class="product-tile product-tile--grid"]'))
   