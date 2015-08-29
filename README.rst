===========================
README for hello_webcrawler
===========================

This is the brief documentation and starter kit for the hello web-crawler task.  It uses flask, a lightweight Python web framework.  The project contains two simple views and two simple unit tests.


Running the project
===================

Install Flask::

    pip install flask

Install Selenium:: 
    
    pip install selenium==2.47
 
Note: Please Update Your Firefox Browser to latest version to work with the latest version of python selenum package.

Install pyvirtualdisplay::

    sudo apt-get install python-pip
    sudo apt-get install xvfb
    sudo pip install pyvirtualdisplay

Run the server::

    python hello.py

Access the URL to see if the server is up::

    http://127.0.0.1:5000/

To run the unit tests::

    python hello_tests.py
    
    Provide input as http://bso.sun-sentinel.com then click submit and wait for 2 to 3 minutes to see the scraped images.
    
