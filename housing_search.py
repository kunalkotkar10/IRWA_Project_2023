from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd

from CLSearch import CLSearch
from aptsSearch import aptsSearch

def get_data(text):
    craigslist = CLSearch(text)
    apts = aptsSearch(text)
    combined = craigslist + apts

    print(craigslist)
    print(apts)

    df = pd.DataFrame(combined, columns=['name', 'link', 'price', 'beds', 'bath'])

    return df

print(get_data('charles village').sort_values('price', ascending=False))