from Listas_Celdas import Lista_Celdas
from Listas_Celdas import Lista_Auxiliar

from Graficar import GeneraGrafica

def CrearTablero(IdeMuestra, NT, CT):           # NT→ filas en Total, CT→ Total de Columnas
    global Tablero
    Tablero = Lista_Celdas()
    FM = int(NT)
    CM = int(CT)

    for i in range(FM):    
        NombreLista = Lista_Celdas()
        for j in range(CM):
            NombreLista.Añadir(0)
        Tablero.Añadir(NombreLista)
    
    
    
    pass
def LlenarTablero(PosF, PosC, Tipo,F,C):
    global TotF, TotC
    TotF = F
    TotC = C
    Tablero.Modificar_Nodos(PosF,PosC,Tipo,F,C)
    return Tablero
    pass
def ColocarOrganismo(TipoOr, IdM , Fila, Columna,F_tot,C_tot,Lista):
    if (int(Fila)<int(F_tot))and (int(Columna)<int(C_tot)):
        Estado = True
        CrearTablero(IdM,int(F_tot),int(C_tot))
        Lista.LLenarTableroJ(IdM,F_tot,C_tot)
        ValorC =Tablero.Leer_Nodos(int(Fila),int(Columna))
        if ValorC['Valor'] ==0:
            print("se puede sustituir")
            Tablero.Modificar_Nodos(int(Fila),int(Columna), TipoOr,int(F_tot),int(C_tot))
            DNO(int(Fila),int(Columna),TipoOr,F_tot,C_tot,IdM,Lista)
            DNE(int(Fila),int(Columna),TipoOr,F_tot,C_tot,IdM,Lista)
            DSO(int(Fila),int(Columna),TipoOr,F_tot,C_tot,IdM,Lista)
            DSE(int(Fila),int(Columna),TipoOr,F_tot,C_tot,IdM,Lista)
            VN(int(Fila),int(Columna),TipoOr,F_tot,C_tot,IdM,Lista)
            VS(int(Fila),int(Columna),TipoOr,F_tot,C_tot,IdM,Lista)
            HO(int(Fila),int(Columna),TipoOr,F_tot,C_tot,IdM,Lista)
            HE(int(Fila),int(Columna),TipoOr,F_tot,C_tot,IdM,Lista)
            print(TipoOr)

        else:
            print("Celda ocupada")
            #break
            pass
    else:
        print("Error al ingresar la posiciones de la celada")
    return {'ListaAc':Lista}
def Imprimir():
    Tablero.Imprimir_Celdas()
    #GeneraGrafica(TotF,TotC,Tablero)

    return {"Tablero": Tablero}

# --------------------------------------------------------------- MOVIMIENTOS PERMITIDOS ------------------------------------------------------------------------
def DNO(F,C,Tipo,FTo,CTo, IdM,listaO):      
   CeldasInt1 = Lista_Auxiliar()
   if (F > 2) and (C>2):
      PosF = F-1
      PosC = C-1
      ContInt = 0         
      while (PosF > 0) and (PosC > 0):        
         Vacia =Tablero.Leer_Nodos(PosF,PosC)   
         if Vacia['Valor'] == 0:               
            Reprod = False
            break
         else:
            print("tipo "+str(Tipo))
            if Vacia['Valor'] == Tipo:
               if ContInt > 0:   
                  CeldasInt1.Imprimir_Ac()     
                  for m in range(ContInt):
                     PosF1 = CeldasInt1.Leer_Nodo(m+1)
                     Tablero.Modificar_Nodos(int(PosF1['PosF']),int(PosF1['PosC']),Tipo,int(FTo),int(CTo))
                     FILA = int(PosF1['PosF'])
                     COLU = int(PosF1['PosC'])
                     listaO.Añadir(IdM,Tipo,F,C)                     
                     print("entrando1")         
                     listaO.ActualizarCelda(IdM,int(PosF1['PosF']),int(PosF1['PosC']),Tipo)
                     
                     
               break
            else:
               CeldasInt1.Añadir(PosF,PosC)
               ContInt += 1      
         PosF -= 1
         PosC -= 1      
def DNE(F,C,Tipo,FTo,CTo, IdM,listaO):      
   CeldasInt2 = Lista_Auxiliar()
   if (F > 2) and (C<CTo-1):
      PosF = F-1
      PosC = C+1
      ContInt = 0         
      while (PosF > 0) and (PosC > 0):        
         Vacia =Tablero.Leer_Nodos(PosF,PosC)   
         if Vacia['Valor'] == 0:               
            Reprod = False
         else:
            if Vacia['Valor'] == Tipo:
               if ContInt > 0:   
                  CeldasInt2.Imprimir_Ac()     
                  for m in range(ContInt):
                     PosF1 = CeldasInt2.Leer_Nodo(m+1)
                     Tablero.Modificar_Nodos(int(PosF1['PosF']),int(PosF1['PosC']),Tipo,int(FTo),int(CTo))
                     FILA = int(PosF1['PosF'])
                     COLU = int(PosF1['PosC'])
                     listaO.Añadir(IdM,Tipo,F,C)
                     listaO.ActualizarCelda(IdM,int(PosF1['PosF']),int(PosF1['PosC']),Tipo)    
               break
            else:
               CeldasInt2.Añadir(PosF,PosC)
               ContInt += 1      
         PosF -= 1
         PosC += 1  
def DSO(F,C,Tipo,FTo,CTo, IdM,listaO):      
   CeldasInt3 = Lista_Auxiliar()
   if (F < FTo-1) and (C>2):
      PosF = F+1
      PosC = C-1
      ContInt = 0         
      while (PosF > 0) and (PosC > 0):        
         Vacia =Tablero.Leer_Nodos(PosF,PosC)   
         if Vacia['Valor'] == 0:               
            Reprod = False
            break
         else:
            if Vacia['Valor'] == Tipo:
               if ContInt > 0:   
                  CeldasInt3.Imprimir_Ac()     
                  for m in range(ContInt):
                     PosF1 = CeldasInt3.Leer_Nodo(m+1)
                     Tablero.Modificar_Nodos(int(PosF1['PosF']),int(PosF1['PosC']),Tipo,int(FTo),int(CTo))
                     FILA = int(PosF1['PosF'])
                     COLU = int(PosF1['PosC'])
                     listaO.Añadir(IdM,Tipo,F,C)
                     listaO.ActualizarCelda(IdM,int(PosF1['PosF']),int(PosF1['PosC']),Tipo)
               break
            else:
               CeldasInt3.Añadir(PosF,PosC)
               ContInt += 1      
         PosF += 1
         PosC -= 1  
def DSE(F,C,Tipo,FTo,CTo, IdM,listaO):      
   CeldasInt4 = Lista_Auxiliar()
   if (F < FTo-1) and (C<CTo-1):
      PosF = F+1
      PosC = C+1
      ContInt = 0         
      while (PosF > 0) and (PosC > 0):        
         Vacia =Tablero.Leer_Nodos(PosF,PosC)   
         if Vacia['Valor'] == 0:               
            Reprod = False
            break
         else:
            print("tipo "+str(Tipo))
            if Vacia['Valor'] == Tipo:
               if ContInt > 0:   
                  CeldasInt4.Imprimir_Ac()     
                  for m in range(ContInt):
                     PosF1 = CeldasInt4.Leer_Nodo(m+1)
                     Tablero.Modificar_Nodos(int(PosF1['PosF']),int(PosF1['PosC']),Tipo,int(FTo),int(CTo))
                     FILA = int(PosF1['PosF'])
                     COLU = int(PosF1['PosC'])                     
                     listaO.Añadir(IdM,Tipo,F,C)
                     listaO.ActualizarCelda(IdM,int(PosF1['PosF']),int(PosF1['PosC']),Tipo)
                     
                     print("entrando1")
               break
            else:
               CeldasInt4.Añadir(PosF,PosC)
               ContInt += 1      
         PosF += 1
         PosC += 1 
def VN(F,C,Tipo,FTo,CTo, IdM,listaO):      
   CeldasInt5 = Lista_Auxiliar()
   if (F > 2) and (C>0):
      PosF = F-1
      PosC = C
      ContInt = 0         
      while (PosF > 0) and (PosC > 0):        
         
         Vacia =Tablero.Leer_Nodos(PosF,PosC)   
         if Vacia['Valor'] == 0:               
            Reprod = False
            break
         else:
            if Vacia['Valor'] == Tipo:
               if ContInt > 0:   
                  CeldasInt5.Imprimir_Ac()     
                  for m in range(ContInt):
                     PosF1 = CeldasInt5.Leer_Nodo(m+1)
                     Tablero.Modificar_Nodos(int(PosF1['PosF']),int(PosF1['PosC']),Tipo,int(FTo),int(CTo))
                     FILA = int(PosF1['PosF'])
                     COLU = int(PosF1['PosC'])
                     listaO.Añadir(IdM,Tipo,F,C)
                     listaO.ActualizarCelda(IdM,int(PosF1['PosF']),int(PosF1['PosC']),Tipo)
                     
                     
               break
            else:
               CeldasInt5.Añadir(PosF,PosC)
               ContInt += 1      
         PosF -= 1
         PosC = PosC 
def VS(F,C,Tipo,FTo,CTo, IdM,listaO):      
   CeldasInt6 = Lista_Auxiliar()
   if (F < FTo-1) and (C>0):
      print("Meto vs ")
      PosF = F+1
      PosC = C
      ContInt = 0         
      while (PosF > 0) and (PosC > 0):        
         Vacia =Tablero.Leer_Nodos(PosF,PosC)   
         if Vacia['Valor'] == 0:               
            Reprod = False
            break
         else:
            if Vacia['Valor'] == Tipo:
               if ContInt > 0:   
                  CeldasInt6.Imprimir_Ac()     
                  for m in range(ContInt):
                     PosF1 = CeldasInt6.Leer_Nodo(m+1)
                     Tablero.Modificar_Nodos(int(PosF1['PosF']),int(PosF1['PosC']),Tipo,int(FTo),int(CTo))
                     FILA = int(PosF1['PosF'])
                     COLU = int(PosF1['PosC'])          
                     listaO.Añadir(IdM,Tipo,F,C)
                     listaO.ActualizarCelda(IdM,int(PosF1['PosF']),int(PosF1['PosC']),Tipo)
                     
                     
               break
            else:
               CeldasInt6.Añadir(PosF,PosC)
               ContInt += 1      
         PosF += 1
         PosC = PosC 
def HO(F,C,Tipo,FTo,CTo, IdM,listaO):      
   CeldasInt7 = Lista_Auxiliar()
   if (F > 0) and (C>2):
      PosF = F
      PosC = C-1
      ContInt = 0         
      while (PosF > 0) and (PosC > 0):        
         Vacia =Tablero.Leer_Nodos(PosF,PosC)   
         if Vacia['Valor'] == 0:               
            Reprod = False
            break
         else:
            if Vacia['Valor'] == Tipo:
               if ContInt > 0:   
                  CeldasInt7.Imprimir_Ac()     
                  for m in range(ContInt):
                     PosF1 = CeldasInt7.Leer_Nodo(m+1)
                     Tablero.Modificar_Nodos(int(PosF1['PosF']),int(PosF1['PosC']),Tipo,int(FTo),int(CTo))
                     FILA = int(PosF1['PosF'])
                     COLU = int(PosF1['PosC'])                
                     listaO.Añadir(IdM,Tipo,F,C)
                     listaO.ActualizarCelda(IdM,int(PosF1['PosF']),int(PosF1['PosC']),Tipo)
                     
                     
               break
            else:
               CeldasInt7.Añadir(PosF,PosC)
               ContInt += 1      
         PosF = PosF
         PosC -=1  
def HE(F,C,Tipo,FTo,CTo, IdM,listaO):      
   CeldasInt8 = Lista_Auxiliar()
   if (F > 0) and (C<CTo-1):
      PosF = F
      PosC = C+1
      ContInt = 0         
      while (PosF > 0) and (PosC > 0):        
         Vacia =Tablero.Leer_Nodos(PosF,PosC)   
         if Vacia['Valor'] == 0:               
            Reprod = False
            break
         else:
            if Vacia['Valor'] == Tipo:
               if ContInt > 0:   
                  CeldasInt8.Imprimir_Ac()     
                  for m in range(ContInt):
                     PosF1 = CeldasInt8.Leer_Nodo(m+1)
                     Tablero.Modificar_Nodos(int(PosF1['PosF']),int(PosF1['PosC']),Tipo,int(FTo),int(CTo))
                     FILA = int(PosF1['PosF'])
                     COLU = int(PosF1['PosC'])                    
                     listaO.Añadir(IdM,Tipo,F,C)     
                     listaO.ActualizarCelda(IdM,int(PosF1['PosF']),int(PosF1['PosC']),Tipo)
                     
                     
               break
            else:
               CeldasInt8.Añadir(PosF,PosC)
               ContInt += 1      
         PosF = PosF
         PosC +=1  