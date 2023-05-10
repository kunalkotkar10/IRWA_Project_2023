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
        address = address.replace(",", "")
    except NoSuchElementException:
        address = "navigate to page for address"

    if address.startswith('google'):
        address = "navigate to page for address"
    
    #listings = driver.find_elements(By.CLASS_NAME, "pricingGridItem multiFamily ")
    try:
        listings = driver.find_element(By.ID, "pricingView")
    except StaleElementReferenceException:
        listings = driver.find_element(By.ID, "pricingView")
    
    rents = listings.find_elements(By.CLASS_NAME, "rentLabel")
    rms = listings.find_elements(By.CLASS_NAME, "detailsLabel")
    
    results = []
    for i in range(len(rms)):
        if len(rents[i].text) > 0:
            price = rents[i].text.split()
            price = re.sub(r'[^\d.]', '', price[0])
            price = int(price)
        else:
            break
        
        if len(rms[i].text) > 0:
            rm = rms[i].find_elements(By.TAG_NAME, 'span')
            if len(rm) > 0:
                beds = rm[0].text.split()[0]
                bath = rm[1].text.split()[0]
        name = beds + 'BR/' + bath + 'Ba unit at ' + address
        results.append((name, url, price, beds, bath))


    '''
    #listings = driver.find_elements(By.CLASS_NAME, "pricingGridItem multiFamily ")

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
                price = int(price)
        try:
            rms = ele.find_element(By.CLASS_NAME, "detailsTextWrapper")
            rms = rms.find_elements(By.TAG_NAME, 'span')
            if len(rms) > 0:
                beds = rms[0].text.split()[0]
                bath = rms[1].text.split()[0]
        except NoSuchElementException:
            pass
    '''

    driver.quit()

    

    return results