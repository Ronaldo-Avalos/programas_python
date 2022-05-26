

carpeta_nombre="C:\\Users\\xdbmo\\Desktop\\Mi_Carpeta\\UdeC\\Semestre_6\\OP1 - Procesamiento del lenguaje natural\\Programas\\Docs\\"

archivo_nombre="UNION-PR4.txt"

palabra = input("Escribe la palabra a buscar en el documento: ")

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto = archivo.read()

if palabra in texto:
    print("La palabra ", palabra, " fue encontrada en el texto.")
else:
    print("La palabra ", palabra, " no fue encontrada en el texto.")
