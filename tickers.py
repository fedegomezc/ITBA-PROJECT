#---------------------FUNCIÓN DE CREACION DE LA BASE DE DATOS E INSERTAR DATOS--------------------#

import sqlite3 as sql
#Creo la base de datos
def createDB (table):
    conn= sql.connect(table)
    conn.commit()
    conn.close()
#Creo la tabla con el contenido
def createTable(table):
    conn= sql.connect(table)
    sql.Cursor= conn.cursor()
    sql.Cursor.execute(
            """CREATE TABLE Tickers (
                Ticker text,
                Date text,
                Open float,
                High float,
                Low float,
                Close float,
                Volumen float,
                Vwap float,
                Timestamp integer,
                Transac integer
            )"""
        )
    conn.commit()
    conn.close
#Inserto los trickers
def insertarT(table,tic,d,o,h,l,c,v,vw,t,tr):
    conn=sql.connect(table)
    cursor= conn.cursor()
    cursor.execute ("INSERT INTO Tickers (Ticker,Date,Open,High,Low,Close,Volumen,Vwap,Timestamp,Transac) VALUES (?,?,?,?,?,?,?,?,?,?)",(tic, d, o, h, l, c, v, vw, t, tr))
    conn.commit()
    conn.close()
#elimino datos de la tabla para actualizar valores
def eliminar (table):
    conn= sql.connect(table)
    sql.Cursor= conn.cursor()
    sql.Cursor.execute(
            """DELETE FROM Tickers; 
            """
        )
    conn.commit()
    conn.close
