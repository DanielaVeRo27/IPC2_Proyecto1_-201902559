from graphviz import Digraph
from  Listas_Celdas import Lista_Celdas
from  Organismos import Lista_Organismos
Organismos = {1:'green',2:'Blue',3:'red',4:'yellow',5:'gray',6:'brown',7:'pink',8:'violet',9:'lightgreen'}
def LeerColor(Organismo):
    Color = 'white'
    for clave in Organismos:
       if clave == Organismo:
           Color = Organismos[clave]
    return Color


def GeneraGrafica(F, C, Lista2=Lista_Celdas, lista3 = Lista_Organismos):
    dot = Digraph(name='Practica', node_attr={'shape': 'square'},format='pdf')
    dot.attr('node', shape ='box', height = '1.25', width = '2.5', fontsize = '30')
    Ultimo = 'N0'    
    Dato = Lista2.Leer_Nodos(1,1)   
    Id = Dato['Valor']
    InfoColor= Colores(lista3,Id)
    Color = LeerColor(InfoColor['Color'])
    dot.attr('node', style = 'filled',fillcolor =Color )   
    dot.node('N0')
    Filas = int(F)
    Columnas = int(C)
    Nodos = Filas*Columnas
    for i in range(Nodos):
        NNodos = "N"+str(i)        
        ValorC = i % Columnas
        ValorF = i // Columnas
        #print("Fila "+str(ValorF+1)+" Columna "+str(ValorC+1)+ " i = "+str(i), end = " ")
        Dato = Lista2.Leer_Nodos(ValorF+1,ValorC+1)   
        #print("Dato "+str(Dato['Valor']))
        Id = Dato['Valor']
        InfoColor= Colores(lista3,Id)
        Color = LeerColor(InfoColor['Color'])
        dot.attr('node', style = 'filled',fillcolor = Color)    
        dot.node(NNodos, 'F'+str(ValorF+1)+ ' C'+str(ValorC+1))
        Ultimo = NNodos

    for i in range(Columnas):
       Ultimo = 'N'+str(i)
       for j in range(Filas-1):
           NNodos = "N"+str(Columnas*(j+1)+i)
           dot.edge(Ultimo,NNodos)
           Ultimo = NNodos
    dot.render('test-output/round-table.gv', view=True)  
def Colores(self,Datos):
    Temporal = self.head
    Color2 =""
    while Temporal != None:
        if Temporal.IdO == Datos:
            Color2 = Temporal.ContOr
        Temporal = Temporal.siguiente
    return {'Color':Color2}
"""def Graficar(F, C, Lista2=Lista_Celdas, lista3 = Lista_Organismos):
    dot = Digraph(name='Practica', node_attr={'shape': 'square'},format='pdf')
    dot.attr('node', shape ='box', height = '1.25', width = '2.5', fontsize = '30')
    Ultimo = 'N0'   
    def Colores(self,Datos):
        Temporal = self.head
        Dato = Lista2.Leer_Nodos(1,1)   
        Color = LeerColor(Dato['Valor'])
        while Temporal != None:
            if Temporal.IdO == Dato['Valor']:
                Color = LeerColor(Temporal.ContOr)
            Temporal = Temporal.siguiente
        
        
        dot.attr('node', style = 'filled',fillcolor = Color)   
        dot.node('N0')"""