#---------------------Pedido de datos para la Actualización de datos------------------#

from ast import Continue
import tkinter as tk
from tkinter import messagebox
from funcionalidad_api.Api import callApi as api
import responsabilidad_base_datos.base_datos as db

#Ventana de visualizacion para actualizacion de los datos
def actualizacion():
    ventana1=tk.Tk()
    ventana1.title('Actualizacion de datos') 
    # Caja de texto con el ticker a pedir
    label1 = tk.Label(ventana1, text="Ingrese ticker a pedir:")
    label1.grid(column=0, row=0)
    dato1 = tk.StringVar()
    entry1 = tk.Entry(ventana1, width=30, textvariable=dato1)
    entry1.grid(column=1, row=0)
    # Caja de texto fecha de inicio a pedir
    label2 = tk.Label(ventana1, text="Desde [AAAA-MM-DD]")
    label2.grid(column=0, row=1)
    dato2 = tk.StringVar()
    entry2 = tk.Entry(ventana1, width=30, textvariable=dato2)         
    entry2.grid(column=1, row=1)
    # Caja de texto fecha fin a pedir
    label3 = tk.Label(ventana1, text="Hasta [AAAA-MM-DD]")
    label3.grid(column=0, row=2)
    dato3 = tk.StringVar()
    entry3 = tk.Entry(ventana1, width=30, textvariable=dato3)         
    entry3.grid(column=1, row=2)
    # Caja de texto con timespan
    label4 = tk.Label(ventana1, text="Espacio de tiempo \n[day,week,month,quarter,year]")
    label4.grid(column=0, row=3)
    dato4 = tk.StringVar()
    entry4 = tk.Entry(ventana1, width=30, textvariable=dato4)         
    entry4.grid(column=1, row=3)

    # Función boton de ingreso de datos
    def boton():
        #tomo los valores que coloca el usuario
        d1=entry1.get().strip()
        d2=entry2.get().strip()
        d3=entry3.get().strip()
        d4=entry4.get().strip()
        datosAlm=[d1.upper(),d2,d3,d4]                          #Los almaceno en una lista
        #llamo a los modulos de Api y de base de datos para insertar los valores en la misma
        okMsg=True
        try:
            data=db.inserData(api(datosAlm),d1.upper())
        except UnboundLocalError:
            messagebox.showwarning("Mensaje","Por Favor, ingrese nuevamente los datos")
            okMsg=False
        def cerrarVentana():
            if okMsg==True:
                messagebox.showinfo('Mensaje','Datos guardados correctamente')
            ventana1.destroy()                       #Funcion para cerrar la ventana
        ventana1.title("Pidiendo Datos...")
        ventana1.after(3000, cerrarVentana)          #Cerramos la ventana después de 3 segundos 
        return data

    # Botón para envío de los datos
    boton1 = tk.Button(ventana1, text="Pedir datos", command=boton)
    boton1.grid(column=1, row=5)

    ventana1.mainloop() 
    
    
    
    
