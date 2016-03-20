# -*- coding: utf-8 -*-
import scrapy
import smtplib
#houscraper in the following "from...import..." refers to the project folder name
from houscraper.items import HouscraperItem

class MovieScraperSpider(scrapy.Spider):
    name = "Houscraper"
    allowed_domains = ["www.dygod.net"]
    start_urls = [
        "http://www.dygod.net",
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]
    

    def parse(self, response):
        #filename = response.url.split("/")[-2] + '.html'
        #with open(filename, 'wb') as f:
            #f.write(response.body)
        sender = 'chao.bian@hotmail.com'
        receivers = ['cbian@mit.edu']
        for sel in response.xpath('//div[@class="co_content8"]/ul/table/tr/td'):
            item = HouscraperItem()
            item['title'] = sel.xpath('a/text()').extract()
            
            if item['title']: 
                movie = item['title'].pop()
                print unicode(movie)
                if movie.find(u"老炮儿") != -1:
                    print "found"
                    smtpObj = smtplib.SMTP('smtp.live.com', 25)
                    smtpObj.ehlo() 
                    smtpObj.starttls() 
                    smtpObj.ehlo() 
                    smtpObj.login(sender, "Bcyx10020719!") 
                    smtpObj.sendmail(sender, receivers, "found")         
                    print "Successfully sent email"
                else:
                    print "not found"