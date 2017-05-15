import requests
from bottle import template,run,route,request,redirect,run,response,static_file
import os
from sys import argv
import base64

ID=os.environ["APPID"]
Oauthsecret=os.environ["SECRET"]


@route('/')
def identificate():
	if  request.get_cookie("access_token", secret='token de autorizacion'):
		token=request.get_cookie("access_token", secret='token de autorizacion')
		cabecerar2={"Accept": "application/json","Authorization":"jwt "+token}
		r2=requests.get("https://apis.bbva.com/accounts-sbx/v1/me/accounts",headers=cabecerar2)
	 	if r2.status_code==200 :
		 	respuesta=r2.json()
		 	cuentas=respuesta["data"]["accounts"]
		 	return template("mostrarcuentas.tpl",listacuentas=cuentas)
		else :
			return template("index.tpl")
	else :
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
	response.set_cookie("access_token",json["access_token"],secret='token de autorizacion')
	redirect('/')

@route('/cuentas/<IBAN>') 
def transaccion(IBAN) :
	token =request.get_cookie("access_token", secret='token de autorizacion')
	if token : 
		token =request.get_cookie("access_token", secret='token de autorizacion')
		cabecerar3={"Accept": "application/json","Authorization":"jwt "+token}
		r3=requests.get("https://apis.bbva.com/accounts-sbx/v1/me/accounts/"+IBAN,headers=cabecerar3)
		json=r3.json()
		return template("infocuenta.tpl",info=json,cuenta=IBAN)
	else :	
		return "ERROR , necesitas estar logueado "
@route('/cuentas/movimientos/<cuentaid>')
def movimientos(cuentaid) :
	token =request.get_cookie("access_token", secret='token de autorizacion')
	cabecerar4={"Accept": "application/json","Authorization":"jwt "+token}
	r4=requests.get("https://apis.bbva.com/accounts-sbx/v1/me/accounts/"+cuentaid+"/transactions?pageSize=10",headers=cabecerar4)
	json=r4.json()
	return template("infotransacciones.tpl",movimientos=json["data"]["accountTransactions"])


@route('/desloguearse')
def desloguearse() :
	token =request.get_cookie("access_token", secret='token de autorizacion')
	cabecerar5={"Authorization":"jwt "+token}
	r5=requests.put("https://apis.bbva.com/manager-sbx/v1/data",headers=cabecerar5 )
	redirect('/')

@route('/static/<filepath:path>')
def server_static(filepath) :
	return static_file(filepath , root='static')


run(host='0.0.0.0', port=argv[1] )


#requests.put(https://apis.bbva.com/manager-sbx/v2/data,headers="jwt "+access_token)