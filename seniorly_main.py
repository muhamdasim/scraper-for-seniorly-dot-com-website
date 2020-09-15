import seniorly_scraper as scraper


url='https://www.seniorly.com/assisted-living/washington/seattle/merrill-gardens-at-first-hill'
url2='https://www.seniorly.com/assisted-living/washington/seattle/aegis-of-west-seattle'




soup=scraper.pageRequests(url)

print(scraper.getPageTitle(soup))
print(scraper.getMetaDescription(soup))
print(scraper.getCommunityName(soup))
print(scraper.getCommunityStreetAddress(soup))
print(scraper.getCommunityZipCode(soup))
print(scraper.getCommunityState(soup))
print(scraper.getCommunityCity(soup))
scraper.getImages(soup)