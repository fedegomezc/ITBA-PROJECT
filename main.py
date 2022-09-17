#---------------------------ARCHIVO PRINCIPAL PARA LA EJECUCIÓN DEL PROGRAMA---------------------#
#Archivo principal del programa
import Responsabilidad_Base_Datos.base_datos as db
import Funcionalidad_Pantallas.Menu_principal as mp

if __name__ == '__main__':
    #Se crea la base de datos   
    db.creacionDB()
    #Abro menú principal
    mp
