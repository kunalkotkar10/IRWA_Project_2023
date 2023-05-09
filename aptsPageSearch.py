from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.chrome.options import Options

def pagesearch(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options = chrome_options)

    driver.get(url)
    try:
        address = driver.find_element(By.CLASS_NAME, "mapaddress").text
    except NoSuchElementException:
        address = "navigate to page for address"

    driver.quit()

    if address == 'google maps':
        address = "navigate to page for address"

    return address