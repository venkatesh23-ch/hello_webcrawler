from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
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
    website = request.form['websiteUrl']
    # print website
    imageList = []
    browserDisplay = Display(visible=0)
    browserDisplay.start()
    driver = webdriver.Firefox()
    driver.get(website)
    for i in range(10):
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
            
        time.sleep(2)
        # img = urllib2.urlopen('http://bsomugshots.s3-website-us-east-1.amazonaws.com/607170.png').read().encode("base64").replace("\n","")
    driver.quit()     
    return render_template('crawlResults.html', imageList=imageList, message="Success!")
    # return "Crawling -------- "+website

if __name__ == '__main__':
    app.debug = True
    app.run()
