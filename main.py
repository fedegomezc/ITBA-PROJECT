#---------------------------ARCHIVO PRINCIPAL PARA LA EJECUCIÓN DEL PROGRAMA---------------------#
#Archivo principal del programa
import base_datos as db
import Menu_principal as mp

if __name__ == '__main__':
    #Se crea la base de datos   
    db.creacionDB()
    #Abro menú principal
    mp
