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

    # # print(craigslist)
    # # print(apts)

    df = pd.DataFrame(combined, columns=['name', 'link', 'price', 'beds', 'bath'])
    # print(df)
    # df = pd.DataFrame({'name': ['mike','danny'], 'link': ['link1','link2'], 'price': [34,48], 'beds': [2,4], 'bath': [2,3]})
    df.to_csv('dataframe/apartments.csv', index=False)
    print('csv saved')
    print('Dataframe: ')
    print(df)
    return df

def get_sortedData(sort_type):
    df = pd.read_csv('dataframe/apartments.csv')
    if sort_type == '1':
        df = df.sort_values('price', ascending=True)
        return df
    elif sort_type == '2':
        df = df.sort_values('price', ascending=False)
        return df
    elif sort_type == '3':
        return df.sort_values('beds', ascending=True)
    elif sort_type == '4':
        return df.sort_values('beds', ascending=False)
    elif sort_type == '5':
        return df.sort_values('bath', ascending=True)
    else:
        return df.sort_values('bath', ascending=False)

# print(get_data('charles village').sort_values('price', ascending=False))