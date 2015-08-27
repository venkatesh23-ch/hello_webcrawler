from flask import Flask
app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome!'


@app.route('/hello')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
