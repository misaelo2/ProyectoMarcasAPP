import requests
import base64
import json
TODO= 'app.bbva.infoCuentas:QUe7MwasE5gJO434ITz82FJ@nz3j8ypcEf4YYcSjw@y2AS1IhfiJGEiUr6qm9tXx'

url_base= 'https://connect.bbva.com/token?grant_type=client_credentials'
encode=base64.b64encode(TODO)
dicc={"Authorization":"Basic "+encode,"Content-Type": "application/json"}
r=requests.post(url_base,headers=dicc)
print r.text