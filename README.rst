===========================
README for hello_webcrawler
===========================

This is the brief documentation and starter kit for the hello web-crawler task.  It uses flask, a lightweight Python web framework.  The project contains two simple views and two simple unit tests.


Running the project
===================

Install Flask::

    pip install flask
    
Install Scrapy

    pip install Scrapy




Install Selenium:: (To run with selenium_crawler )
    
    pip install selenium==2.47
 
Note: Please Update Your Firefox Browser to latest version to work with the latest version of python selenum package.

Install pyvirtualdisplay::

    sudo apt-get install python-pip
    sudo apt-get install xvfb
    sudo pip install pyvirtualdisplay

Run the server::
  
To crawl using scrapy run the following  

    python hello.py
    
    (OR)
 
 To crawl using selenium run the following
    
    python selenium_crawler.py
    
Access the URL to see if the server is up::

    http://127.0.0.1:5000/

    Provide input url as http://www.bestwallpapers-hd.com and depth of your wish then click submit and wait to see the scraped images.

To run the unit tests::

    python hello_tests.py
    
    
    
