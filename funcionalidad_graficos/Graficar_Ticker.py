#-----------------Ventana para pedir datos al usuario - Gráfico de Ticker-------------------#

import tkinter as tk
from tkinter import messagebox
from funcionalidad_graficos.Graph import graphic as gp
def graficarTicker():
    ventana1 = tk.Tk()
    ventana1.title('Grafico de ticker')
    # Caja de texto con el ticker a pedir
    label1 = tk.Label(ventana1, text="Ingrese ticker a graficar:")
    label1.grid(column=0, row=0)
    dato1 = tk.StringVar()
    entry1 = tk.Entry(ventana1, width=30, textvariable=dato1)
    entry1.grid(column=1, row=0)

    # Función para ingresar los datos y cerrar ventana
    def boton():
        d1=entry1.get().strip()
        try:
            gp('tickers.db',d1.upper())
        except:
            messagebox.showwarning('Mensaje','Ticker cargado incorrectamente')
        def cerrarVentana():
            ventana1.destroy()
        ventana1.title("Graficando...")       
        ventana1.after(1000,cerrarVentana)         #Cerramos la ventana 
    
    # Botón para envío de los datos
    boton1 = tk.Button(ventana1, text="Graficar", command=boton)     
    boton1.grid(column=1, row=3)

    ventana1.mainloop()
