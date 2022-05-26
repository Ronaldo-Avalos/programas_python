
carpeta_nombre="C:\\Users\\xdbmo\\Desktop\\Mi_Carpeta\\UdeC\\Semestre_6\\OP1 - Procesamiento del lenguaje natural\\Programas\\Docs\\"
archivo_nombre="UNION-PR4.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto = archivo.read()

simbolos=["(",")",",",".",";",":","\""]

for simbolo in simbolos:
    texto=texto.replace(simbolo," "+simbolo+" ")

palabras_lista=texto.split()

palabras_unicas=[]

for palabra in palabras_lista:
    if palabra in palabras_unicas:
        continue
    palabras_unicas.append(palabra)

print(palabras_unicas)
num=len(palabras_unicas)
print("numero de palabras en el documento: ", num)
print("numero de palabras en todo el documento: ", len(palabras_lista))
