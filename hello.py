from flask import Flask, render_template, request
import sys,os
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
        print 'depth : ', int(depth)
        #imageList = []
        if not website.endswith('/'):
            website = website + '/' 
        #print 'scrapy runspider flaskspider.py -a website=\'' + website + '\' -a depth=' + depth
        #os.system('scrapy runspider flaskspider.py -a website=\'' + website + '\' -a depth=' + depth)
        os.system('python crawler.py \'' + website + '\' ' + depth)
        return render_template('Results.html')
        # return "Crawling -------- "+website
    except Exception:
        e = sys.exc_info()[0]
        print e
    finally:
        # driver.quit()
        pass

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
