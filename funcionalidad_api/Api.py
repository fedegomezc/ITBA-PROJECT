#---------------------FUNCION EJECUCION E INTERACCIÓN API------------------------#
from tkinter import messagebox
import requests
import json as js
#Conexion con la API
def callApi(listInput):
    #Devolución de los datos ingresados por el usuario
    tick= listInput[0]
    mul=1
    val=listInput[3]
    fr=listInput[1]
    to=listInput[2]
    #Pido a la api la informacion
    while True:
        try:
            responseAp= requests.get("https://api.polygon.io/v2/aggs/ticker/{}/range/{}/{}/{}/{}?apiKey=yZwCxHM7SewyfORUIO55Tf4mnyIwKhxd".format(tick,mul,val,fr,to))
            responseTxt=responseAp.text
            #Transformo el string formato json en un diccionario
            jsonDict=js.loads(responseTxt)
            listTickerJson=jsonDict["results"]
            break
        except KeyError:
            messagebox.showwarning("Mensaje","Se está ingresando de forma incorrecta uno de los campos")
            break
        except:
            messagebox.showwarning("Mensaje","No puede ingresar campos vacios")
            break
    return listTickerJson
    
