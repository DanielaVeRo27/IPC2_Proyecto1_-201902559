from ArchivoXml import Lectura
from Tablero import CrearTablero, Imprimir, ColocarOrganismo
from Graficar import GeneraGrafica
from Reporte import Reporte


"""
♣ → Verificaciones que dedo hacer o tomar en cuenta en el programa 
♥ → Correciones que debo de hacer 
? → Dudas, preguntas a resolver mas adelante 
◘ → Explicaciones.
♠ → Cosas que debo de agregar mas adelante 
♦ → plus o sea detalles que podria agregar 
"""
opc = 0
ResSN =""




def  Menu():
    
    global opc , OrganismoList, MuestrasList, CeldasVivasList, ResSN
    
    print()
    print("♥___♥___♥___MENU___♥___♥___♥___")
    print("| 1. Cargar Archivo            ♥")
    print("♥ 2. Ver informacion Muestra   |")                # identifica las celdas donde las muestras pueden prosperar 
    print("| 3. Actualizar Muestra        ♥")
    print("♥ 4. Inicialización            |")
    print("| 5. Reporte final             ♥")
    print("♥ 7. Crear Nueva Muestra       |")
    print("| 8. Colocar Organismo         ♥")      
    print("♥          6. Salir            |")
    print("|____♥___♥___♥___♥___♥____♥____♥")    
    print()
    
    print("Ingrese La opcion que desea Realizar", end="    ")
    opc = input()
    
    print()

    if opc == "1" :
        print("Lectura del Archivo XML")
        print("Ingerese la ruta de su archivo: ", end="   ")
        Listas = Lectura()
        OrganismoList = Listas['Organismos']
        MuestrasList = Listas['Muestras']
        CeldasVivasList = Listas['CeldasVivas']
           
        # ♥  PEDIR LA RUTA DEL ARCHIVO POR LEER 

    elif opc == "2":
        print()

        MuestrasList.MuestrasDisponibles()
        print()
        print("Ingrese el codigo de la muestra que desea ver:  ", end="  ")
        Cod =input()
        print()
        Info = MuestrasList.InfoTablero(Cod)
        F = Info['Filas']
        C = Info['Columnas']
        print(F,C)        
        print("FIN PRUEBA")
        CrearTablero(Cod,F,C)
        print("sdjkhdih")
        CeldasVivasList.LLenarTableroJ(Cod,int(F),int(C))
        Tab = Imprimir()
        TabMues = Tab['Tablero']
        GeneraGrafica(F,C,TabMues,OrganismoList)

    elif opc == "3":
        print("Actualizar Muestra ")
        print()
        MuestrasList.Imprimir()    
        print("Ingrese el codigo de la muestra que desea modificar: ", end="   ")
        CodM = input()
        Existe_M = MuestrasList.Actualizar(CodM)
        Estado_Mu = Existe_M['EstadoM']
        if Estado_Mu == False:
            print("Existe")
            ActualizarMuest(CodM)

        else: 
            print("Error la muestra no existe")
    
    elif opc == "4":
        # ♦ Preguntar si esta seguro de borrar los datos, si no lo esta mostrar un mensaje diciendo usted ha decidido no inicializar nada y luego volver a mostra menu 
        print("Usted ha inicializado el programa")
        OrganismoList.Inicializar()   
        MuestrasList.Inicializar()
        CeldasVivasList.Inicializar()


    elif opc== "5":
        print("Reporte final de las actualizaciones de las celdas y muestras ") # ♠ aqui debe de ir el reporte xml con la info final 
        print("Ingrese la Ruta donde desea a guardar el documento: ", end="")
        RUTAA =input()
        print("Ingrese el nombre del archivo: ", end="  ")
        Name = input()
        Reporte(RUTAA, Name, OrganismoList,MuestrasList, CeldasVivasList)
    elif opc == "6":
        print("usted ha salido ")
    elif opc == "7":
        print("Ingrese el codigo de la muestra que va agregar: ", end="   ")
        CodNM = input()
        print()
        print("Ingrese la descripcion de la muestra que esta agregando: ", end="   ")
        DesNM = input()
        print()
        print("Ingrese la catidad de filas que va a tener la muestra que esta agregando: ", end="   ")
        FilasNM = input()
        print()
        print("Ingrese la cantidad de columnas que va a tener la muestra  que esta agregando: ", end="   ")
        ColumNM = input()
        print()
        ExtraerEstado = MuestrasList.Actualizar(CodNM)
        EstadoMu = ExtraerEstado['EstadoM']

        if EstadoMu == True:
            MuestrasList.Añadir(CodNM, DesNM, FilasNM, ColumNM)
            print("Desea agregar celdas vivas ", end="   ")
            ResSN = input()
            AgregarPosCeldas(FilasNM,ColumNM,CodNM)
            while ResSN!= ("N"or"n"):
                AgregarPosCeldas(FilasNM,ColumNM,CodNM)       
        else: 
            print("Error el codigo ingresado de la muestra existe, no se puede crear")    
        
        
    elif opc == "8" :
        print()
        OrganismoList.Imprimir()

        print("Ingrese el tipo de Organismo que desea colocar: ", end="     ")
        TipeOr = input()
        MuestrasList.MuestrasDisponibles()
        print("Ingrese el codigo de la muestra donde desee colocar el organismo:", end="    ")
        Cod_Mu = input()
        InfTab = MuestrasList.InfoTablero(Cod_Mu)
        F_tot = int(InfTab["Filas"])
        C_tot = int(InfTab['Columnas'])
        print("Ingrese la posicion de la fila donde desea colocar el organismo: ", end="   ")
        PosFN = input()
        print("Ingrese el numero de columna donde desea  colocar el organismo: ", end="   ")
        PosCN= input()
        ColocarOrganismo(TipeOr,Cod_Mu,PosFN,PosCN,F_tot,C_tot,CeldasVivasList)
        
    elif opc == "9":
        pass



    else:
        print("opcion erronea")

def AgregarPosCeldas(FilaT, ColuT, ideM):
    global ResSN
    if ResSN == ("S"or "s"):
        print("Ingrese la posicion de la fila donde desee agregar el organismo:  ", end="   " )
        PosF = input()
        print()
        print("Ingrese la posicion de la columna donde desee agregar el organismo:  ", end="  ")        
        PosC = input()
        if (int(PosF)<int(FilaT+1))and(int(PosC)<int(ColuT+1))and(int(PosF)>0 )and(int(PosC)>0):
            print("Ingrese el tipo de organimos que desea agregar: ", end="  ")
            TipoOr = input()
            BuscarId =  OrganismoList.BuscarOr(TipoOr)
            Id_Or = BuscarId['EstadoO']
            if Id_Or :
                print("ERROR el organismo que desea agregar no existe ")
            elif not Id_Or :
                CeldasVivasList.Añadir(ideM,TipoOr, PosF, PosC)
                print("Desea agregar otra celda viva")
                ResSN = input()
        else:
            
            print("ERROR AL INGRESAR LA POSICION DE LAS CELDAS")
      

    
def CrearMuestra():
    print("Creando Una Muestra •••")
    print()
    print("Ingrese el Codigo de la Muestra ")

def ActualizarMuest(id):
    print("         Menu Actualizar          |")
    print("A. Descripcion                    |")
    print("B. Codigo                         |")
    print("C. Agregar Organismo a una celda  |")
    print("D. Regresar                       |")
    print("___________________________________")
    print()
    print("Ingrese la letra de la opcion que desea realizar ", end="   ")
    OpcAc = input()
    print()
    if OpcAc ==("A" or "a"):
        print("Ingrese la descripcion que desea cambiar ")
        Desc =input()
        MuestrasList.ActualizarDes(id,Desc)
    elif OpcAc == ("B" or "b"):
        print("El Codigo que va a cambiar es:  ", id)
        print("Ingrese el nuevo Codigo de esa Muestra:  ", end="      ")
        CodNuev = input()
        MuestrasList.ActualizarId(id,CodNuev)
        CeldasVivasList.ActualizarIdM(id, CodNuev)
    elif OpcAc== ("D" or "d"):
        print("← Regresando •••")
    else: 
        print("ERORRR")
        
    pass

if __name__ == '__main__':
    while opc !="6":
        Menu()