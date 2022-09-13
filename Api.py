from tkinter import messagebox
#---------------------FUNCION EJECUCION E INTERACCIÓN API------------------------#

import requests
import json as js
#Conexion con la API
def callApi(lista):
    #Devolución de los datos ingresados por el usuario
    tick= lista[0]
    mul=1
    val=lista[3]
    fr=lista[1]
    to=lista[2]
    #Pido a la api la informacion
    while True:
        try:
            respuesta = requests.get("https://api.polygon.io/v2/aggs/ticker/{}/range/{}/{}/{}/{}?apiKey=yZwCxHM7SewyfORUIO55Tf4mnyIwKhxd".format(tick,mul,val,fr,to))
            rrp=respuesta.text
            #Transformo el string formato json en un diccionario
            jsonDict=js.loads(rrp)
            newList=jsonDict["results"]
            break
        except KeyError:
            messagebox.showwarning("Mensaje","Se está ingresando de forma incorrecta uno de los campos")
            break
        except:
            messagebox.showwarning("Mensaje","No puede ingresar campos vacios")
            break
    return newList
    
