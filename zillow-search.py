from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException



# Set up the WebDriver
driver = webdriver.Chrome()

driver.get("https://www.zillow.com/homes/for_rent/")

# Find the search bar and enter the location you want to search for
search_box = driver.find_element(By.ID, "srp-search-box")
search_bar = search_box.find_element(By.TAG_NAME, 'input')
search_bar.send_keys("charles village")
search_bar.send_keys(Keys.RETURN)

import time
time.sleep(10)

# Print out the names of the apartments
listings = driver.find_elements(By.CLASS_NAME, "ListItem-c11n-8-85-1__sc-10e22w8-0 srp__sc-wtsrtn-0 jhnswL")

results = []

for ele in listings:
    try:
        listing = ele.find_element(By.CLASS_NAME, "StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0 gdfTyO property-card-link")
        #name = listing.get_attribute("aria-label")
        name = driver.find_elements_by_tag_name("address")
        name = name[0]
        link = listing.get_attribute("href")
        try:
            price = ele.find_element(By.CLASS_NAME, "property-pricing").text
        except NoSuchElementException:
            try:
                price = ele.find_element(By.CLASS_NAME, "property-rents").text
            except:
                price = ele.find_element(By.CLASS_NAME, "price-range").text
        #print(name, "|", link, "|", price)
    except StaleElementReferenceException:
        # Retry the element lookup in case of StaleElementReferenceException
        listing = ele.find_element(By.CLASS_NAME, "StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0 gdfTyO property-card-link")
        #name = listing.get_attribute("aria-label")
        name = driver.find_elements_by_tag_name("address")
        name = name[0]
        link = listing.get_attribute("href")
        try:
            price = ele.find_element(By.CLASS_NAME, "property-pricing").text
        except NoSuchElementException:
            try:
                price = ele.find_element(By.CLASS_NAME, "property-rents").text
            except:
                price = ele.find_element(By.CLASS_NAME, "price-range").text
        #print(name, "|", link, "|", price)
    results.append((name, link, price))
    

print("done - apartments.com")

# Close the browser
input()
driver.quit()


