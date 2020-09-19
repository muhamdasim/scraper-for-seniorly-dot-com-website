import seniorly_scraper as scraper
import pandas as pd
import csv
urls=[]
df=pd.read_csv('urls.csv')

for i in df['urls']:
    urls.append(i)


pageTitle=[]
metaDescription=[]
communityName=[]
communityStreetAddres=[]
communityZipCode=[]
communityState=[]
images=[]
content=[]
careTypesProvided=[]
AmenitiesProvided=[]
pricingStartsFrom=[]
pricingByRoomType=[]


def save():
    with open("sample.csv", "w", newline='', encoding="utf-8") as csvFile:
        fieldnames = ['pageTitle', 'metaDescription', 'communityName','communityStreetAddress','communityZipCode','communityState',
        'images','content','careTypes','Amenities','pricingStartsFrom','pricingByRoomType']
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        writer.writeheader()
        for h, d, c in zip(pageTitle,metaDescription,communityName,communityStreetAddres,communityZipCode,communityState
                           ,images,content,careTypesProvided,AmenitiesProvided,pricingStartsFrom,pricingByRoomType):
            writer.writerow({'pageTitle':pageTitle, 'metaDescription':metaDescription, 'communityName':communityName,'communityStreetAddress':communityStreetAddres,'communityZipCode':communityZipCode,'communityState':communityState,
        'images':images,'content':content,'careTypes':careTypesProvided,'Amenities':AmenitiesProvided,'pricingStartsFrom':pricingStartsFrom,'pricingByRoomType':pricingByRoomType})


counter=0

for i in urls:

        print("Scraping No:",counter,i)
        soup=scraper.pageRequests(i)
        ad=scraper.getCommunityStreetAddress(soup)
        communityStreetAddres.append(ad)
        pageTitle.append(scraper.getPageTitle(soup))
        metaDescription.append(scraper.getMetaDescription(soup))
        communityName.append(scraper.getCommunityName(soup))
        communityZipCode.append(scraper.getCommunityZipCode(soup))
        communityState.append(scraper.getCommunityState(soup))
        images.append(scraper.getImages(soup))
        #content.append(scraper.getCommunityContent(soup))
        careTypesProvided.append(scraper.getCareTypesProvided(soup))
        AmenitiesProvided.append(scraper.getAmenitiesProvided(soup))
        pricingStartsFrom.append(scraper.getPricingStartsFrom(soup))
        pricingByRoomType.append(scraper.getPricingByRoomType(soup))
        counter+=1
        save()





