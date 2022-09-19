#--------------------------FUNCION BOTÓN PARA IMPRIMIR EL RESUMEN------------------------#
from tkinter import messagebox
from funcionalidad_pantallas.ResumenDatos import imprimir as imp
from funcionalidad_pantallas.ResumenDatos import readDataRed as redu
import tkinter as tk

def imprimir():
    ventana=tk.Tk()
    ventana.title('Resumen Base de Datos')
    ventana.geometry("400x50")
    def btn():
        imp()
    def cerrarVentana():
        ventana.destroy()                       #Funcion para cerrar la ventana
    def btn2():
        resu=redu("tickers.db")
        info=[]
        for k,v in resu.items():
            result=f'{k} ---> {v[0]} a {v[-1]}'
            info.append(result)
        infos=str(info).strip('[]!').replace("'","").replace(', ','\n')   #trnasformo la lista en str para manipular los datos y poder imprimir
        messagebox.showinfo('Resumen',infos)                              #muestro un mensaje con el resumen
        
    boton1 = tk.Button(ventana, text="Informe completo", command=btn)
    boton1.grid(column=1, row=3)
    boton1.place(relx=0.20,rely=0.5,width=120,anchor='c')

    boton2 = tk.Button(ventana, text="Imprimir resumen", command=btn2)
    boton2.grid(column=1, row=3)
    boton2.place(relx=0.55,rely=0.5,width=120,anchor='c')

    boton3 = tk.Button(ventana, text="Salir", command=cerrarVentana)
    boton3.grid(column=1, row=3)
    boton3.place(relx=0.85,rely=0.5,width=80,anchor='c')

    ventana.mainloop()