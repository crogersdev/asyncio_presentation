#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import make_response
import random
from datetime import datetime
import time

app = Flask(__name__)

random.seed(1)

@app.route('/<number>')
def hello(number):
    n = datetime.now().isoformat()
    delay = random.randint(0, 3)
    time.sleep(delay)
    headers = { 'content_type': 'text/html', 'delay': str(delay) }

    with open('count_of_monte_cristo_full.html', 'rb') as html_body:
        print(f'{n}: {request.endpoint} delay: {delay}')
        resp = make_response(html_body.read())
        resp.headers = headers
        return resp

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)