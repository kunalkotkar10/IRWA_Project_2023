from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
import re

def pagesearch(url):
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # driver = webdriver.Chrome(options = chrome_options)
    driver = webdriver.Chrome()

    price = "navigate to page for price"
    beds = None
    bath = None

    driver.get(url)
    try:
        address = driver.find_element(By.CLASS_NAME, "delivery-address").text
    except NoSuchElementException:
        address = "navigate to page for address"

    listings = driver.find_elements(By.CLASS_NAME, "pricingGridItem multiFamily ")

    for i, ele in enumerate(listings):
        try:
            price = ele.find_elements(By.CLASS_NAME, "rentLabel")
            if len(price) > 0:
                price = price[0].text.split()
                price = re.sub(r'[^\d.]', '', price[0])
        except:
            price = ele.find_elements(By.CLASS_NAME, "rentLabel")
            if len(price) > 0:
                price = price[0].text.split()
                price = re.sub(r'[^\d.]', '', price[0])
        try:
            rms = ele.find_element(By.CLASS_NAME, "detailsTextWrapper")
            rms = rms.find_elements(By.TAG_NAME, 'span')
            if len(rms) > 0:
                beds = rms[0].text.split()[0]
                bath = rms[1].text.split()[0]
        except NoSuchElementException:
            pass

    driver.quit()

    if address == 'google maps':
        address = "navigate to page for address"

    return beds, bath, address, price