"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():
    df = pd.read_fwf('clusters_report.txt', skiprows=4, skipfooter=0, names=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    df['cluster']=df['cluster'].fillna(method="ffill")
    df['principales_palabras_clave']=df[['cluster', 'principales_palabras_clave']].groupby(['cluster'])['principales_palabras_clave'].transform(lambda x: ' '.join((x)))
    df=df.dropna()
    df=df.reset_index()
    del df["index"]
    df=df.replace(r'ªs+', ' ', regex=True)
    df['principales_palabras_clave']= df['principales_palabras_clave'].str.replace('.','')
    df['porcentaje_de_palabras_clave']= df['porcentaje_de_palabras_clave'].str[:-2]
    df['porcentaje_de_palabras_clave']= df['porcentaje_de_palabras_clave'].str.replace(',','.')
    df['porcentaje_de_palabras_clave']= pd.to_numeric(df['porcentaje_de_palabras_clave'])
    df=df.astype({'principales_palabras_clave':'string'})
    df['cluster'] = df['cluster'].astype(int)
    
    return df
