# coding: utf-8

from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/test/')
def test_page():
    return 'This is a test_page'

if __name__ == '__main__':
    app.run()