#------------FUNCIÓN PARA GRAFICAR LOS TICKERS-----------#
import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt


def graphic(table,ticker):
    conn = sql.connect(table) 
    sql_query = pd.read_sql_query ('''
                                SELECT
                                Ticker, Date, Open, Close, High, Low
                                FROM Tickers
                                WHERE Ticker= '{ticker}';
                                '''.format(ticker=ticker), conn)

    #Armamos un Data Frame de la base de datos para graficar
    prices = pd.DataFrame(sql_query, columns = ['Ticker', 'Date', 'Open', 'Close', 'High', 'Low'])

    #Saco las horas de la fecha para el gráfico
    prices['Date'] = pd.to_datetime(prices['Date']).dt.date

    #Index para que me lo tome como el eje x. 
    prices.set_index('Date', inplace=True)

    plt.rcParams["figure.figsize"] = [15, 10]
    plt.rcParams["figure.autolayout"] = True

    #Graficamos uno de líneas
    plt.subplot(212)
    ax = plt.gca()

    prices.plot(kind='line',marker='.', y='Close', color='blue', ax=ax)
    ax.set_ylabel("Cierre")
    ax.set_xlabel("Periodo")

    #grafico de boxplots
    plt.subplot(211)

    #Defino el ancho de los boxplots
    width = 1.5
    width2 = .1

    #Defino los precios up y down
    up = prices[prices.Close>=prices.Open]
    down = prices[prices.Close<prices.Open]

    #Defino los colores 
    col1 = 'green'
    col2 = 'red'

    #Grafico los up prices
    plt.bar(up.index, up.Close-up.Open, width, bottom=up.Open, color=col1)
    plt.bar(up.index, up.High-up.Close, width2, bottom=up.Close, color=col1)
    plt.bar(up.index, up.Low-up.Open, width2, bottom=up.Open, color=col1)

    #Grafico los down prices
    plt.bar(down.index, down.Close-down.Open, width, bottom=down.Open, color=col2)
    plt.bar(down.index, down.High-down.Open, width2, bottom=down.Open, color=col2)
    plt.bar(down.index, down.Low-down.Close, width2, bottom=down.Close, color=col2)

    #Agrego los títulos de los ejes
    plt.ylabel('Cierre')
    plt.xlabel('Periodo')


    #Imprimo
    plt.show()
