import pandas as pd #pd es solo como un acronimo que se suele usar para llamar a los pandas

#dataframe es la informacion basica con el nombre de las piezas y centimetros para poder armar el excel
data={ #tanto las piezas y centimetros son como las columnas que tendra nuestro excel
    "piezas" : ["pata", "tablero", "puerta", "estante", "panel Lateral"], #es importante que coinsidan los elementos de lo contrario sera error. 5 elementos en piezas
    "centimetros" : [40,120,60,30,180] #5 elementos de centimetros ok polisha!!!
}

df= pd.DataFrame(data) 
#   pd estas invocando panda y con DataFrame es para pasarle la informacion del data.

#ahora esa informacion la vamos a guardar en un archivo excel
df.to_excel("muebles_medidas.xlsx", index=False)

      