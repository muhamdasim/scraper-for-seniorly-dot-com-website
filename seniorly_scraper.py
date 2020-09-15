import requests
import bs4
import re
import json
import pandas as pd



def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))

def pageRequests(url):
    r=requests.get(url)
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    return soup

def getPageTitle(soup):
    return soup.title.string.strip()

def getMetaDescription(soup):
    meta = soup.find_all('meta')
    return listToString([meta.attrs['content'] for meta in meta if 'name' in meta.attrs and meta.attrs['name'] == 'description'])

def getCommunityName(soup):
    return soup.find(class_='Root__H1-sc-1lnoi1-0 iCGCDp Root-sc-1lnoi1-4 eaYBkV Heading-p8la3x-0 irVoEB').get_text().strip()

def getCommunityStreetAddress(soup):
    return soup.find(class_='Root__H2-sc-1lnoi1-1 eaHtqb Root-sc-1lnoi1-4 jBwoEe Heading-p8la3x-0 irVoEB').get_text().strip()

def getCommunityZipCode(soup):
    data=soup.find(class_='Root__H2-sc-1lnoi1-1 eaHtqb Root-sc-1lnoi1-4 jBwoEe Heading-p8la3x-0 irVoEB').get_text().strip()
    return re.sub("[^\w]", " ", data).split()[-1]


    return city
def getCommunityState(soup):
    data = soup.find(
        class_='Root__H2-sc-1lnoi1-1 eaHtqb Root-sc-1lnoi1-4 jBwoEe Heading-p8la3x-0 irVoEB').get_text().strip()
    state= ''

    return re.sub("[^\w]", " ", data).split()[-2]

def getCommunityCity(soup):
    data = soup.find(
        class_='Root__H2-sc-1lnoi1-1 eaHtqb Root-sc-1lnoi1-4 jBwoEe Heading-p8la3x-0 irVoEB').get_text().strip()
    state = ''

    return re.sub("[^\w]", " ", data).split()[-3]

def getImages(soup):
    print(soup.find(class_='ResponsiveImage__ResponsiveWrapper-l4g8bp-0 jscNWe').get('href'))