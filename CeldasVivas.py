#C:\Users\Luisa\Documents\2023\Primer Semestre\Ipc 2\Proyecto1\EntradaEjemplo.XML
""" 
Lista donde se guarda la informacion de las celdas que van a estar vivas  de las muestras y ademas nos va a decir que tipo de 
organismos tiene esa celda   
"""
from Tablero import LlenarTablero

class Nodo_CV:
    def __init__(self,Id_M,Id_O,Fila_VM,Columna_VM,):
        self.IdM =Id_M
        self.IdO = Id_O
        self.FilaV = Fila_VM       # N → Fila          NV → Fila viva
        self.ColumnaV = Columna_VM    # M → Columnas      MV → ColumnaVviva
        self.siguiente = None

class list_CeldasVivas:

    def __init__(self):
        self.head = None
        self.end = None
    def Añadir(self, IdM,IdO,FV,CV):
        NuevoNodo = Nodo_CV(IdM, IdO, FV, CV)
        if self.head == None:
            self.head = NuevoNodo
            self.end = NuevoNodo
        else:
            self.end.siguiente = NuevoNodo
            self.end = NuevoNodo

        pass
    def imprimir(self):
        Temporal1 = self.head
        while Temporal1 != None:
            print("| Codigo Muestra: "+str(Temporal1.IdM),end="    ")
            print("| Fila: "+str(Temporal1.FilaV), end="   ")
            print("| Columna: "+Temporal1.ColumnaV, end="     ")
            print("| Codigo Organismo: "+Temporal1.IdO )
            Temporal1 =  Temporal1.siguiente
    def infoCeldas(self, id):
        Tempo = self.head
        cont =3
        while Tempo !=None:
            if Tempo.IdM == id:
                Tempo2 = Tempo
                print()
                print("Fila"+str(Tempo2.FilaV),end="   ")
                while Tempo2 !=None:
                    Tempo3 = Tempo2
                    cont = 4
                    print("f"+str(Tempo2.FilaV)+"C"+str(Tempo2.ColumnaV))
                    Tempo2 = Tempo2.siguiente
                   
                Tempo = Tempo.siguiente
            Tempo = Tempo.siguiente


    
    
    def BCeldasVivas (self, id,N,M):
        Temporal = self.head
        cont =1
        while Temporal !=None:
            if Temporal.IdM == id:
                Temporal2 = Temporal
                #print("Fila"+str(Temporal.FilaV) , end=" :  ")
                while Temporal2 != None:
                    if Temporal2.FilaV == Temporal.FilaV:
                        print(str(Temporal2.ColumnaV), end=" , ")
                        
                        Temporal2= Temporal2.siguiente    
                    #break
                
                print()                
            Temporal = Temporal.siguiente
            continue
    def LLenarTableroJ(self, Id_Muestra,F,C):
        Temporal = self.head
        while Temporal != None:
            if Temporal.IdM == str(Id_Muestra):
                LlenarTablero(int(Temporal.FilaV),int(Temporal.ColumnaV), Temporal.IdO,F,C)
            Temporal =Temporal.siguiente
    def ActualizarIdM(self, IdMues, IdMNew):
        Temporal = self.head
        while Temporal != None:
            if Temporal.IdM ==IdMues:
                Temporal.IdM = IdMNew
            Temporal = Temporal.siguiente  
    def ActualizarCelda(self, idM, F, C,idO):
        Temporal = self.head
        contador1 = 0
        while Temporal != None:
            contador1 += contador1
            if (Temporal.IdM == idM) :               
               F1 = str(Temporal.FilaV)
               C1 = str(Temporal.ColumnaV)                       
               if (F1 == str(F) ) and (C1 == str(C)):   
                  Temporal.IdO = idO
                
                #Temporal.IdM = IdMNew
            Temporal = Temporal.siguiente 

    def ActuaC(self, idm, Ido,F,C):
        Tempo = self.head
        cont =3
        while Tempo !=None:
            if Tempo.IdM == idm:
                Tempo2 = Tempo
                #print()
                #print("Fila"+str(Tempo2.FilaV),end="   ")
                while Tempo2 !=None:
                    if(Tempo2.FilaV == (int(F) or str(F) ))and(Tempo2.ColumnaV == (int(C) or str(C))):
                      Tempo2.IdO = Ido
                    Tempo2 = Tempo2.siguiente
                     
                
            Tempo = Tempo.siguiente



        """ Temporal = self.head
        print("--------------------------")
        print(F)
        while Temporal != None:
            print("FILA"+str(Temporal.FilaV))

            if Temporal.IdM == idm :
              print("Entroooooooo if 1")
              if (Temporal.FilaV==F):
                print("Entroooooooo if 2")
              if Temporal.ColumnaV==int(C):
                    print("Entroooooooo if 3")
            Temporal = Temporal.siguiente"""
        print("ASHDKASHDKJASHDJKAHSDJKASHDKJHASDJKHASD")
           


"""    def LLenarTableroJ(self, Id_Muestra):
        Temporal = self.head
        while Temporal != None:
            if Temporal.IdM == str(Id_Muestra):
                LlenarTablero(int(Temporal.FilaV),int(Temporal.ColumnaV), Temporal.IdO)
            Temporal =Temporal.siguiente"""