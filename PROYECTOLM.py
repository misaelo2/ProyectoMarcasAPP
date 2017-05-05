import requests
from bottle import template,run,route,request
import os
from sys import argv
import base64

ID=os.environ["APPID"]
Oauthsecret=os.environ["SECRET"]


@route('/')
def identificate():
	if  request.get_cookie("access_token", secret='token de autorizacion'):
		return "funciona las cookies"
	else 
		return template("index.tpl",APPID=ID) 


@route('/callback')
def hacerpeticion() :	
	code=request.query.code
	url_base="https://connect.bbva.com/token"
	payload={"grant_type":"authorization_code","code":code,"redirect_uri":"https://bbuveame.herokuapp.com/callback"}
	encode=base64.b64encode(ID+":"+Oauthsecret)
	diccionario={"Authorization":"Basic "+encode,"Content-Type": "application/json"}
	r=requests.post(url_base,params=payload,headers=diccionario)
	json=r.json()
	response.set_cookie("access_token", json["access_token"],secret='token de autorizacion')
	redirect('/')






	cabecerar2={"Content-Type": "application/json","Authorization":"jwt "+token["access_token"]}
	r2=requests.get("https://apis.bbva.com/accounts-sbx/v1/me/accounts")
run(host='0.0.0.0', port=argv[1] )
