from flask import Flask, render_template, request
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
    return render_template('crawlResults.html', name=website)
    # return "Crawling -------- "+website

if __name__ == '__main__':
    app.debug = True
    app.run()
