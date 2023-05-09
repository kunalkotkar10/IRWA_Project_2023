from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
# from pyvirtualdisplay import Display


def get_data(request):
# Set up the WebDriver
    # display = Display(visible=0, size=(800, 600))
    # display.start()
    driver = webdriver.Chrome()
    # driver = webdriver.PhantomJS()

    # Navigate to the apartments.com website
    driver.get("https://www.apartments.com/search/")
    # driver.get('https://www.zillow.com/homes/for_rent/')

    # Find the search bar and enter the location you want to search for
    search_bar = driver.find_element(By.ID, "searchBarLookup")
    # search_box = driver.find_element(By.ID, 'srp-search-box')
    # search_bar = search_box.find_element(By.TAG_NAME, 'input')

    search_bar.send_keys(request)
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
    listings = driver.find_elements(By.CLASS_NAME, "property-info")

    results = []

    for ele in listings:
        try:
            listing = ele.find_element(By.CLASS_NAME, "property-link")
            name = listing.get_attribute("aria-label")
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
            listing = ele.find_element(By.CLASS_NAME, "property-link")
            name = listing.get_attribute("aria-label")
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
        # apts = {"Name":[],"Link":[],"Price":[]}

        # apts["Name"].append(name)
        # apts["Link"].append(link)
        # apts["Price"].append(price)	
        

    print("done")
    # print(results)

    # Close the browser
    # input()
    driver.quit()
    # print(apts)
    # display.stop()
    return results
