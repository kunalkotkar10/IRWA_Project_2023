from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

from CLPageSearch import pagesearch

def CLSearch():
    # Set up the WebDriver
    driver = webdriver.Chrome()

    # Navigate to the apartments.com website
    driver.get("https://baltimore.craigslist.org/search/apa")

    # Find the search bar and enter the location you want to search for
    search_box = driver.find_element(By.CLASS_NAME, "cl-query-bar")
    search_bar = search_box.find_element(By.TAG_NAME, 'input')
    search_bar.send_keys("charles village")
    search_bar.send_keys(Keys.RETURN)


    # # Find the search button and click it
    # search_button = driver.find_element(By.Title, "search-submit-button")
    # search_button.click()

    # Wait for the search results to load
    #wait = WebDriverWait(driver, 10)
    #wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "placardBanner")))
    import time
    time.sleep(10)

    # Print out the names of the apartments
    listings = driver.find_elements(By.CLASS_NAME, "gallery-card")

    results = []

    for ele in listings:
        try:
            listing = ele.find_element(By.CLASS_NAME, "titlestring")
            name = listing.text
            link = listing.get_attribute("href")
            address = pagesearch(link)
            price = ele.find_element(By.CLASS_NAME, "priceinfo").text
        except StaleElementReferenceException:
            # Retry the element lookup in case of StaleElementReferenceException
            listing = ele.find_element(By.CLASS_NAME, "titlestring")
            name = listing.text
            link = listing.get_attribute("href")
            address = pagesearch(link)
            price = ele.find_element(By.CLASS_NAME, "priceinfo").text
        print(name, '|', address, '|', link, '|', price)
        results.append((name, address, link, price))
        
    print("done - craigslist.org")
    #print(str(results[i])+"\n" for i in range(len(results)))

    # Close the browser
    input()
    driver.quit()
    
    return results

