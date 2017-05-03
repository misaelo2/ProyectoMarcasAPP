import requests
from bottle import template,run,route
import os


ID=os.environ["APPID"]
#Oauthsecret=OS.environ["SECRET"]


@route('/')
def identificate():
	return template("index.tpl",APPID=ID) 


@route('/callback')
def hacerpeticion() :	
	code=request.query.code
	ruta=request.urlparts["path"]
	url_base="https://connect.bbva.com/token"
	payload={"grant_type":"authorization_code","code":code,"redirect_uri":"/callback"}
	return "<p>%s</p>" %ruta
run(host='localhost', port=8080)