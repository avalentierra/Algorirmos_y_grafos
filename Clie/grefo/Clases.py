import sys
import tkinter
import heapq
class grafo():
    def __init__(self):
        self.listav = []
        self.listaA = []
        #self.vertices = []
        #self.matriz_Adyac = [[None]*len(self.listav)]*len(self.listav)


    def __str__(self):
        return str(self.listav)
        return str(self.matrizA)

    def agregarVertice(self, v):
        self.listav.append(v)

    def agregarArista(self,a):
        self.listaA.append(a)
   
   
class vertice():
    def __init__(self, nombre, x, y):
        self.la = []
        self.ld = []
        self.nombre = nombre
        self.x = x
        self.y = y
        self.distancia = sys.maxsize
        self.visitado = False
        self.predecesor = None
        

    def __str__(self):
        return str(self.la)

    def vecino(self, ver_ad):
        self.la.append(ver_ad)

class arista():
    def __init__(self, frm, to, distancia, x1, y1, x2, y2):
        self.ld = []
        self.frm = frm
        self.to = to
        self.distancia = distancia
        #self.bloqueo = False
        self.var = tkinter.IntVar()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2