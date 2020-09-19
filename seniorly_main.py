import seniorly_scraper as scraper

urls=[]

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

for i in urls:
    try:
        soup=scraper.pageRequests(i)
        ad=scraper.getCommunityStreetAddress(soup)
        communityStreetAddres.append(ad)
        pageTitle.append(scraper.getPageTitle(soup))
        metaDescription.append(scraper.getMetaDescription(soup))
        communityName.append(scraper.getCommunityName(soup))
        communityZipCode.append(scraper.getCommunityZipCode(soup))
        communityState.append(scraper.getCommunityState(soup))
        images.append(scraper.getImages(soup))
        content.append(scraper.getCommunityContent(soup))
        careTypesProvided.append(scraper.getCareTypesProvided(soup))
        AmenitiesProvided.append(scraper.getAmenitiesProvided(soup))
        pricingStartsFrom.append(scraper.getPricingStartsFrom(soup))
        pricingByRoomType.append(scraper.getPricingByRoomType(soup))
    except:
        continue