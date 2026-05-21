from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.vijaysales.com/c/laptops-and-accessories?categories=Laptops")
time.sleep(2)

html = driver.page_source

with open(r'C:/Users/Himanshu/OneDrive/Documents/my documents/python course/Python_Projects/Laptop-Price-Predictor/Scraper/vijaysales.html', 'w', encoding='utf-8') as f:
    f.write(html)


driver.quit()
