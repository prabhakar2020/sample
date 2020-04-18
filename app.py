from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import Flask, make_response, request
import json
import sqlite3 as sq


# A very simple Flask Hello World app for you to get started with...

from flask import Flask, make_response, request
import json
import sqlite3 as sq

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'
@app.route("/webhook",methods = ['POST'])
def webhook():
    if request.method == 'POST':
        req = request.get_json(silent=True, force=True)
        print ("#"*50)
        print (req)
        res = processRequest(req)
        res = json.dumps(res, indent=4)
        r = make_response(res)
        r.headers["Content-Type"] = 'application/json'
        return r

def processRequest(req):
    query_response = req.get("queryResult",{})

    # queryText = query_response.get('queryText','')
    parameters = query_response.get('parameters','')
    speech = "Sorry, I didn't understand what you are saying"
    if parameters:
        speech = "Hi," +str(parameters.get("name",''))+" glad to meet you"
    return {
        "fulfillmentText": speech
        }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    app.run(debug=False, port=port, host='0.0.0.0')
