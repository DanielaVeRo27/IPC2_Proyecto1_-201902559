from ArchivoXml import Lectura
global opc  

def menu2():
    print()
    print("___♥___♥___MENU___♥___♥____")
    print("| 1. Cargar Archivo       ♥")

    print("Ingrese La opcion que desea Realizar", end="    ")
    opc = input()
    if opc =="1":
        print("Ingerese la ruta de su archivo: ", end="   ")
        Lectura()
    else:
        print("Hola lusjn ")
menu2()