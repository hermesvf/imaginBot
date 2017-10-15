# -*- coding: utf-8 -*-
from flask import Flask,request,jsonify
from OpenSSL import SSL
import json
import urllib

app = Flask(__name__)

def getFromServer(query):
    print(query)
    response_server = urllib.urlopen(caca_server+query)
    return response_server.read()

def toText(data):
    return """{"speech":"You have """+ data +""" Euros", "displayText":"You have """+ data +""" Euros"}"""

def balance():
    #@app.route('/<user>/balance')
    data = getFromServer("/Marc/balance")
    print(data)
    return toText(data)

def movements():
    #@app.route('/<user>/movements')
    data = getFromServer("/Marc/movements")
    print(data)
    return data

def promotions(type,city):
    #@app.route('/promotions/<type>/<city>')
    data = getFromServer("/promotions/{0}/{1}".format(type,city))
    print(data)
    return data

def send(fromm,to,amount):
    #@app.route('/send/<from_user>/<to_user>/<amount>')
    data = getFromServer("/send/{0}/{1}/{2}".format(fromm,to,amount))
    print(data)
    return data

@app.route('/', methods=['GET','POST'])
def hello_world():
    resultat = None
    request_json =request.get_json()
    action = request_json['result']['action']
    if action == 'balance.query':
       print('balance query')
       resultat = balance()
    elif action == 'products.company':
        print('products company')
        enterprise = request_json['result']['parameters']['enterprise']
        resultat = getFromServer('/products/{}'.format(enterprise))
	print(str(resultat))
    elif action == 'promotions':
        print('promotions')
        city = request_json['result']['parameters']['geo-city']
        print(city)
        typee = request_json['result']['parameters']['type']
        print(typee)
        resultat = promotions(typee,city)
    elif action == 'send.money':
        print('send money')
        fromm = "Marc"
        to = request_json['result']['parameters']['person']
        amount = request_json['result']['parameters']['unit-currency']['amount']
        resultat = send(fromm,to,amount)
    else:
        print('Unsupported action')


    return resultat, 201, {'Content-Type': 'application/json'}

caca_server = "http://46.101.16.235:5000"


if __name__ == '__main__':
    	context = ('fullchain.pem','privkey.pem')
	app.run(host='0.0.0.0', port=8080, ssl_context=context, debug=True)
