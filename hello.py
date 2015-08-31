from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from selenium import webdriver
import sys
from pyvirtualdisplay import Display

app = Flask(__name__)


@app.route('/')
def welcome():
    # return 'Welcome!'
    return render_template('index.html')

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route("/crawl", methods=['POST'])
def crawl():
    try:
        website = request.form['websiteUrl']
        depth = request.form['depth']
        #print 'depth : ',int(depth)
        imageList = []
        browserDisplay = Display(visible=0)
        browserDisplay.start()
        driver = webdriver.Firefox()
        driver.implicitly_wait(1)
        driver.get(website)
        for i in range(int(depth)):
            soup = BeautifulSoup(driver.page_source)
            #print soup.findAll('img')
            if i:
                img = soup.findAll('img')[2].get('src')
            else:
                img = soup.findAll('img')[1].get('src')
            if website.endswith('/'):
                img = website + img
            else:
                img = website + '/' + img
            # print img
            imageList.append(img)
            if i :
                driver.find_element_by_xpath('//*[@id="mugnav"]/a[2]/img').click()
            else:
                driver.find_element_by_xpath('//*[@id="mugnav"]/a/img').click()
                
            # img = urllib2.urlopen('http://bsomugshots.s3-website-us-east-1.amazonaws.com/607170.png').read().encode("base64").replace("\n","")
        return render_template('crawlResults.html', imageList=imageList, message="Success!")
        # return "Crawling -------- "+website
    except Exception:
        e = sys.exc_info()[0]
        print e
    finally:
        driver.quit()

if __name__ == '__main__':
    app.debug = True
    app.run(port=8000)
