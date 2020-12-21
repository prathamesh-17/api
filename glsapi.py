# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 23:31:54 2020

@author: DNDLPBhosale
"""

from flask import Flask, Response

 

data_dict = {}

 

def main():
   
    import json
    app = Flask(__name__)

 

    @app.route('/api/licenseDetails/<id>')
    def getLicenseByCustomerId(id):
        dict = {"customerId":id, "product": [
            {"productId":1000, "feature":["feature1", "feature2"]},
            {"productId":2000, "feature":["feature1"]}]
            }
    
        newresponse = Response(json.dumps(dict), mimetype="application/json")
        newresponse.headers.add('Access-Control-Allow-Origin', '*')
        newresponse.headers.add('Cache-Control', 'no-cache')
        return newresponse

 

    @app.route('/api/customer/<id>')
    def getCustomerDetailsById(id):
        dict = {"customerId":id, "customerName": "test" + id, "email":"abc@example.com"}
    
        newresponse = Response(json.dumps(dict), mimetype="application/json")
        newresponse.headers.add('Access-Control-Allow-Origin', '*')
        newresponse.headers.add('Cache-Control', 'no-cache')
        return newresponse

 

    @app.route('/api/usageData/<id>')
    def getUsageDataById(id):
        dict = {"customerId":id, "product": [
            {"productId":1000, "feature":[{"feature1":100, "feature2":200}]},
            {"productId":2000, "feature":[{"feature1":10}]}]
            }
    
        newresponse = Response(json.dumps(dict), mimetype="application/json")
        newresponse.headers.add('Access-Control-Allow-Origin', '*')
        newresponse.headers.add('Cache-Control', 'no-cache')
        return newresponse

 

    app.run(host = '0.0.0.0', port=8080, threaded=True)
    
if __name__ == "__main__":
   main()