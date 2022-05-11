'''
Oscar Dalí Nattaniel Romero Raygoza    6°B    ICI
'''

from tkinter import simpledialog
import nltk
import matplotlib

carpeta_nombre="C:\\Users\\xdbmo\\Desktop\\Mi_Carpeta\\UdeC\\Semestre_6\\OP1 - Procesamiento del lenguaje natural\\Programas\\Docs\\"

archivo_nombre = "DocCompleto.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto = archivo.read()

tokens = nltk.word_tokenize(texto, "spanish")

text = nltk.Text(tokens)

text.collocations()

print("---------------------------------------------------")

text.similar("google")

print("---------------------------------------------------")

text.dispersion_plot(["google", "datos"])
