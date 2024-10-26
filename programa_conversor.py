import pandas as pd

def cm_a_pulgadas(cm):
    return f"{cm / 2.54:.3f}"

def cm_a_pies(cm):
    return cm / 30.48

df = pd.read_excel("muebles_medidas.xlsx")
df["Pulgadas"] = df["centimetros"].apply(cm_a_pulgadas) 
df["Pies"] = df["centimetros"].apply(cm_a_pies) 

df.to_excel("mueble_medidas_convertidas_ujajaja.xlsx", index=False)
print(
    "Conversion completada y guardada en un nuevo repositorio mueble_medidas_convertidas.xlsx"
)
