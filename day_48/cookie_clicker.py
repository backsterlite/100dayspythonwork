from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time
import random
import threading
driver = None
def init_driver():
    chrome_service = Service(executable_path='/home/backster/Apps/chromedriver_linux64/chromedriver')
    driver = webdriver.Chrome(service=chrome_service)
    driver.get('https://orteil.dashnet.org/cookieclicker/')
    products = []
    time.sleep(3)
    language = driver.find_element(By.ID, 'langSelect-EN')
    language.click()
    time.sleep(3)
    for id in range(19):
        product = driver.find_element(By.ID, f"product{id}")
        print(type(product))
        products.append(product)

    cookies_obj = driver.find_element(By.ID, 'cookies')

    cookie_button = driver.find_element(By.CSS_SELECTOR, 'button#bigCookie')

    start_time = round(time.time())
    while True:
        cookie_button.click()
        curr_time = round(time.time())
        if (curr_time - start_time) % 10 == 0:
            for product in products[::-1]:
                if hasClass(product, 'enabled'):
                    product.click()


th = threading.Thread(target=init_driver)
th.start()

def hasClass(element: WebElement, need: str) -> bool:
    classList = element.get_attribute('class').split()
    return need in classList


