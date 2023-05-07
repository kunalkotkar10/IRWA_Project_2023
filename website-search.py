from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the apartments.com website
driver.get("https://www.apartments.com/search/")

# Find the search bar and enter the location you want to search for
search_bar = driver.find_element(By.ID, "searchBarLookup")
search_bar.send_keys("charles village")
search_bar.send_keys(Keys.RETURN)


# # Find the search button and click it
# search_button = driver.find_element(By.Title, "search-submit-button")
# search_button.click()

# Wait for the search results to load
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "placardTitle")))

# Print out the names of the apartments
apartment_names = driver.find_elements(By.CLASS_NAME, "placardTitle")
for name in apartment_names:
    print(name.text)

# Close the browser
# input()
driver.quit()