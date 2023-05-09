from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

def pagesearch(url):
    driver = webdriver.Chrome()

    driver.get(url)
    try:
        address = driver.find_element(By.CLASS_NAME, "mapaddress").text
        if address == 'google maps':
            address = "navigate to page for address"
    except NoSuchElementException:
        address = "navigate to page for address"

    try:
        rms = driver.find_element(By.CLASS_NAME, "shared-line-bubble")
        rms = rms.find_elements(By.TAG_NAME, 'b')
        beds = rms[0]
        if address == 'google maps':
            address = "navigate to page for address"
    except NoSuchElementException:
        address = "navigate to page for address"

    driver.quit()

    

    return address