import requests
from bottle import template,run,route,request
import os
from sys import argv

ID=os.environ["APPID"]
#Oauthsecret=OS.environ["SECRET"]


@route('/')
def identificate():
	return template("index.tpl",APPID=ID) 


@route('/callback')
def hacerpeticion() :	
	code=request.query.code
	url_base="https://connect.bbva.com/token"
	payload={"grant_type":"authorization_code","redirect_uri":"https://bbuveame.herokuapp.com/callback","code":code}
	r=requests.POST(url_base,params=payload)
	return r.text
run(host='0.0.0.0', port=argv[1] )
