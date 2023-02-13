"""
♣ → Verificaciones que dedo hacer o tomar en cuenta en el programa 
♥ → Correciones que debo de hacer 
? → Dudas, preguntas a resolver mas adelante 
◘ → Explicaciones.
♠ → Cosas que debo de agregar mas adelante 
♦ → plus o sea detalles que podria agregar 
"""
opc = 0


def  Menu():
    
    global opc  
    print()
    print("___♥___♥___MENU___♥___♥____")
    print("| 1. Cargar Archivo       ♥")
    print("♥ 2. Celdas por prosperar |")                # identifica las celdas donde las muestras pueden prosperar 
    print("| 3. Colocar Muestra      ♥")
    print("♥ 4. Inicialización       |")
    print("| 5. Reporte final        ♥")
    print("♥ 6. Salir                |")
    print("|____♥___♥___♥___♥___♥____♥")    
    print()
    print("Ingrese La opcion que desea Realizar", end="    ")
    opc = input()
    print()

    if opc == "1" :
        print("Lectura del Archivo XML")
        # ♥  PEDIR LA RUTA DEL ARCHIVO POR LEER 

    elif opc == "2":
        print("Las Celdas en donde prosperan las muestras son las siguientes")
    
    elif opc == "3":
        print("Usted a decidido colocar una muestra en la cuadricula: ")
        print()
        print("Por favor ingrese el tipo de Organismo que será la muestra:  ", end = " ")  # ♣ Hay que verificar que el organismo que seleccione Exista 
        Organismo = input()
        print()
        # ♥ Si el organismo no existe mostrar error
        # ? Que pasa si el organismo no existe 
        print("Ingrese en que fila se encontrará la muestra: ", end ="  ") # ♣ Hay que verificar si no se pas del total de filas que hay 
        fila = input()
        print()
        print("Ingrese en que columna se encontrará la muestra: ", end="  ") # ♣ Verificar si no se pasa del total de columnas que hay 
        columna = input()
        print()
        # ♣ Verificar que no se vaya a colocar en una celda vacia 
        # ? Que pasa si se coloca en una celda ocupada 
    
    elif opc == "4":
        # ♦ Preguntar si esta seguro de borrar los datos, si no lo esta mostrar un mensaje diciendo usted ha decidido no inicializar nada y luego volver a mostra menu 
        print("Usted ha inicializado el programa")

    elif opc== "5":
        print("Reporte final de las actualizaciones de las celdas y muestras ") # ♠ aqui debe de ir el reporte xml con la info final 
    elif opc == "6":
        print("usted ha salido ")
    else:
        print("opcion erronea")
if __name__ == '__main__':
    while opc !="6":
        Menu()