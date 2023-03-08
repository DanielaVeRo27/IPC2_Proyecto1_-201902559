class Nodo_Muestra:
    def __init__(self,Id_M,Descripcion,Filas, Columnas):
        self.IdM = Id_M
        self.Des = Descripcion
        self.N = Filas
        self.M = Columnas        
        self.siguiente = None

# MUESTRA -->  Rejillas o cuadriculas o TABLERO
class Lista_Muestra:
    def __init__(self) -> None:
        self.head = None
        self.end = None
    def Añadir(self, Id_M, Des, N,M):
        NuevoNodo = Nodo_Muestra(Id_M, Des, N, M)
        if self.head == None:
            self.head = NuevoNodo
            self.end = NuevoNodo
        else:
            self.end.siguiente = NuevoNodo
            self.end = NuevoNodo

        pass

    def Imprimir(self):
        Temporal1 = self.head

        while Temporal1 != None:
            Filas_Total = Temporal1.N
            Columnas_Total = Temporal1.M
            print("| Codigo: "+str(Temporal1.IdM),end="    ")
            print("| Descripcion: "+str(Temporal1.Des), end="   ")
            print("| Filas: "+Temporal1.N, end="     ")
            print("| Columnas: "+Temporal1.M )

            Temporal1 = Temporal1.siguiente
    
        return {'FilasT' : Filas_Total,'ColumnasT':Columnas_Total}
    def MuestrasDisponibles(self):
        Temporal = self.head
        print()
        print("_•_○_•_○_•_○_•_○_•_○_•_○_•_○_•_○  Muestras Disponibles _•_○_•_○_•_○_•_○_•_○_•_○_•_○_•_○")

        while Temporal!= None:
            print("-----------------------------------------------------------------------------------------")
            print("|    "+"Codigo:    " + str(Temporal.IdM),end="      ")
            print("| Descripcion: "+str(Temporal.Des))
            Temporal = Temporal.siguiente    
            print("-----------------------------------------------------------------------------------------")
        print("_•_○_•_○_•_○_•_○_•_○_•_○_•_○_•_○ _•_○_•_○_•_○_•_○_•_○_•_○_•_○_•_○ _•_○_•_○_•_○_•_○_•_○_•")
    def Inicializar(self):
        while self.head != None:
            self.head = None
            self.head = self.head
    def InfoTablero(self, ID_Muestra):
        Temporal = self.head

        while Temporal != None:
            if Temporal.IdM == ID_Muestra:
                Cant_F = Temporal.N
                Cant_M = Temporal.M
                break
            Temporal = Temporal.siguiente

        return {"Filas" : Cant_F, "Columnas": Cant_M }

    def Actualizar(self, Id):
        Temporal = self.head
        EstadoMuestra= True
        while Temporal !=None:
            if Temporal.IdM == Id :
                EstadoMuestra = False
                break
            Temporal = Temporal.siguiente

        return{'EstadoM' : EstadoMuestra}

    def ActualizarDes(self, Id, Desc):
        Temporal = self.head
        EstadoMuestra= True
        while Temporal !=None:
            if Temporal.IdM == Id :
                Temporal.Des = Desc
                break
            Temporal = Temporal.siguiente  
        pass
    def ActualizarId(self, Id, IdNuevo):
        Temporal = self.head
        EstadoMuestra= True
        while Temporal !=None:
            if Temporal.IdM == Id :
                Temporal.IdM = IdNuevo
                break
            Temporal = Temporal.siguiente  
        pass
    def Inicializar(self):
        while self.head != None:
            self.head = None
            self.head = self.head