import requests
import bs4
import re
import json
import pandas as pd



def listToString(s):
    # initialize an empty string
    str1 =''

    # return string
    for i in s:
        str1+=i+', '

    return str1[:-2]

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
    dt=[]
    for i in soup.findAll(class_='ResponsiveImage__ResponsiveWrapper-l4g8bp-0 jscNWe'):
        dt.append(i.find('img').get('data-src'))

    if not dt:
        return -1
    else:
        return listToString(dt)

def getCommunityContent(soup):
    try:
        return soup.find(class_='CollapsibleBlock__BlockCap-s326rf-1 jhhVKz').get_text().strip()
    except:
        return -1
def getCareTypesProvided(soup):
    try:
        dt=[]
        for i in soup.find(class_='CommunityCareService__Wrapper-sc-1uu6i2h-0 bDIQtl').findAll(class_='Root-sc-1m9vk1w-0 gCatle Block-sc-1184las-0 IconItem__Wrapper-sc-155qj67-0 ivNDcb'):
            dt.append(i.find(class_='Root-sc-1m9vk1w-0 gCatle Block-sc-1184las-0 jqgkYL').get_text().strip())



        return listToString(dt)

    except:
        return  -1


def getAmenitiesProvided(soup):
    try:
        dt=[]
        for i in soup.find(class_='CommunityAmenities__Wrapper-sc-1gihmpf-0 RJvAA').findAll(class_='Root-sc-1m9vk1w-0 gCatle Block-sc-1184las-0 IconItem__Wrapper-sc-155qj67-0 ivNDcb'):
            dt.append(i.find(class_='Root-sc-1m9vk1w-0 gCatle Block-sc-1184las-0 jqgkYL').get_text().strip())



        return listToString(dt)

    except:
        return -1


def getPricingStartsFrom(soup):
    try:
        return soup.find(class_='Span-vzvmw4-0 jYbTJi').get_text().strip()
    except:
        return -1

def getPricingByRoomType(soup):
    try:
        dt=[]
        for i in soup.find(class_='CommunityPricingTable__StyledTable-r1omm4-4 lbwBwC').findAll('tr'):
            for k in i.findAll('td'):
                dt.append(k.get_text())


        dt.remove('Type')
        dt.remove('Average Monthly Cost*')

        return listToString(dt)

    except:
        return -1

