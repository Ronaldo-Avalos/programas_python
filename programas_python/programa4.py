'''
Oscar Dalí Nattaniel Romero Raygoza    6°B    ICI
'''

import os

carpeta_nombre="C:\\Users\\xdbmo\\Desktop\\Mi_Carpeta\\UdeC\\Semestre_6\\OP1 - Procesamiento del lenguaje natural\\Programas\\Docs\\"

carpeta_salida="C:\\Users\\xdbmo\\Desktop\\Mi_Carpeta\\UdeC\\Semestre_6\\OP1 - Procesamiento del lenguaje natural\\Programas\\Docs\\"

archivo_salida="UNION-PR4.txt"

archivo_lista=os.listdir(carpeta_nombre)

union=""

for archivo_nombre in archivo_lista:
    archivo=open(carpeta_nombre+archivo_nombre)
    union+=archivo.read()+"\n"
    archivo.close()

with open(carpeta_salida+archivo_salida,"w") as salida:
    salida.write(union)