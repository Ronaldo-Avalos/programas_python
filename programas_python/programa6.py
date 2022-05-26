
import os

carpeta_nombre="C:\\Users\\xdbmo\\Desktop\\Mi_Carpeta\\UdeC\\Semestre_6\\OP1 - Procesamiento del lenguaje natural\\Programas\\Docs\\"

simbolos = ["(",")",",",".",";",":","\""]
archivos_lista=os.listdir(carpeta_nombre)
for archivos_nombre in archivos_lista:
    archivo = open(carpeta_nombre+archivos_nombre)
    lineas_lista = archivo.readlines()
    archivo.close()
    longitud = len(lineas_lista)
    print("El archivo", archivos_nombre, " TIENE ", longitud, "lineas")


    archivo = open(carpeta_nombre+archivos_nombre)
    texto = archivo.read()
    archivo.close()
    for simbolo in simbolos:
        texto = texto.replace(simbolo, " " + simbolo + " ")
    
    palabras_lista = texto.split()
    palabras_lista.sort()
    for palabras in palabras_lista:
        print(palabras)
    
