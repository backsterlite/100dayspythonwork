import time
from urllib.request import urlopen
import requests

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re

from bs4 import BeautifulSoup
# city_name = input('Enter the city name [ex. San Francisco, CA]: ')
G_Form_link = 'https://docs.google.com/forms/d/e/1FAIpQLSc1nUPcxG4exOVjUGJlsNa7BTcJrazleHCcmbJlkRV2LEqGLQ/viewform?usp=sf_link'
zillow_url = 'https://www.zillow.com/'
# ser = Service(executable_path='/home/backster/Apps/chromedriver_linux64/chromedriver')
# driver = Chrome(service=ser)

# NOT WORKING RECAPCHA
# city_name = re.sub(r'[\s | ,]', '-', city_name).lower()
# driver.get(f"{zillow_url}")
# driver.execute_script(f' return document.querySelector("div#srp-search-box input").value = "{city_name}";')
# driver.find_element(By.CSS_SELECTOR, 'div#srp-search-box button[type=submit]').click()
#
# time.sleep(1.5)
# driver.find_element(By.ID, 'listing-type').click()
# driver.find_element(By.ID, 'isForRent').click()
# driver.find_element(By.ID, 'price').click()
# price = driver.find_element(By.ID, 'price-exposed-max')
# price.send_keys(3000)
# driver.find_element(By.CSS_SELECTOR, 'li#max-3000 button').click()
#
# rents = []


header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(
    "https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
    headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

links_list = []
prices_list = []
addresses_list = []
addresses = soup.select('.list-card-top ')
for addr in addresses:
    print(addr.text)
