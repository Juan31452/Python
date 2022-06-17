
import pandas as pd
# ruta file csv
rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'


def listaPeliculas(rutaFileCsv: str) -> str:
  try:
    #crear un dataframe
    df = pd.read_csv(rutaFileCsv,sep=",")
    #filtar
    dfpeli = df.filter(items=['Country','Language','Gross Earnings'])
    #print(dfpeli)
    
    #list(dfpeli)
    
    #tabla dinamica index Country y Language
    pivot_tble=pd.pivot_table(dfpeli, index=['Country','Language'], values='Gross Earnings')[:10]
    #print(pivot_tble)
    return (pivot_tble.head(10))   
  except ImportError:
   print("Error al leer el archivo de datos.")

print(listaPeliculas(rutaFileCsv))
  