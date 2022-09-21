#-------------------MENÚ PRINCIPAL----------------------#
import tkinter as tk
from funcionalidad_pantallas.Limpiar_DB import limpiar as lp                     #Función para limpiar base de datos
from funcionalidad_api.Actualizacion_Datos import actualizacion as act     #Función opcion actualizar datos
from funcionalidad_graficos.Graficar_Ticker import graficarTicker               #Función (ventana) opción 'Grafico de Ticker'
from funcionalidad_pantallas.Print_Resumen import imprimir as im                 #Función para resumir los datos actuales dela Data Base


# creamos la ventana principal
ventana = tk.Tk()
ventana.title('ITBA Project')          
ventana.geometry('500x400')

# creamos una barra de menús y la añadimos a la ventana principal
# cada ventana solo puede tener una barra de menús
barra_menus = tk.Menu(ventana)
ventana.config(menu=barra_menus)

# creamos un menú cuyo contenedor será la barra de menús
menu = tk.Menu(barra_menus, tearoff=False)

# añadimos opciones al menú indicando su nombre y acción asociado
menu.add_command(label='Actualización de datos', command=act)

#Limpiar la base de datos
menu.add_command(label='Limpiar base de datos', command=lp)

# creamos submenú de las opciones de visualización de datos 
submenu = tk.Menu(menu, tearoff=False)
submenu.add_command(label='Resumen', command=im)
submenu.add_command(label='Gráfico de ticker', command=graficarTicker)

# añadimos el submenú al menú principal
menu.add_cascade(label='Visualización de datos', menu=submenu)

# añadimos una línea separadora y la opción de salir
menu.add_separator()
menu.add_command(label='Salir', command=ventana.destroy)

# finalmente añadimos el menú a la barra de menús
barra_menus.add_cascade(label="Menú", menu=menu)

# añadimos una etiqueta
textoBienvenido = tk.Label(ventana, text='¡Bienvenido/a!\nAca encontrarás\ninformación de\ntickers')
textoBienvenido.place(x=200, y=140)

# añadimos una etiqueta
textoAut = tk.Label(ventana, text='Powered by: Catalina Vivot-Federico Gómez-Sebastian Gómez\nVictor Monzon-Martin Gautt')
textoAut.place(x=20, y=350)

#if __name__ == '__main__':
ventana.mainloop()  # ejecutamos la ventana principal
