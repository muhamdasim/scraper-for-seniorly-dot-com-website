# import seniorly_scraper as scraper
#
#
# url='https://www.seniorly.com/assisted-living/washington/seattle/merrill-gardens-at-first-hill'
# url2='https://www.seniorly.com/assisted-living/washington/seattle/aegis-of-west-seattle'
#
#
#
#
# soup=scraper.pageRequests(url)
#
# print(scraper.getPageTitle(soup))
# print(scraper.getMetaDescription(soup))
# print(scraper.getCommunityName(soup))
# print(scraper.getCommunityStreetAddress(soup))
# print(scraper.getCommunityZipCode(soup))
# print(scraper.getCommunityState(soup))
# print(scraper.getImages(soup))
# print(scraper.getCommunityContent(soup))
def guest_list(guests):
	for i in guests:
		print("{} is {} years old and works as {}".format(i[0],i[1],[2]))
        

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])