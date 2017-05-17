#!/usr/bin/env python

from __future__ import print_function
from future import standard_library
standard_library.install_aliases()
import urllib.request, urllib.parse, urllib.error
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
    
open('https://github.com/giacomo1989/prova-import/blob/master/pizzaimport.json').read()
config = json.loads(open('https://github.com/giacomo1989/prova-import/blob/master/pizzaimport.json').read())



    #response = urllib.urlopen('https://github.com/giacomo1989/prova-import/blob/master/pizzaimport.json')
    #data = json.load(response) 
    
    # with open('pizzaimport.json') as data_file:    
    # data = json.load(data_file)
    

def processRequest(req):
	if req.get("result").get("action") == "Cost":
		result = req.get("result")
		pro = data.get("price")
		parameters = result.get("parameters")
		zone = parameters.get("pizza")
		cost = {'margherita':3.50, 
			'diavola':5.50, 
			'prosciutto and funghi':6.00, 
			'tonno and cipolla':6.90, 
			'capricciosa':5.50}
		speech = "la pizza " +zone+ " costa "+str(cost[zone])+ " euro "+config["price"] #pro #+ data.get["pizza"]["name"]
		res = makeWebhookResult(speech)
		return res
	
	else:
		return {}



def makeWebhookResult(speech):
    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data":[],
        # "contextOut": [],
        "source": "prueba"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
