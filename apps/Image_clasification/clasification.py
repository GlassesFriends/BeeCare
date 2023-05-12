import csv
import pandas as pd
import requests

def download(Abeja_melifera_europea, img_name):
    for i in range(len(Abeja_melifera_europea)):
        url_imagen = Abeja_melifera_europea[i] # El link de la imagen
        nombre_local_imagen = img_name+'_'+str(i)+'.jpg' # El nombre con el que queremos guardarla
        imagen = requests.get(url_imagen).content
        with open(nombre_local_imagen, 'wb') as handler:
                handler.write(imagen)

common_name=[];

Abeja_melifera_europea=[];

with open('observations-303237.csv', encoding="utf8") as f:
    reader=csv.reader(f)
    for row in reader:
        if(row[36] not in common_name and row[36]!='common_name'):
            common_name.append(row[36])
        

print((common_name))

with open('observations-303237.csv', encoding="utf8") as f:
    reader=csv.reader(f)
    for row in reader:
            if(common_name[28]==row[36]):
                Abeja_melifera_europea.append(row[13])


print(Abeja_melifera_europea)
download(Abeja_melifera_europea,'Abejas cortadoras de hojas'.replace(' ','_'))

# miarchivo=open('observations-303237.csv','r')
# lectura= miarchivo.readline().split(',')
# print(len(lectura))
# print(lectura[13])

# datos=pd.read_csv('observations-303237.csv',header=0,usecols=['common_name','image_url'])
# df=pd.DataFrame(datos)
# common_name=df.sort_values(by='common_name')
# print(common_name)
# print(df.query("common_name=='abejorro californiano'"))





