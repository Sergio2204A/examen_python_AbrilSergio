import os 
import sys

def limpiarpantalla():
    if sys.platform=="linux" or sys.platform=="darwin":
        os.system('clear')
    else: 
        os.system('cls')

def pausar_pantalla():
    input ('presione para continuar......')