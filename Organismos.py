class Nodo_Organismo:
    def __init__(self,Id_O, Nombre,contOr):
        self.IdO = Id_O
        self.Nombre = Nombre
        self.ContOr = contOr
        self.siguiente = None
class Lista_Organismos:
    def __init__(self):
        self.head = None
        self.end = None
    def Añadir(self, Id, NombreO,ContOr):
        NuevoNodo = Nodo_Organismo(Id,NombreO, ContOr)
        if self.head == None:
            self.head = NuevoNodo
            self.end = NuevoNodo
        else:
            self.end.siguiente = NuevoNodo
            self.end = NuevoNodo
    def Imprimir(self):
        Temporal1 = self.head

        while Temporal1 != None:
            print("| Codigo: "+str(Temporal1.IdO),end="    ")
            print("| Nombre: "+str(Temporal1.Nombre))
            print("------------------------------------------------")
            Temporal1 = Temporal1.siguiente
    def Inicializar(self):
        while self.head != None:
            self.head = None
            self.head = self.head
            
    def BuscarOr(self, id):
        temporal = self.head
        EstadoOr  = True
        while temporal != None:
            if temporal.IdO == str(id):
                EstadoOr = False
                break
            temporal = temporal.siguiente
        return {'EstadoO': EstadoOr}

