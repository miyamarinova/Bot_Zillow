import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import lxml

URL = "https://errorsandanswers.com/how-to-get-height-of-entire-document-with-javascript/"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
          }
FORM_URL = 'https://docs.google.com/forms/d/1uOXhIA54MRUSwoi7w8d-YpTfiZ7VLrR3v7fWDoddmHc/edit'


chrome_driver_path = "/Users/miyamarinova/Development/chromedriver.exe"

driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get(URL)
time.sleep(4)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(5)

driver.get(FORM_URL)
time.sleep(1)
address_input = driver.find_element(By.XPATH, "//*[@id='SchemaEditor']/div/div[2]/div/div[2]/div[3]/div[1]/div/div/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/input")
address_input.click()
address_input.send_keys("G.Benkovski")
time.sleep(4)
