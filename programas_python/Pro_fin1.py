'''
El programa consiste en leer dos documentos de texto .txt
Cada documento debe tener tres parrafos como minimo
..Debe mostrar cuantas lineas con texto y cuantas lineas vacias tiene cada doc
    ...Eliminar los simbolos de puntuacion
    ...Muestre las palabras que contiene cada documento de manera ordenada.
    ...Muestre cuantas palabras tiene cada documento

    ...Que una los documentos en uno nuevo.
    ...Que elimine los simbolos de puntuacion
    ...Que muestre todas las palabras que contiene el documento nuevo de manera ordenada
    ...Que muestre cuantas palabras tiene el doc
    ...Que escriba una palabra e indique si existe o no
'''

import os 

carpeta_nombre="C:\\Users\\xdbmo\\Desktop\\Mi_Carpeta\\UdeC\\Semestre_6\\OP1 - Procesamiento del lenguaje natural\\Programas\\Docs\\Pro1\\"

archivo_salida="UNION-PROYEC.txt"

simbolos = ["(",")",",",".",";",":","\""]

texto_junto = ""

archivos_lista = os.listdir(carpeta_nombre)

for archivo_nombre in archivos_lista:
    with open(carpeta_nombre+archivo_nombre,"r") as archivo:
        lineas_lista = archivo.readlines()
    num_linea = 1
    num_texto = 0
    num_vacio = 0
    for linea in lineas_lista:
        if linea.strip() == "":
            num_linea = num_linea + 1
            num_vacio = num_vacio+1
        else: 
            num_linea = num_linea+1
            num_texto = num_texto+1
    print("El archivo", archivo_nombre, " TIENE ", num_linea, "lineas")
    print("El archivo", archivo_nombre, " TIENE ", num_texto, "lineas con texto")
    print("El archivo", archivo_nombre, " TIENE ", num_vacio, "lineas vacias\n")

for archivo_nombre in archivos_lista:
    print("\nARCHIVO ", archivo_nombre)
    with open(carpeta_nombre+archivo_nombre,"r") as archivo:
        texto = archivo.read()
    for simbolo in simbolos:
        texto = texto.replace(simbolo, " ")
    texto_junto = texto_junto + texto + "\n"
    palabras_lista = texto.split()
    palabras_lista.sort()
    print("Tiene ", len(palabras_lista), " palabras.")
    
    print(palabras_lista)

with open(carpeta_nombre+archivo_salida,"w") as salida:
    salida.write(texto_junto)

with open(carpeta_nombre+archivo_salida,"r") as archivo:
    texto = archivo.read()

print("\nArchivo ", archivo_salida)
palabras_lista = texto.split()
palabras_lista.sort()
print("\nTiene ", len(palabras_lista), " palabras.")

print(palabras_lista)

with open(carpeta_nombre+archivo_salida,"r") as archivo:
    lineas_lista = archivo.readlines()

palabra = input("\nEscribe la palabra a buscar en el documento: ")
num_palabras=0

for linea in lineas_lista:
    if linea.strip() != "":
        if palabra in linea:
            num_palabras = num_palabras+1

print("La palabra: ", palabra, " se encuentra: ", num_palabras," veces en el documento.")



