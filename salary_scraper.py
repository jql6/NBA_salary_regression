"""
Python script for scraping player salaries from HoopsHype.

Title: HoopsHype Salary Scraper
Author: Jackie Lu
Date: 2021, Apr. 02

Instructions:
```{bash}
cd /Users/Jackie/Documents/Coding/GitHub/NBA_salary_regression;\
conda activate PS5_bot;\

```
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import json
from time import sleep

class HHPS_Bot():
    def __init__(self):
        # Replace the string with your path to the chromedriver you downloaded
        self.driver = webdriver.Chrome("./chromedriver")

    def go_to_homepage(self):
        self.driver.get('https://hoopshype.com/salaries/players/')
        
    # See if we can enter javascript code into the console
    def download_salary_report(self):
        # Wait for table to load
        sleep(2)
        
        # Scrape the table into a csv file
        # Find the table
        report = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div[4]/div[2]/div[1]/div/div[1]/div/div[3]/div[2]/table'
            ).find_element_by_tag_name("tbody")
        
        report_header = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div[4]/div[2]/div[1]/div/div[1]/div/div[3]/div[2]/table'
            ).find_element_by_tag_name("thead")
        
        # Create the csv file
        with open('./data/NBA_player_salaries.csv', 'w', newline='') as csvfile:
            wr = csv.writer(csvfile)
            # Write header
            wr.writerow(
                [d.text for d in report_header.find_elements_by_css_selector('td')][0: ]
                )
            for i, row in enumerate(
                # Find the table rows
                report.find_elements_by_css_selector('tr')
                ):
                # Write the table contents
                wr.writerow(
                    [d.text for d in row.find_elements_by_css_selector('td')][0:])
        
        
# Bot commands
bot = HHPS_Bot()
bot.go_to_homepage()
bot.download_salary_report()