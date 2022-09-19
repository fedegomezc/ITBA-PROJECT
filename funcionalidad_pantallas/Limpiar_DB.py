#----------------------FUNCION PARA LIMPIAR LA BASE DE DATOS----------------------#

from responsabilidad_base_datos.tickers import eliminar as el
import tkinter as tk

def limpiar():
    ventana=tk.Tk()
    ventana.title('Limpiar datos')
    ventana.geometry("250x50")
    def btn():
        el("tickers.db")
        def cerrarVentana():
            ventana.destroy()                       #Funcion para cerrar la ventana
        ventana.title("Limpiando datos...")
        ventana.after(2000, cerrarVentana)
    boton1 = tk.Button(ventana, text="Limpiar", command=btn)
    boton1.grid(column=1, row=3)
    boton1.place(relx=0.5,rely=0.5,width=50,anchor='c')

    ventana.mainloop()