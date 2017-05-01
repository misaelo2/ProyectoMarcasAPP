import requests
from bottle import template,run,route
import os


ID=os.environ["APPID"]
#Oauthsecret=OS.environ["SECRET"]


@route('/')
def identificate():
	return template("index.tpl",APPID=ID) 


#@route('/callback')


run(host='localhost', port=8080)
