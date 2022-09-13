#-------------FUNCION EJECUCION RESUMEN DE DATOS - BASE DE DATOS-------------------#
import sqlite3 as sql
import tkinter as tk
from tkinter import CENTER, ttk
from tkinter.messagebox import showinfo
from turtle import width

#Leo la base de datos y devuelvo una lista
def readData(table):
    conn= sql.connect(table)
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Tickers")
    tickers= cursor.fetchall()             #con fetchall devuelvo una lista de tuplas
    conn.commit()
    conn.close()
    return tickers

#Leo solamente una porcion de la tabla para devolver un resumen
def readDataRed(table):
    conn= sql.connect(table)
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Tickers")
    tickers= cursor.fetchall()             
    ticker={}                                #creo un diccionario con cada ticker
    for tick in tickers:                    
        if tick[0] not in ticker:                #recorro la respuesta de la base de datos y verifico si el ticker existe o no en el dicc
            ticker[tick[0]]= list()                    
        ticker[tick[0]].extend([tick[1]])        #con el método extend creo una lista en la clave indicada (almaceno las fechas que pertenecen a ese ticker)
    conn.commit()
    conn.close()
    return ticker

#Desarrollo de la pantalla gráfica 
def pantalla(data):
    root = tk.Tk()
    root.title('Resumen de datos de Tickers')
    root.geometry('1080x950')

    # definicion de las columnas
    columns = ('Ticker', 'Date', 'Open', 'High', 'Low', 'Close','Volumen','Vwap','Timestamp','Transac')

    tree = ttk.Treeview(root, height=34,columns=columns, show='headings')
    
    #Ajusto las columnas
    tree.column('Ticker',width=100,anchor=CENTER)
    tree.column('Date',width=120,anchor=CENTER)
    tree.column('Open',width=100,anchor=CENTER)
    tree.column('High',width=100,anchor=CENTER)
    tree.column('Low',width=100,anchor=CENTER)
    tree.column('Close',width=100,anchor=CENTER)
    tree.column('Volumen',width=100,anchor=CENTER)
    tree.column('Vwap',width=100,anchor=CENTER)
    tree.column('Timestamp',width=100,anchor=CENTER)
    tree.column('Transac',width=100,anchor=CENTER)

    # Definicion de los encabezados de la talba
    tree.heading('Ticker',text='Ticker')
    tree.heading('Date', text='Date')
    tree.heading('Open', text='Open')
    tree.heading('High', text='High')
    tree.heading('Low', text='Low')
    tree.heading('Close', text='Close')
    tree.heading('Volumen', text='Volumen')
    tree.heading('Vwap', text='Vwap')
    tree.heading('Timestamp', text='Timestamp')
    tree.heading('Transac', text='Transac')

    # Agrego la lista al treeview
    for ticker in data:
        tree.insert('', tk.END, values=ticker)


    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Resumen de tickers', message=','.join(record))


    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=0, column=0, sticky='nsew')

    # Agrego la scroll bar
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    return root

def imprimir():
    pantalla(readData("tickers.db")).mainloop()
