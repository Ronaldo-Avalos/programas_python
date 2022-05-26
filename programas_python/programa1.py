
print("Hola MUNDO")
print("Ingenieria en Computo Inteligente")

suma = 10+16

resultado = suma/2

print("resultado = ",resultado)


archivo=open("C:\\Users\\xdbmo\\Desktop\\Mi_Carpeta\\UdeC\\Semestre_6\\OP1 - Procesamiento del lenguaje natural\\Programas\\Hola.txt")
print(archivo.read())

archivo2=open("C:\\Users\\xdbmo\\Desktop\\Mi_Carpeta\\UdeC\\Semestre_6\\OP1 - Procesamiento del lenguaje natural\\Programas\\archivo1.txt","w+")
archivo2.write("Buenos dias pana")

archivo2=open("C:\\Users\\xdbmo\\Desktop\\Mi_Carpeta\\UdeC\\Semestre_6\\OP1 - Procesamiento del lenguaje natural\\Programas\\archivo1.txt")
print(archivo2.read())

archivo.close()
archivo2.close()
