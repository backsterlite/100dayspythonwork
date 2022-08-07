from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_service = Service(executable_path='/home/backster/Apps/chromedriver_linux64/chromedriver')
driver = webdriver.Chrome(service=chrome_service)

driver.get('http://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.NAME, 'fName')
last_name = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')

submit = driver.find_element(By.CSS_SELECTOR, 'form button[type=submit]')

first_name.send_keys('Evan')
last_name.send_keys('Backster')
email.send_keys('backstercorp@gmail.com')

submit.click()




