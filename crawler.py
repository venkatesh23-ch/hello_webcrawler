# -*- coding: utf-8 -*- 
import requests
#import re
import urlparse
import sys
from bs4 import BeautifulSoup

# link_re = re.compile(r'src="/web/wallpapers/*\.jpg$"')
def crawl(url, current_page):
    # Limit the recursion, we're not downloading the whole Internet
    if(current_page > depth):
        return
    
    print 'crawling page : '+str(current_page)
    # Get the webpage
    req = requests.get(url)
    
    # Check if successful
    if(req.status_code != 200):
        return []
    
    # print req.text
    # To get All the Images in page
    # links = link_re.findall(req.text)
    
    soup = BeautifulSoup(req.text)
    for image in soup.findAll('div', {'class':'box-main'})[1].findAll('img'):
        image_url = urlparse.urljoin(url, image.get('src').strip())
        # print image_url
        image_urls.append(image_url)
    #print images
    # print len(images)
    next_url = urlparse.urljoin(url, '/wallpapers/browse/' + str(current_page + 1) + '?order=publish-date-newest')
    #print next_url
    crawl(next_url, current_page + 1) 
   
depth = int(sys.argv[-1])
# print sys.argv[-3]  
url = sys.argv[-2]
image_urls = []
#url = urlparse.urljoin(url, '/wallpapers/browse/1?order=publish-date-newest')
crawl(url, 1)
filename = 'templates/Results.html'
#print image_urls  
with open(filename, 'wb') as f:
    for i in range(len(image_urls)):
        f.write('<img src="' + image_urls[i] + '"/>')
