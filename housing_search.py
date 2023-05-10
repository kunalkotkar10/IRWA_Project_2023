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
        print('Ascending Price')
        return df
    elif sort_type == '2':
        df = df.sort_values('price', ascending=False)
        print('Descending Price')
        return df
    elif sort_type == '3':
        df = df.sort_values('beds', ascending=True)
        print('Ascending Beds')
        return df
    elif sort_type == '4':
        df = df.sort_values('beds', ascending=False)
        print('Descending Beds')
        return df
    elif sort_type == '5':
        df = df.sort_values('bath', ascending=True)
        print('Ascending Baths')
        return df
    else:
        df = df.sort_values('bath', ascending=False)
        print('Descending Baths')
        return df

# print(get_data('charles village').sort_values('price', ascending=False))