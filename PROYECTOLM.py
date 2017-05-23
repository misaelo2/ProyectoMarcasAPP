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
		respuesta=r2.json()
		cuentas=respuesta["data"]["accounts"]
		return template("mostrarcuentas.tpl",listacuentas=cuentas)
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

@route('/cuentas/movimientos/<cuentaid>',method='GET')
def formulario(cuentaid) :
	return template('Formulario.tpl',cuenta=cuentaid)

@route('/cuentas/movimientos/<cuentaid>',method='POST')
def movimientos(cuentaid) :
	fechafrom=request.forms.get('dateFrom')
	fechato=request.forms.get('dateTo')
	token =request.get_cookie("access_token", secret='token de autorizacion')
	cabecerar4={"Accept": "application/json","Authorization":"jwt "+token}
	if fechafrom and fechato :
		r4=requests.get("https://apis.bbva.com/accounts-sbx/v1/me/accounts/"+cuentaid+"/transactions?dateFrom="+fechafrom+"&dateTo="+fechato,headers=cabecerar4)
		json=r4.json()
		if r4.status_code==200 :
			return 	template("infotransacciones.tpl",cuentaid=cuentaid,movimientos=json["data"]["accountTransactions"],fechafrom=fechafrom,fechato=fechato,numpag=5)
		else :
			return "<h1>Las fechas son incorrectas</h1>"
	elif not fechafrom and not fechato :
		fechafrom=""
		fechato=""
		r4=requests.get("https://apis.bbva.com/accounts-sbx/v1/me/accounts/"+cuentaid+"/transactions?pageSize=5",headers=cabecerar4)
		json=r4.json()
		return template("infotransacciones.tpl",cuentaid=cuentaid,movimientos=json["data"]["accountTransactions"],fechafrom=fechafrom,fechato=fechato,numpag=5)
	else :	
		return "<h1>Necesitas introducir las dos fechas, o ninguna</h1>"

@route('/cuentas/movimientos/<cuentaid>/<fechafrom>/<fechato>/<numpag>')
def movimientosconvariables(cuentaid,fechafrom,fechato,numpag) :
	token =request.get_cookie("access_token", secret='token de autorizacion')
	cabecerar6={"Accept": "application/json","Authorization":"jwt "+token}
	r6=requests.get("https://apis.bbva.com/accounts-sbx/v1/me/accounts/"+cuentaid+"/transactions?dateFrom="+fechafrom+"&dateTo="+fechato,headers=cabecerar6)
	json=r6.json()
	return json

@route('/desloguearse')
def desloguearse() :
	token =request.get_cookie("access_token", secret='token de autorizacion')
	cabecerar5={"Authorization":"jwt "+token}
	r5=requests.put("https://apis.bbva.com/manager-sbx/v1/data",headers=cabecerar5 )
	response.set_cookie("access_token",' ',max_age=0)
	redirect('/')

@route('/static/<filepath:path>')
def server_static(filepath) :
	return static_file(filepath , root='static')


run(host='0.0.0.0', port=argv[1] )


