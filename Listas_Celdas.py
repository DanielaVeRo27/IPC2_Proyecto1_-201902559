"""  
Lista donde se crea y se modifica el tablero, y se maneja 
"""


class Nodo_Celda:
    def __init__(self, C1):
        self.C1 = C1
        self.siguiente = None
        pass
class Nodo_Auxiliar:
    def __init__(self,IdA, Actor):        
        self.IdA = IdA
        self.Actor = Actor
        self.siguente = None 
class Lista_Celdas:
    def __init__(self) :
        self.head = None
        self.end = None 
    def Añadir(self, C1):
        NuevoNodo = Nodo_Celda(C1)
        if self.head == None:
            self.head = NuevoNodo
            self.end = NuevoNodo
        else:
            self.end.siguiente = NuevoNodo            
            self.end = NuevoNodo
    def Imprimir_Celdas(self):       
        Temporal = self.head
        while Temporal!= None:
            NodoA = Temporal.C1
            Temporal1 = NodoA.head
            while Temporal1 != None:
                #print(Temporal1.C1, end = " - ")                
                Temporal1 = Temporal1.siguiente
            #print("")    
            Temporal = Temporal.siguiente  

        
    def Modificar_Nodos(self,NLinea,NNodo,Tipo,F,C):       
        Temporal = self.head
        ContLineas = 0
        Existe = False
        Regreso = "0"
        #print("F-"+str(NLinea)+" C-"+str(NNodo))
        if (NLinea >0) and (NLinea < F):
            while Temporal!= None or ContLineas > (NLinea-1):
                if ContLineas == (NLinea-1):
                    Existe = True               
                    NuevaLinea = Temporal.C1
                    Temporal12 = NuevaLinea.head
                    ContNodos = 0
                    while (Temporal12 != None) or (ContNodos > (NNodo-1)):                        
                        if ContNodos == (NNodo-1):
                            Temporal12.C1 = Tipo  
                            break
                        ContNodos += 1                        
                        Temporal12 = Temporal12.siguiente
                    break
                ContLineas += 1
                Temporal = Temporal.siguiente               
        return {'Estado':Existe,'Valor':Regreso}
    def Leer_Nodos(self,NLinea,NNodo):       
        Temporal = self.head
        ContLineas = 0
        Existe = False
        Regreso = "0"
        #print("F-"+str(NLinea)+" C-"+str(NNodo))
        if (NLinea >0) and (NLinea < 30):
            while Temporal!= None or ContLineas > (NLinea-1):
                if ContLineas == (NLinea-1):
                    Existe = True               
                    NuevaLinea = Temporal.C1
                    Temporal12 = NuevaLinea.head
                    ContNodos = 0
                    while (Temporal12 != None) or (ContNodos > (NNodo-1)):                        
                        if ContNodos == (NNodo-1):
                            Regreso = Temporal12.C1      
                            break
                        ContNodos += 1                        
                        Temporal12 = Temporal12.siguiente
                    break
                ContLineas += 1
                Temporal = Temporal.siguiente               
        return {'Estado':Existe,'Valor':Regreso}


class Lista_Auxiliar:
    def __init__(self):      
        self.head = None 
        self.end = None 
    def Añadir(self, IdA,Actor):      
        nuevoNodo = Nodo_Auxiliar(IdA,Actor)
        if self.head == None:
            self.head = nuevoNodo
            self.end = nuevoNodo
        else:
            self.end.siguente = nuevoNodo            
            self.end = nuevoNodo
    def Imprimir_Ac(self):       
        Temporal = self.head
        print("-",end="")
        while Temporal!= None:
            print(str(Temporal.IdA) ,end= ",")
            print(str(Temporal.Actor))
            Temporal = Temporal.siguente   
        print(" ")    
    def Leer_Nodo(self,pos):       
        Temporal = self.head
        cont = 0
        PosF = 7
        PosC = 0
        print("--",end="")
        while (Temporal != None) or (cont > pos):
            cont += 1
            if cont == pos:
               PosF = Temporal.IdA
               PosC = Temporal.Actor    
               break  
            Temporal = Temporal.siguente   

        return {'PosF':PosF,'PosC':PosC}