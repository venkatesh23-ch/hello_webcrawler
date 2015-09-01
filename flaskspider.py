import scrapy
from scrapy.http import FormRequest 
import sys
class FlaskSpider(scrapy.Spider):
    name = 'flaskspider'
    start_urls = []
    count = 0
    image_urls = [] 
    depth = 0
    def __init__(self, category=None, *args, **kwargs):
        # print 'init method'
        self.depth = int(sys.argv[-1].split('=')[-1].strip())
        #print sys.argv[-3]  
        self.start_urls = [sys.argv[-3].split('=')[-1].strip()]
    def parse(self, response):
        print 'depth : ', self.depth
        count = self.count 
        self.count += 1
        current_page = self.count
        print 'current_page : ', current_page
        if current_page < self.depth:
            next_link = '' 
                # print response.selector.xpath('//*[@id="mugnav"]/a/@onclick').extract()
            if count:
                next_link = response.selector.xpath('//*[@id="mugnav"]/a[2]/@onclick').extract()[0]
            else: 
                # print response.selector.xpath('//*[@id="mugnav"]/a/@onclick').extract()
                image = response.url + response.selector.xpath('//*[@id="dropzone"]/div[1]/article/img/@src').extract()[0] 
                print image
                self.image_urls.append(image)
                next_link = response.selector.xpath('//*[@id="mugnav"]/a/@onclick').extract()[0]
            next_link = next_link.split('(')[-1] 
            next_link = next_link.replace(';', '').replace(')', '').strip()
            # print 'next_link : ',next_link
            #if current_page < self.depth:
            next_image = 'http://bso.sun-sentinel.com/mugshots/' + next_link + '.png'
            print next_image
            self.image_urls.append(next_image)
            yield FormRequest('http://bso.sun-sentinel.com/index.php', callback=self.parse, formdata={'paginate':next_link})
        else: 
            print "Completed"
            filename = 'templates/Results.html'
            image_urls = self.image_urls
            print image_urls  
            with open(filename, 'wb') as f:
                for i in range(len(image_urls)):
                    f.write('<img src="' + image_urls[i] + '"/>')
