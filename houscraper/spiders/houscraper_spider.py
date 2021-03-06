# -*- coding: utf-8 -*-
import scrapy
import smtplib
#houscraper in the following "from...import..." refers to the project folder name
from houscraper.items import HouscraperItem

class MovieScraperSpider(scrapy.Spider):
    name = "Houscraper"
    allowed_domains = ["www.remax.ca"]
    start_urls = [
        #"http://www.dygod.net",
        "http://www.remax.ca/on/toronto-real-estate/#queryText=Toronto,+on&minPrice=250000&coordinatesFor=Toronto,+ON&mode=Box&province=ON&cityName=Toronto&zoom=10&south=43.24541188674621&west=-80.22315216064455&north=44.06016562961736&east=-78.54224395751955&maxPrice=700000&mainlist.listingPageSize=100&mainlist.groupByCities=true&listingtab.index=0&minBedroomNumber=3&propertyTypeIds=20,50&showTypeIds=&minBathroomNumber=&minSquareFeet=&maxSquareFeet=&minLotSize=&maxLotSize=&minWalkScore=0&maxWalkScore=100&minTransitScore=0&maxTransitScore=100&minFee=0&maxFee=&mainlist.listingPage=1",
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]
    

    def parse(self, response):
        #filename = response.url.split("/")[-2] + '.html'
        #with open(filename, 'wb') as f:
            #f.write(response.body)
        sender = 'chao.bian@hotmail.com'
        receivers = ['baobeituzi1002@hotmail.com']
        #for sel in response.xpath('//div[@class="co_content8"]/ul/table/tr/td'):
        for sel in response.xpath('//div[contains(@class, "draggableListingItem teaser padding16")]/ul/li[@class="propertyPrice"]'):    
            item = HouscraperItem()
            item['price'] = sel.xpath('a/text()').extract()
            if item['price']:
                  price = item['price'].pop()
                  print unicode(price)
                  print "found"
                  smtpObj = smtplib.SMTP('smtp.live.com', 25)
                  smtpObj.ehlo() 
                  smtpObj.starttls() 
                  smtpObj.ehlo() 
                  smtpObj.login(sender, "Bcyx10020719!") 
                  smtpObj.sendmail(sender, receivers, "found price: " + unicode(price))         
                  print "Successfully sent email"
                  break
##            if item['title']: 
##                movie = item['title'].pop()
##                print unicode(movie)
##                if movie.find(u"老炮儿") != -1:
##                    print "found"
##                    smtpObj = smtplib.SMTP('smtp.live.com', 25)
##                    smtpObj.ehlo() 
##                    smtpObj.starttls() 
##                    smtpObj.ehlo() 
##                    smtpObj.login(sender, "Bcyx10020719!") 
##                    smtpObj.sendmail(sender, receivers, "found")         
##                    print "Successfully sent email"
##                else:
##                    print "not found"
