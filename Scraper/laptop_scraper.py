from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from laptop_parser import ParseData
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.vijaysales.com/c/laptops-and-accessories?categories=Laptops")
time.sleep(2)
all_dfs = []

wait = WebDriverWait(driver, 10)

for i in range(1, 17):
    element = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="vscontainer-80b71eee22"]/div[1]/div[2]/div[4]/div[3]/ul/li[{i}]')))
    driver.execute_script("arguments[0].click();", element)
    time.sleep(2)
    html = driver.page_source
    df = ParseData().parse_data(html)
    all_dfs.append(df)

final_df = pd.concat(all_dfs, ignore_index=True)
final_df.to_csv('laptops.csv', index=False)




# with open(r'C:/Users/Himanshu/OneDrive/Documents/my documents/python course/Python_Projects/Laptop-Price-Predictor/Scraper/vijaysales.html', 'w', encoding='utf-8') as f:
#     f.write(html)


driver.quit()
