#--------------------FUNCION PARA CONECTAR CON LA BASE DE DATOS E INTERACTUAR CON LA API--------------------#

from ast import Continue
import responsabilidad_base_datos.tickers as tk
import datetime 

#Manejo de los posbiles errores
def creacionDB():
    #Error al conectar con la base de datos
    try:
        tk.createDB("tickers.db")
        print("Conexión Satisfactoria")
    except:
        print("No se ha podido acceder a la base de datos")
    #Error al crar la tabla
    try:
        tk.createTable("tickers.db")
    except:
        Continue
#Inserto los datos en la base de datos
def inserData (vari,tic):
    #Recorro la longitud de la lista y tomo los valores del diccionario
    for i in vari: 
        dic=i
        #Tomo la época y la guardo como fecha
        epoch= dic['t']/1000
        ep= datetime.datetime.fromtimestamp(epoch)
        epToDat=ep.date()
        #Armo la tabla
        tk.insertarT("tickers.db",tic,epToDat,dic['o'],dic['h'],dic['l'],dic['c'],dic['v'],dic['vw'],dic['t'],dic['n'])
    
