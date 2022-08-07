from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_service = Service(executable_path='/home/backster/Apps/chromedriver_linux64/chromedriver')
driver = Chrome(service=chrome_service)

driver.get('https://linkedin.com')
time.sleep(3)
sign_in = driver.find_element(By.LINK_TEXT, 'Sign in')
sign_in.click()
username_field = driver.find_element(By.ID, 'username')
password_field = driver.find_element(By.ID, 'password')
submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type=submit]')

username_field.send_keys('backstercorp@gmail.com')
password_field.send_keys('kapr1zofgods')
submit_button.click()

# driver.close()