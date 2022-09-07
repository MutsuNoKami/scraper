
from lib2to3.pgen2 import driver
from xml.etree.ElementPath import xpath_tokenizer
import requests
import json
import time 
import os
import uuid
import boto3 
import chromedriver_autoinstaller
from sqlalchemy import create_engine
import pandas as pd
import uuid
import sqlite3 as lite

from unittest.main import main

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.chrome.service import Service


from selenium.common.exceptions import WebDriverException

PATH = r'C:\Users\Admin\Downloads\chromedriver_103\chromedriver.exe'
class Scraper:

    '''
    
    This class is used to scrape data from websites.

    '''  

 
    print("Scraper ready")
    def enable_cookies(self):
        cookie_banner = self.driver.find_element(By.ID, 'cookiebanner')
        cookies_button = cookie_banner.find_element(By.CLASS_NAME, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
        cookies_button.click()

        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div[2]' )

    def store_files(self, path_to_store: str):
        pass

    def get_container_links(self, zpath_to_container:str, max_index: int, tag_name: str):
        container = self.driver.find_element(by=By.XPATH, value= xpath_to_container)
        return list_of_links

    def scroll_page(self, items_to_scroll, no_of_scrtolls:int):
        self.driver.execute_script()

    def check_game_store(self):
        '''
        Finds and clicks the store button
        '''
        all_products = self.driver.find_element(By.LINK_TEXT,"STORE")
        time.sleep(5)
        all_products.click()
        time.sleep(10)
    
    def check_community(self):
        '''
        Finds and clicks the store button
        '''
        read_community = self.driver.find_element(By.LINK_TEXT,"COMMUNITY")
        time.sleep(5)
        read_community.click()
        time.sleep(10)
        
    def check_support(self):
        '''
        Finds and clicks the store button
        '''
        support_page = self.driver.find_element(By.LINK_TEXT,"SUPPORT")
        time.sleep(5)
        support_page.click()
        time.sleep(10)

    def create_uuids_for_url_list(self):
        url = self.get_urls()
        ig_urls = [i.rsplit('/', 2)[-2] for i in url]
        uuid_list = [str(uuid4()) for x in ig_urls]
        dic = [str(x[0]) + '--' + x[1] for x in zip(ig_urls, uuid_list)]
        url_list = {'Unique Code':dic, 'URL':url}
        df = pd.DataFrame(url_list)

        for column in df:
            s = df['URL'].values
        s = list(s)
        return s
    
    
        
    def __init__(self): 

       
        self.link_list = []
        self.image_list = []      
        self.url = "https://www.gog.com"
        service = Service(PATH)
        options = Options()

        #options.binary_location(r"C:\Program Files\LibreWolf\librewolf.exe")
    # options.headless = True 
        #defines the webdriver used
        #fp = webdriver.FirefoxProfile()
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options, service=service)
        self.driver.get(self.url)     
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        time.sleep(5)
        self.enable_cookies(self)


    def run(self):
        self.driver.get(self.url)
        pass
    

if __name__ == '__main__':
    webscraper = Scraper()