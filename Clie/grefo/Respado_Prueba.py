from __future__ import division
from encodings import utf_8
from re import sub

from reportlab.pdfgen import canvas
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
#from scipy.misc import imread
from matplotlib.pyplot import imread
#import imagio
import os
import numpy as np

from pathlib import Path

from reportlab.lib.units import inch, cm
from os import remove
from numpy import matrix
import pymongo
import numpy as np
import xml.etree.ElementTree as ET
from turtle import bgcolor
from fpdf import FPDF 
from matplotlib import widgets

from sklearn.metrics import balanced_accuracy_score, jaccard_score
from grefo.Clases import *
from grefo.ClaseNodo import *
import json
from tkinter.filedialog import *
from tkinter import messagebox
import math
import openpyxl
from tkinter import scrolledtext
  
import time
import os
from threading import Thread
from tkinter import *
from PIL import Image, ImageTk,ImageDraw
import random
from reportlab.pdfgen import *
import tkinter as tk
from cProfile import label
from cgitb import text
from cgitb import text
Ventana = tk.Tk()
#Ventana.state("zoomed")
Ventana.geometry("750x650")
Ventana.title("Grafos")
Ventana.iconbitmap('Clie\cp-logo.ico')
canvas3 = Canvas(Ventana, width=400, height=450, bg="#B3B6B7")#taget
canvas3.pack(fill=BOTH, expand=YES)







#ancho = 40
li = []


white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0,128,0)



width = 550
height = 570
center = height//2


#image1 = Image.new("RGB", (width, height), white)
image2 = Image.new("RGB", (width+150, height+50), white)
#draw = ImageDraw.Draw(image1)
draw2= ImageDraw.Draw(image2)


canvas3.postscript(file="my_drawing.ps", colormode='color')
# Crear Grafo
g = grafo()
l = []
img = Image.open(os.path.join(r'C:\Users\RUPERTO\OneDrive\Escritorio\g\data\Clie\bola.png'))
#img = Image.open('bola.png')
bola = ImageTk.PhotoImage(img)


# Informacion del vertice
def click(event):
    for vert in g.listav:
        if event.x > vert.x and event.x < vert.x + ancho and event.y > vert.y and event.y < vert.y + ancho:
            info = Toplevel()
            info.title("Informacion del Punto")
            l1 = Label(info, text="Nombre:").grid(row=0, column=0)
            l2 = Label(info, text=vert.nombre).grid(row=0, column=1)
         





# Agregar vertice al mapa
def dobleclick(event):
    # Ingresar Vertice
    ingreso = Toplevel()
    ingreso.title("Agregar Punto")
    tnombre = Label(ingreso, text="Ingrese nombre del vertice:")
    tnombre.grid(row=0, column=0)
    nombrev = Entry(ingreso)
    nombrev.grid(row=0, column=1)
    
    agregar = Button(ingreso, text="Agregar",
                     command=lambda: agregarv(event.x, event.y, nombrev.get(), ingreso))
    agregar.grid(row=3, columnspan=2)

def agregarv(x, y, nombre, ingreso):
    try:

        gradoa = float(100)
        if (gradoa < 1 ):
            ingreso.destroy()
            #messagebox.showerror("ERROR", "El grado de accidentalidad no esta permitido")
        else:
            vtemp = vertice(nombre, x, y)
            g.agregarVertice(vtemp)
            ingreso.destroy()
            actualizar()
    except ValueError:
        ingreso.destroy()
       # messagebox.showerror("ERROR", "Usted no digito un grado de accidentalidad correcto")

def agregarA(frm, to, distancia, x1, y1, x2, y2):
    atemp = arista(frm, to, distancia, x1, y1, x2, y2)
    g.agregarArista(atemp)
    actualizar()



# Relacionar vertices
def clickrelacion():
    vrelacion = Toplevel()
    vrelacion.title("Agregar Ruta")
    opciones1 = Listbox(vrelacion, exportselection=0)
    opciones2 = Listbox(vrelacion, exportselection=0)
    for v in g.listav:
        opciones1.insert(END, v.nombre)
        opciones2.insert(END, v.nombre)
    opciones1.pack(side=LEFT)
    opciones2.pack(side=LEFT)
    #t1 = Label(vrelacion, text="Desde")
    #t1.pack()
    #nv1 = Entry(vrelacion)
    #nv1.pack()
    #t2 = Label(vrelacion, text="Hasta")
    #t2.pack()
    #nv2 = Entry(vrelacion)
    #nv2.pack()
    t3=Label(vrelacion, text="Ingrese el peso")
    t3.pack()
    nv3=Entry(vrelacion)
    nv3.pack()
    #relacionar = Button(vrelacion, text="Relacionar", command=lambda: relacion(nv1.get(), nv2.get(), vrelacion))
   # relacionar.pack()
   
    relacionar2 = Button(vrelacion, text="Dirigida",
                         command=lambda: relacion(opciones1.get(opciones1.curselection()),
                                                  opciones2.get(opciones2.curselection()),nv3.get(), vrelacion))
    relacionar2.pack()
    relacionar3 = Button(vrelacion, text="No Dirijida",
                         command=lambda: relacion_No_Dirijida(opciones1.get(opciones1.curselection()),
                                                  opciones2.get(opciones2.curselection()),nv3.get(), vrelacion))
    relacionar3.pack()

def relacion(nv1, nv2,nv3, vrelacion):
    if (nv1 == nv2):
        vrelacion.destroy()
        messagebox.showinfo("Denegado", "No puede seleccionar el mismo vertice")
    else:

        for v in g.listav:
            if (nv1 == v.nombre):
                a = v
                for v in g.listav:
                    if (nv2 == v.nombre):
                        b = v
                        a.vecino(b)
                        d = int(nv3)
                        agregarA(a, b, d, a.x, a.y, b.x, b.y)
                        vrelacion.destroy()
        
        actualizar()

def relacion(nv1, nv2,nv3, vrelacion):
    #if (nv1 == nv2):
     #   vrelacion.destroy()
      #  messagebox.showinfo("Denegado", "No puede seleccionar el mismo punto de interes")
    #else:

        for v in g.listav:
            if (nv1 == v.nombre):
                a = v
                for v in g.listav:
                    if (nv2 == v.nombre):
                        b = v
                        a.vecino(b)
                        d = int(nv3)
                        agregarA(a, b, d, a.x, a.y, b.x, b.y)
                        vrelacion.destroy()
        
        actualizar()

def relacion_No_Dirijida(nv1, nv2,nv3, vrelacion):
    if (nv1 == nv2):
        vrelacion.destroy()
        messagebox.showinfo("Denegado", "No puede seleccionar el mismo punto de interes")
    else:

        for v in g.listav:
            if (nv1 == v.nombre):
                a = v
                for v in g.listav:
                    if (nv2 == v.nombre):
                        b = v
                        a.vecino(b)
                        d = int(nv3)
                        agregarA(a, b, d, a.x, a.y, b.x, b.y)
                        
                        vrelacion.destroy()
        relacion(nv2,nv1,nv3,vrelacion)
        actualizar()





# Eliminar Vertices
def clickeliminarv():
    veliminar = Toplevel()
    veliminar.title("Eliminar Punto")
    t1 = Label(veliminar, text="Nombre punto de interes")
    t1.pack()
    opciones = Listbox(veliminar, exportselection=0)
    for v in g.listav:
        opciones.insert(END, v.nombre)
    opciones.pack()
    nombrev = Entry(veliminar)
    nombrev.pack()
    eliminar = Button(veliminar, text="Eliminar", command=lambda: eliminarv(nombrev.get(), veliminar))
    eliminar.pack()
    eliminar2 = Button(veliminar, text="Elimina desde listas",
                       command=lambda: eliminarv(opciones.get(opciones.curselection()), veliminar))
    eliminar2.pack()

def eliminarv(nombrev, veliminar):
    try:
        for v in g.listav:
            if (nombrev == v.nombre):
                a = v
            for i in v.la:
                if (nombrev == i.nombre):
                    b = i
                    v.la.remove(b)
        g.listav.remove(a)
        c = 0
        indice = []
        for a in g.listaA:
            if nombrev == a.frm.nombre or nombrev == a.to.nombre:
                c += 1
                indice.append(g.listaA.index(a))
        for i in reversed(indice):  # sorted(indice, reverse=True)
            del g.listaA[i]
        veliminar.destroy()
        actualizar()
    except:
        veliminar.destroy()
        messagebox.showerror("ERROR", "El punto no se encuentra")

# Eliminar Aristas
def clickeliminara():
    veliminara = Toplevel()
    veliminara.title("Eliminar Ruta")
    desde = Listbox(veliminara, exportselection=0)
    hasta = Listbox(veliminara, exportselection=0)
    for v in g.listav:
        desde.insert(END, v.nombre)
        hasta.insert(END, v.nombre)
    desde.pack(side=LEFT)
    hasta.pack(side=LEFT)
    t1 = Label(veliminara, text="Desde")
    t1.pack()
    nv1 = Entry(veliminara)
    nv1.pack()
    t2 = Label(veliminara, text="Hasta")
    t2.pack()
    nv2 = Entry(veliminara)
    nv2.pack()
    eliminar = Button(veliminara, text="Eliminar", command=lambda: eliminara(nv1.get(), nv2.get(), veliminara))
    eliminar.pack()
    eliminar2 = Button(veliminara, text="Eliminar desde listas",
                       command=lambda: eliminara(desde.get(desde.curselection()), hasta.get(hasta.curselection()),
                                                 veliminara))
    eliminar2.pack()

def eliminara(desde, hasta, veliminara):
    try:
        for v in g.listav:
            if (desde == v.nombre):
                a = v
                for i in a.la:
                    if (hasta == i.nombre):
                        b = i
                        a.la.remove(b)
        for ar in g.listaA:
            if (desde == ar.frm.nombre and hasta == ar.to.nombre):
                temp = ar
                g.listaA.remove(temp)
        veliminara.destroy()
        actualizar()
    except:
        print("No elimina ruta")

# Calcular Distancias
def distancias(a, b):
    
    distancia = math.sqrt(math.pow(b.x - a.x, 2) + math.pow(b.y - a.y, 2))
    return round(distancia, 2)


# Dijkstra
def clickdijkstra():
    vdijkstra = Toplevel()
    vdijkstra.title("Rutas Mas Cortas")
    t1 = Label(vdijkstra, text="Nombre del punto")
    t1.pack()
    opciones = Listbox(vdijkstra, exportselection=0)
    for v in g.listav:
        opciones.insert(END, v.nombre)
    opciones.pack()
    eliminar = Button(vdijkstra, text="Calcular Distancia",
                      command=lambda: dijkstra(opciones.get(opciones.curselection()), vdijkstra))
    eliminar.pack()

def dijkstra(inicio, vdijkstra):
    for i in g.listav:
        if inicio == i.nombre:
            indice = i
    listad, listap = g.dijkstra(indice) ###################################################### Verificar aqui
    if (len(indice.la) == 0):
        messagebox.showinfo("Dijkstra", "El punto seleccionado no tiene rutas")
    else:
        resaltarcaminos(listap, li, indice)
        vdijkstra.destroy()
        mostrardijkstra = Toplevel()
        mostrardijkstra.title("Distancias")
        t1 = Label(mostrardijkstra, text="Distancia de las rutas desde %s : " % (inicio.upper()), font="Verdana 10 bold")
        t1.pack()
        for i in range(len(g.listav)):
            if (listap[i] != None):
                dista = str(listad[i])
                hastaa = g.listav[i].nombre
                hastaa = hastaa.upper()
                dista = dista[0:6]
                t2 = Label(mostrardijkstra, text=" hasta " + hastaa + " es: " + dista+"m")
                t2.pack()

# Resaltar Caminos del Dijkstra
def resaltarcaminos(listap, li, inicio):
    for aris in li:
        canvas3.delete(aris)
    del li[:]
    h1 = Thread(target=resaltar, args=(listap, li, inicio))
    h1.start()

def resaltar(listap, li, inicio):
    num = ancho / 2
    for i in range(len(g.listav)):
        if listap[i] != None and listap[i].nombre == inicio.nombre:
            time.sleep(0.5)
            if (listap[i].x >= g.listav[i].x and listap[i].y > g.listav[i].y):
                a = canvas3.create_line(listap[i].x + num, listap[i].y, g.listav[i].x + ancho, g.listav[i].y + num,
                                       width=3, fill="DarkGoldenrod1", arrow="last", smooth=True)
                li.append(a)
            if (listap[i].x > g.listav[i].x and listap[i].y < g.listav[i].y):
                a = canvas3.create_line(listap[i].x + num, listap[i].y + ancho, g.listav[i].x + ancho,
                                       g.listav[i].y + num, width=3, fill="DarkGoldenrod1", arrow="last", smooth=True)
                li.append(a)
            if (listap[i].x <= g.listav[i].x and listap[i].y > g.listav[i].y):
                a = canvas3.create_line(listap[i].x + num, listap[i].y, g.listav[i].x, g.listav[i].y + num, width=3,
                                       fill="DarkGoldenrod1", arrow="last", smooth=True)
                li.append(a)
            if (listap[i].x < g.listav[i].x and listap[i].y < g.listav[i].y):
                a = canvas3.create_line(listap[i].x + num, listap[i].y + ancho, g.listav[i].x, g.listav[i].y + num,
                                       width=3, fill="DarkGoldenrod1", arrow="last", smooth=True)
                li.append(a)
            resaltar(listap, li, g.listav[i])

# Camino
def clickcamino():
    vcamino = Toplevel()
    vcamino.title("Mostrar Ruta")
    desde = Listbox(vcamino, exportselection=0)
    hasta = Listbox(vcamino, exportselection=0)
    for v in g.listav:
        desde.insert(END, v.nombre)
        hasta.insert(END, v.nombre)
    desde.grid(row=1, column=0)
    hasta.grid(row=1, column=1)
    t1 = Label(vcamino, text="Desde")
    t1.grid(row=0, column=0)
    t2 = Label(vcamino, text="Hasta")
    t2.grid(row=0, column=1)
    caminob = Button(vcamino, text="Camino",
                     command=lambda: camino(desde.get(desde.curselection()), hasta.get(hasta.curselection()), vcamino))
    caminob.grid(row=1, column=2)

def camino(desde, hasta, vcamino):
    try:
        for v in g.listav:
            if desde == v.nombre:
                ld, lp = g.dijkstra(v)
        lc = []
        for i in range(len(g.listav)):
            if lp[i] != None:
                if hasta == g.listav[i].nombre:
                    lc.append(g.listav[i])
                    lc.append(lp[i])
                    lc = rec(lp[i], lc, lp)
       # lp[i].x, lp[i].y, g.listav[i].x, g.listav[i].y
        vcamino.destroy()
        mostrarcamino(list(reversed(lc)), li)
        hmc = Thread(target=mostrarcamino, args=(list(reversed(lc)), li))
        hmc.start()
        hm = Thread(target=movimiento, args=(list(reversed(lc)), bola))
        hm.start()
    except:
        messagebox.showerror("ERROR","Camino no encontrado")

def rec(vdestino, lc, lp):
    for i in range(len(g.listav)):
        if vdestino == g.listav[i]:
            if lp[i] != None:
                lc.append(lp[i])
                rec(lp[i], lc, lp)
    return lc

def mostrarcamino(lc, li):
    num = ancho / 2
    for aris in li:
        canvas3.delete(aris)
    del li[:]
    for i, j in zip(lc, lc[1:]):
        time.sleep(0.5)
        if i.x >= j.x and i.y > j.y:
            a = canvas3.create_line(i.x + num, i.y, j.x + ancho, j.y + num, width=3, fill="DarkGoldenrod1", arrow="last",
                                   smooth=True)
            li.append(a)
        if (i.x > j.x and i.y < j.y):
            a = canvas3.create_line(i.x + num, i.y + ancho, j.x + ancho, j.y + num, width=3, fill="DarkGoldenrod1",
                                   arrow="last", smooth=True)
            li.append(a)
        if (i.x <= j.x and i.y > j.y):
            a = canvas3.create_line(i.x + num, i.y, j.x, j.y + num, width=3, fill="DarkGoldenrod1", arrow="last",
                                   smooth=True)
            li.append(a)
        if (i.x < j.x and i.y < j.y):
            a = canvas3.create_line(i.x + num, i.y + ancho, j.x, j.y + num, width=3, fill="DarkGoldenrod1", arrow="last",
                                   smooth=True)
            li.append(a)

def movimiento(lc, bola):
    if(len(lc)!=0):
        num = ancho / 2
        canvas3.delete("obj")
        canvas3.create_image(lc[0].x + num, lc[0].y + num, image=bola, tag="obj")
        m = round((lc[1].y-lc[0].y)/(lc[1].x-lc[0].x),4)
        aumento = 2
        tiempo=0.05

        for i, j in zip(lc, lc[1:]):
            cords = canvas3.coords("obj")
            h1 = Thread(target=muestra, args=(cords[0],cords[1],lc))
            h1.start()
            time.sleep(tiempo)
            if i.x >= j.x and i.y > j.y:
                m = (j.y - i.y) / (j.x - i.x)
                for x in range(i.x, j.x, -aumento):
                    pos = canvas3.coords("obj")
                    if pos[0] > j.x+num:
                        canvas3.move("obj", -aumento, -aumento * m)
                        canvas3.update()
                        time.sleep(tiempo)
                    else:
                        break
            if i.x > j.x and i.y < j.y:
                m = (j.y - i.y) / (j.x - i.x)
                for x in range(i.x, j.x, -aumento):
                    pos = canvas3.coords("obj")
                    if pos[0] > j.x+num:
                        canvas3.move("obj", -aumento, -aumento * m)
                        canvas3.update()
                        time.sleep(tiempo)
                    else:
                        break
            if i.x <= j.x and i.y > j.y:
                m = (j.y - i.y) / (j.x - i.x)
                for x in range(i.x, j.x, aumento):
                    pos = canvas3.coords("obj")
                    if pos[0] < j.x+num:
                        canvas3.move("obj", aumento, aumento * m)
                        canvas3.update()
                        time.sleep(tiempo)
                    else:
                        break
            if i.x < j.x and i.y < j.y:
                m = (j.y - i.y) / (j.x - i.x)
                for x in range(i.x, j.x, aumento):
                    pos = canvas3.coords("obj")
                    if pos[0] < j.x+num:
                        canvas3.move("obj", aumento, aumento * m)
                        canvas3.update()
                        time.sleep(tiempo)
                    else:
                        break
    else:
        messagebox.showerror("ERROR","No se puede calcular la ruta")

def muestra(x,y,lc):
    for vert in g.listav:
        if x > vert.x-15 and x < vert.x+15+ancho and y > vert.y-15 and y < vert.y +15+ ancho:
            info = Toplevel()
            l1 = Label(info, text="Nombre:").grid(row=0, column=0)
            l2 = Label(info, text=vert.nombre).grid(row=0, column=1)
            
            time.sleep(5)
            info.destroy()
        if vert==lc[-2]:
            ultimo = Toplevel()
            l1 = Label(ultimo, text="Nombre:").grid(row=0, column=0)
            l2 = Label(ultimo, text=lc[-1].nombre).grid(row=0, column=1)
            
            time.sleep(5)
            ultimo.destroy()

# Ruta con distancia

def listaprev(previo, listap, listica):
    for i in range(len(g.listav)):
        if g.listav[i] == previo:
            if listap[i] != None:
                listica.append(listap[i])
                listaprev(listap[i], listap, listica)
    return listica


def cargarmapa():
    listaX=[188,419,361,260,311,408,227,546,116,249,588,341,197,554,97,515,430,467,577,324]
    listaY=[145,190,97,332,215,358,256,291,328,59,114,473,445,447,168,106,302,511,396,413]
    try:
        del g.listav[:]
        del g.listaA[:]
        file = askopenfile(title="Abrir mapa", filetypes=[("Archivo de texto", "*.txt")])
        ftemp = []
        for  t in file.readlines():
            ftemp.append(t)  
            
        NumeroVertice=int(len(ftemp))
        for n in range(0, NumeroVertice):
           # vtemp=vertice(str(n), -0.859*100, -0.963*10)
            vtemp=vertice(str(n), listaX[n], listaY[n])
            #vtemp=vertice(str(n), int(random.randint(220, 540)), int(random.randint(230, 570)))
            g.agregarVertice(vtemp)
            actualizar()
        cargarrelaciones(ftemp)
        file.close()
    except:
      messagebox.showerror("No se cargo el Grafo")

# usando matriz de adyacencia
def cargarrelaciones(ftemp):
    c=int(len(ftemp))
    matrizA = [[None]*c]*c
    
    for i in range(len(ftemp)):
        
        temp = ftemp[i].split(",")
       
        for j in range(len(ftemp)):
            #print("i:",i,"j:",j)""
            if int(temp[j])!=0:
              matrizA[i][j]=int(temp[j])
              relacion(str(i), str(j),int(temp[j]), Toplevel(Ventana))
            else: 
                matrizA[i][j]=int(temp[j])
  
          
            
def mostrarprofundidad():
    l = []
    l = g.profundidad(g.listav[0], l)
    for vert in l:
        print(vert.nombre)

def algoritmo1():
    global bandera 
    bandera=1
def algoritmo2():
    global bandera
    bandera=2
def algoritmo3():
    global bandera
    bandera=3
def algoritmo4():
    global bandera
    bandera=4 


def Ejecusion():
    try:
        if bandera==1:
            clickdijkstra()
        if bandera==2:
            clickcamino()
        if bandera==3:
            print
        if bandera==4:
            print
    except:
        messagebox.showerror("No ha")
                 
def Guaradar_PDF():
    try:
        ingreso = Toplevel()
        ingreso.title("Guardar PDF")
        tnombre = Label(ingreso, text="Ingrese nombre del Pdf:")
        tnombre.grid(row=0, column=0)
        nombrev = Entry(ingreso)
        nombrev.grid(row=0, column=1)
        agregar = Button(ingreso, text="Guardar",
                        command=lambda: PDF(nombrev.get(), ingreso))
        agregar.grid(row=3, columnspan=2)
    except:
      messagebox.showerror("No  se Guardo el PDF")

def PDF(nombre_pdf,ingreso):
    try:
        num = ancho / 2
        image2 = Image.new("RGB", (width, height), white)
        draw2 = ImageDraw.Draw(image2)   
    
        for i in range(len(g.listav)): 
            draw2.ellipse([g.listav[i].x-60, g.listav[i].y-60, g.listav[i].x-60 + ancho, g.listav[i].y-60 + ancho],  fill="#3498DB", outline ="green")  
        
        for i in range(len(g.listaA)):

            if g.listaA[i].x1 >= g.listaA[i].x2 and g.listaA[i].y1 > g.listaA[i].y2:
                draw2.line([g.listaA[i].x1-60 + num, g.listaA[i].y1-60, g.listaA[i].x2-60 + ancho, g.listaA[i].y2-60 + num],fill="#A3E4D7", width=3,  joint=None)
            
            if g.listaA[i].x1 > g.listaA[i].x2 and g.listaA[i].y1 < g.listaA[i].y2:
                draw2.line([g.listaA[i].x1-60 + num, g.listaA[i].y1-60 + ancho, g.listaA[i].x2-60 + ancho,g.listaA[i].y2-60 + num],fill="#A3E4D7", width=3, joint=None)
                
            if g.listaA[i].x1 <= g.listaA[i].x2 and g.listaA[i].y1 > g.listaA[i].y2:
                draw2.line([g.listaA[i].x1-60 + num, g.listaA[i].y1-60, g.listaA[i].x2-60, g.listaA[i].y2-60 + num],fill="#A3E4D7", width=3,
                                    joint="curve")
            
            if g.listaA[i].x1 < g.listaA[i].x2 and g.listaA[i].y1 < g.listaA[i].y2:
                draw2.line([g.listaA[i].x1-60 + num, g.listaA[i].y1-60 + ancho, g.listaA[i].x2-60, g.listaA[i].y2-60 + num],
                                fill="#A3E4D7",width=3, joint=None)
            
        for i in range(len(g.listaA)):

            if g.listaA[i].x1 >= g.listaA[i].x2 and g.listaA[i].y1 > g.listaA[i].y2:
                tx1 = ((g.listaA[i].x1-60 + num) + (g.listaA[i].x2-60 + ancho)) / 2
                ty1 = (g.listaA[i].y1-60 + (g.listaA[i].y2-60 - num)) / 2
                
                draw2.text([tx1, ty1+ num], text=str(g.listaA[i].distancia),fill=black )
            
            if g.listaA[i].x1 > g.listaA[i].x2 and g.listaA[i].y1 < g.listaA[i].y2:
                tx1 = ((g.listaA[i].x1-60 + num) + (g.listaA[i].x2-60 + ancho)) / 2
                ty1 = ((g.listaA[i].y1-60 - ancho) + (g.listaA[i].y2-60 + num)) / 2
                
                draw2.text([tx1, ty1 + ancho], text=str(g.listaA[i].distancia),fill=black)
                
                
            if g.listaA[i].x1 <= g.listaA[i].x2 and g.listaA[i].y1 > g.listaA[i].y2:
                tx1 = ((g.listaA[i].x1-60 + num) + g.listaA[i].x2-60) / 2
                ty1 = (g.listaA[i].y1-60 + (g.listaA[i].y2-60 - num)) / 2
                
                draw2.text([tx1, ty1 + num], text=str(g.listaA[i].distancia),fill=black )
            
            if g.listaA[i].x1 < g.listaA[i].x2 and g.listaA[i].y1 < g.listaA[i].y2:
                tx1 = (g.listaA[i].x1-60 + (num + g.listaA[i].x2-60)) / 2
                ty1 = ((g.listaA[i].y1-60 - ancho) + (g.listaA[i].y2-60 + num)) / 2
            
                draw2.text([tx1, ty1 + ancho], text=str(g.listaA[i].distancia),fill=black )
                
        for i in range(len(g.listav)):
            nombre = str(g.listav[i].nombre)
            if len(nombre) > 5:
                nombre = nombre[0:4] + ".."
            draw2.text([g.listav[i].x-60 + num, g.listav[i].y-60 + num], text=nombre, fill="#A93226" )
                 
        path = Path("C:\Grafos")
        path.mkdir(parents=True, exist_ok=True)
        messagebox.showinfo("Se guardo en la carpeta : Grafos en el disco")
        nombrePdf="C:\carpeta-graf\Grafo_"+str(nombre_pdf)+".pdf"
        c = canvas.Canvas(nombrePdf)
        ingreso.destroy()
        c.drawString(280, 800, "¡Grafo!")
        nommbreJPG=str(nombre_pdf)+ ".jpg"
        image2.save(nommbreJPG)       
        c.drawImage(nommbreJPG, 25, 480, 480, 270) # Dibujamos una imagen (IMAGEN, X,Y, WIDTH, HEIGH)
        c.save()
    except:
        messagebox.showinfo("No se Guardo el  pdf")  

def Guardar_EXCEL():
    lista=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    wb = openpyxl.Workbook()
    hoja = wb.active
    c=0    
    for i in range(len(g.listav)):
        cad=lista[0]+str(i+1)
        hoja[cad]=g.listav[i].nombre
        for j in range(len(g.listaA)):
            cadena=str(g.listaA[j].frm.nombre)            
            if g.listav[i].nombre==cadena:
                c=c+1
                cad=lista[c]+str(i+1)
                cadena2=str(g.listaA[j].to.nombre) +','+ str(g.listaA[j].distancia)
                hoja[cad]=cadena2
        c=0    
    file = asksaveasfile(mode="wb", title="Guardar Grafo en formato EXCEL", defaultextension=".xlsx",filetypes=[("Archivo de texto", "*.xlsx")])
    wb.save(file)   
        

def quit(self):
    self.root.destroy() 


def GuardarMatriz():
    try:
        global filename
        filename = "mp.txt"
        archivo = asksaveasfile(mode="w", title="Guardar mapa", defaultextension=".txt",filetypes=[("Archivo de texto", "*.txt")])
        for i in range(len(g.listav)):
            for j in range(len(g.listav)):
                archivo.writelines(str(int(matriz_Adyac[i][j])))
                archivo.writelines(", ")
            archivo.writelines("\n")
        archivo.close()      
    except:
        messagebox.showerror("No se guardo la Matriz")
        

def GuardarMatriz2():
    try:
        global filename
        filename = "mp.txt"
        archivo = asksaveasfile(mode="w", title="Guardar Matriz", defaultextension=".txt",
                                filetypes=[("Archivo de texto", "*.txt")])
        #archivo=open(fil, "w")
       
        for i in range(len(g.listav)):
            for j in range(len(g.listav)):
            
              archivo.write(matriz_Adyac[i][j])
            archivo.write("\n")
        archivo.close()
    except:
        messagebox.showerror("No se guardo la Matriz")


def Guaradar_JSON():
    ### Guardamos en formato JSON el grafo
    data = {}
    data['Grafo'] = []
    try:
        #data['Grafo'].append({"_id":1})
        for i in range(len(g.listav)):
            cadena='N_'
            cadena= cadena + str(g.listav[i].nombre)
            data['Grafo'].append({"identificacion":i+1,"etiqueta":cadena,'cordenadas:':{'x:':g.listav[i].x,'y:':g.listav[i].y} })
            data['Grafo'].append("vinculado a: ")
            for j in range(len(g.listaA)):
                if g.listaA[j].frm.nombre==g.listav[i].nombre:
                    data['Grafo'].append({  'Id. Nodo':g.listaA[j].to.nombre,'distancia':g.listaA[j].distancia})
        
        with open('Formato3.json', 'w') as file:
         json.dump(data, file, indent=4)
        
    except:
         messagebox.showerror("No se Gurado el Grafo")
        
   ###Guardamos en la base de datos el grafo
    try:  
         
      


         client = pymongo.MongoClient("mongodb://avalentierra:MHRurv73Alifer@cluster0-shard-00-00.rbl8j.mongodb.net:27017,cluster0-shard-00-01.rbl8j.mongodb.net:27017,cluster0-shard-00-02.rbl8j.mongodb.net:27017/Grafos?ssl=true&replicaSet=atlas-9cwijg-shard-0&authSource=admin&retryWrites=true&w=majority")
         db = client['Grafos']
         col=db['GRA']
         col.insert_one(data)
         messagebox.showinfo("!Se cargó exitosamente!")
    except:
       messagebox.showinfo("Error: Vaya a Ayuda")
   
def Guardar_Como_XML():
    datas = ET.Element('Grafo') 
    try: 
        for i in range(len(g.listav)):
            cadena='N_'
            cadena= cadena + str(g.listav[i].nombre)
            cadena1="[ identificacion : "+ str(i) + " etiqueta :" + str(cadena) + ' [cordenadas :' + str('x:'+str(g.listav[i].x)+ 'y:'+str(g.listav[i].y)+']')+']'
            ET.SubElement(datas,cadena1)
            ET.SubElement(datas, 'Vinculado a:')    
            for j in range(len(g.listaA)):         
                if g.listaA[j].frm.nombre==g.listav[i].nombre:
                    cadena1='(Id. Nodo :'+str(g.listaA[j].to.nombre)+', distancia :'+str(g.listaA[j].distancia )+')'
                    ET.SubElement(datas,cadena1)                    
        mydata = ET.tostring(datas)
        myfile = asksaveasfile(mode="w", title="Guardar Grafo en formato XML", defaultextension=".xml",
                                filetypes=[("Archivo de texto", "*.xml")])
       
        myfile.write(str(mydata)) 
    except: 
         messagebox.showerror("No se guardo el XML")       

def Guaradar_Como_JSON():
    ### Guardamos en formato JSON el grafo
    data = {}
    data = []
    try:
        for i in range(len(g.listav)):
            cadena='N_'
            cadena= cadena + str(g.listav[i].nombre)
            data.append({"identificacion":i+1,"etiqueta":cadena,'cordenadas:':{'x:':g.listav[i].x,'y:':g.listav[i].y} })
            data.append("vinculado a: ")
        
            for j in range(len(g.listaA)):
                if g.listaA[j].frm.nombre==g.listav[i].nombre:
                    data.append({  'Id. Nodo':g.listaA[j].to.nombre,'distancia':g.listaA[j].distancia})
        
        file = asksaveasfile(mode="w", title="Guardar Grafo en formato .JSON", defaultextension=".json",
                                filetypes=[("Archivo de texto", "*.json")])
        json.dump(data, file, indent=4)
    except:
         messagebox.showerror("No se guardo la informacion .JSON")


def buscar(a):
    
    for i in range(len(g.listav)):
        if a==g.listav[i].nombre:
            return i
    
def ventan_tabla():
    tabla = Tk()
    tabla.title("Matriz de Adyacencia")
    tabla.geometry("300x300")
    cantidad=len(g.listav)
    global matriz_Adyac
    matriz_Adyac = np.zeros((cantidad,cantidad))
    text_area = scrolledtext.ScrolledText(tabla, wrap = tk.WORD, width = 29, height = 12, font = ("Times New Roman",15))
    text_area.grid(row=0,column =1 )
   
    for i in range(len(g.listav)):
      
            for j in range(len(g.listaA)):
                
                if g.listav[i].nombre==g.listaA[j].frm.nombre:
                    frm=buscar(g.listaA[j].frm.nombre)
                    to=buscar(g.listaA[j].to.nombre)
                    matriz_Adyac[frm][to]=g.listaA[j].distancia
                    
    text_area.insert(END, matriz_Adyac)
    
    Butt = Button(tabla, text="Guardar Matriz",
                      command=lambda: GuardarMatriz())
    Butt.grid(row=1,column=1)
    
    
def ventan_grafica():
    tabla = Tk()
    tabla.title("Grafo")
    tabla.geometry("500x500")
    canvas_grafica = Canvas(tabla, width=400, height=400, bg="#B3B6B7")#taget
    canvas_grafica.pack(fill=BOTH, expand=YES)
    Butt = Button(tabla, text="Guardar Grafico",
                      command=lambda: GuardarImagen())
    Butt.pack()

    num = ancho / 2
    
    canvas_grafica.delete("all")
    for i in range(len(g.listav)):
        canvas_grafica.create_oval(g.listav[i].x-80, g.listav[i].y-80, g.listav[i].x-80 + ancho, g.listav[i].y-80 + ancho, fill="#3498DB", width=0)
        canvas_grafica.create_oval(g.listav[i].x+5-80, g.listav[i].y+5-80, g.listav[i].x-80 + ancho-5, g.listav[i].y-80 + ancho-5, fill="#3498DB", activefill="#E67E22", width=0)
        
    for i in range(len(g.listaA)):

        if g.listaA[i].x1 >= g.listaA[i].x2 and g.listaA[i].y1 > g.listaA[i].y2:
            canvas_grafica.create_line(g.listaA[i].x1-80 + num, g.listaA[i].y1-80, g.listaA[i].x2-80 + ancho, g.listaA[i].y2-80 + num,
                               width=3, fill="#A3E4D7", arrow="last", smooth=True)
           
        if g.listaA[i].x1 > g.listaA[i].x2 and g.listaA[i].y1 < g.listaA[i].y2:
            canvas_grafica.create_line(g.listaA[i].x1-80 + num, g.listaA[i].y1-80 + ancho, g.listaA[i].x2-80 + ancho,
                               g.listaA[i].y2-80 + num, width=3, fill="#A3E4D7", arrow="last", smooth=True)
            
        if g.listaA[i].x1 <= g.listaA[i].x2 and g.listaA[i].y1 > g.listaA[i].y2:
            canvas_grafica.create_line(g.listaA[i].x1-80 + num, g.listaA[i].y1-80, g.listaA[i].x2-80, g.listaA[i].y2-80 + num, width=3,
                               fill="#A3E4D7", joint=None)
           
        if g.listaA[i].x1 < g.listaA[i].x2 and g.listaA[i].y1 < g.listaA[i].y2:
            canvas_grafica.create_line(g.listaA[i].x1-80 + num, g.listaA[i].y1-80 + ancho, g.listaA[i].x2-80, g.listaA[i].y2-80 + num,
                               width=3, fill="#A3E4D7", arrow="last", smooth=True)
            

    for i in range(len(g.listaA)):

        if g.listaA[i].x1 >= g.listaA[i].x2 and g.listaA[i].y1 > g.listaA[i].y2:
            tx1 = ((g.listaA[i].x1-80 + num) + (g.listaA[i].x2-80 + ancho)) / 2
            ty1 = (g.listaA[i].y1-80 + (g.listaA[i].y2-80 - num)) / 2
            canvas_grafica.create_text([tx1, ty1 + num], text=str(g.listaA[i].distancia) )
            
            
            
        if g.listaA[i].x1 > g.listaA[i].x2 and g.listaA[i].y1 < g.listaA[i].y2:
            tx1 = ((g.listaA[i].x1-80 + num) + (g.listaA[i].x2-80 + ancho)) / 2
            ty1 = ((g.listaA[i].y1-80 - ancho) + (g.listaA[i].y2-80 + num)) / 2
            canvas_grafica.create_text(tx1, ty1 + ancho, text=str(g.listaA[i].distancia) )
            
           
        if g.listaA[i].x1 <= g.listaA[i].x2 and g.listaA[i].y1 > g.listaA[i].y2:
            tx1 = ((g.listaA[i].x1-80 + num) + g.listaA[i].x2-80) / 2
            ty1 = (g.listaA[i].y1-80 + (g.listaA[i].y2-80 - num)) / 2
            canvas_grafica.create_text(tx1, ty1 + num, text=str(g.listaA[i].distancia) )
            
            
            
        if g.listaA[i].x1 < g.listaA[i].x2 and g.listaA[i].y1 < g.listaA[i].y2:
            tx1 = (g.listaA[i].x1-80 + (num + g.listaA[i].x2-80)) / 2
            ty1 = ((g.listaA[i].y1-80 - ancho) + (g.listaA[i].y2-80 + num)) / 2
            canvas_grafica.create_text(tx1, ty1 + ancho, text=str(g.listaA[i].distancia) )
           

    for i in range(len(g.listav)):
        nombre = str(g.listav[i].nombre)
        if len(nombre) > 5:
            nombre = nombre[0:4] + ".."
        canvas_grafica.create_text(g.listav[i].x-80 + num, g.listav[i].y-80 + num, text=nombre, fill="#A93226", font="bold")
      


def GuardarImagen():
    num = ancho / 2
    fileI = asksaveasfile(mode="w", title="Guardar grafo como Imagen  .PNG", defaultextension=".jpg",
                                filetypes=[("Archivo de texto", "*.jpg")])
    filename2 = fileI
    global image1
    image1 = Image.new("RGB", (width, height), white)
   
    draw = ImageDraw.Draw(image1)   
   
         #os.startfile(filename2)
    
    for i in range(len(g.listav)):
        
        draw.ellipse([g.listav[i].x-60, g.listav[i].y-60, g.listav[i].x-60 + ancho, g.listav[i].y-60 + ancho],  fill="#3498DB", outline ="green")
        
       
    for i in range(len(g.listaA)):

        if g.listaA[i].x1 >= g.listaA[i].x2 and g.listaA[i].y1 > g.listaA[i].y2:
            
            draw.line([g.listaA[i].x1-60 + num, g.listaA[i].y1-60, g.listaA[i].x2-60 + ancho, g.listaA[i].y2-60 + num],
                              fill="#A3E4D7", width=3,  joint=None)
           
        if g.listaA[i].x1 > g.listaA[i].x2 and g.listaA[i].y1 < g.listaA[i].y2:
            
            draw.line([g.listaA[i].x1-60 + num, g.listaA[i].y1-60 + ancho, g.listaA[i].x2-60 + ancho,
                                g.listaA[i].y2-60 + num],fill="#A3E4D7", width=3, joint=None)
            
        if g.listaA[i].x1 <= g.listaA[i].x2 and g.listaA[i].y1 > g.listaA[i].y2:
            
            draw.line([g.listaA[i].x1-60 + num, g.listaA[i].y1-60, g.listaA[i].x2-60, g.listaA[i].y2-60 + num],fill="#A3E4D7", width=3,
                                joint="curve")
           
        if g.listaA[i].x1 < g.listaA[i].x2 and g.listaA[i].y1 < g.listaA[i].y2:
            
            draw.line([g.listaA[i].x1-60 + num, g.listaA[i].y1-60 + ancho, g.listaA[i].x2-60, g.listaA[i].y2-60 + num],
                               fill="#A3E4D7",width=3, joint=None)
           
    for i in range(len(g.listaA)):

        if g.listaA[i].x1 >= g.listaA[i].x2 and g.listaA[i].y1 > g.listaA[i].y2:
            tx1 = ((g.listaA[i].x1-60 + num) + (g.listaA[i].x2-60 + ancho)) / 2
            ty1 = (g.listaA[i].y1-60 + (g.listaA[i].y2-60 - num)) / 2
            
            draw.text([tx1, ty1 + num], text=str(g.listaA[i].distancia),fill=black )
           
        if g.listaA[i].x1 > g.listaA[i].x2 and g.listaA[i].y1 < g.listaA[i].y2:
            tx1 = ((g.listaA[i].x1-60 + num) + (g.listaA[i].x2-60 + ancho)) / 2
            ty1 = ((g.listaA[i].y1-60 - ancho) + (g.listaA[i].y2-60 + num)) / 2
            
            draw.text([tx1, ty1 + ancho], text=str(g.listaA[i].distancia),fill=black)
            
            
        if g.listaA[i].x1 <= g.listaA[i].x2 and g.listaA[i].y1 > g.listaA[i].y2:
            tx1 = ((g.listaA[i].x1-60 + num) + g.listaA[i].x2-60) / 2
            ty1 = (g.listaA[i].y1-60 + (g.listaA[i].y2-60 - num)) / 2
            
            draw.text([tx1, ty1 + num], text=str(g.listaA[i].distancia),fill=black )
           
        if g.listaA[i].x1 < g.listaA[i].x2 and g.listaA[i].y1 < g.listaA[i].y2:
            tx1 = (g.listaA[i].x1-60 + (num + g.listaA[i].x2-60)) / 2
            ty1 = ((g.listaA[i].y1-60 - ancho) + (g.listaA[i].y2-60 + num)) / 2
           
            draw.text([tx1, ty1 + ancho], text=str(g.listaA[i].distancia),fill=black )
            
    for i in range(len(g.listav)):
        nombre = str(g.listav[i].nombre)
        if len(nombre) > 5:
            nombre = nombre[0:4] + ".."
        draw.text([g.listav[i].x-60 + num, g.listav[i].y-60 + num], text=nombre, fill="#A93226" )
    image1.save(filename2)      
        
############## IMPORTAR INFORMACION

def cargarDocumento_Formato_JSON(data2):
    c=0
    for i in data2['grafico']:
        listaX=[188,419,361,260,311,408,227,546,116,249,588,341,197,554,97,515,430,467,577,324,145,190,97,332,215,358,256,291,328,59,114,473,445,447,168,106,302,511,396,413]
        listaY=[145,190,97,332,215,358,256,291,328,59,114,473,445,447,168,106,302,511,396,413,188,419,361,260,311,408,227,546,116,249,588,341,197,554,97,515,430,467,577,324]
        
        for j in i['datos']:
            id_Nodo_Origen=(j['id']) ### de esta forma acede al id del nodo
            control=0
            for h in g.listav:
             if  str(id_Nodo_Origen) == str(h.nombre): ##### Tal vez aqui haya un error
                control=1
            if control==0:
               
                
                vtemp=vertice(str(id_Nodo_Origen), int(listaX[c]), int(listaY[c]))
                c=c+1
                g.agregarVertice(vtemp)
                actualizar() 

           
    #### Nodos adyacentes
            keysLista=list(j['vinculado a']) 
            for k in keysLista:
                id_Nodo_Destino=k['nodeId']
                dist=k['distancia']
               
                control=0
                
                
                for p in g.listav:
                    if str(id_Nodo_Destino) == str(p.nombre):
                       control=1
                       for q in g.listav:
                           if str(id_Nodo_Origen)== str(q.nombre):
                 
                            atemp = arista(str(id_Nodo_Origen), str(id_Nodo_Destino), int(dist), int(p.x), int(p.y), int(q.x), int(q.y)) 
                            g.agregarArista(atemp)
                            actualizar()
                            break
                        
                    
                if control==0:
                    vtemp=vertice(str(id_Nodo_Destino), int(listaX[c]), int(listaY[c]))
                    c=c+1
                    g.agregarVertice(vtemp)
                    actualizar()
                    
                    for p in g.listav:
                        if str(id_Nodo_Destino)==str(p.nombre):
                            for q in g.listav:
                            
                                if str(id_Nodo_Origen)== str(q.nombre):   
                                    atemp = arista(str(id_Nodo_Origen), str(id_Nodo_Destino), int(dist), int(q.x),int(q.y),int(p.x),int(p.y))
                                    g.agregarArista(atemp)
                                    actualizar() 
                                    break
                                  
#IMPORTAR DE LA BASE DE DATOS
def Importar_Base():
   
    try:       
        client = pymongo.MongoClient("mongodb://avalentierra:MHRurv73Alifer@cluster0-shard-00-00.rbl8j.mongodb.net:27017,cluster0-shard-00-01.rbl8j.mongodb.net:27017,cluster0-shard-00-02.rbl8j.mongodb.net:27017/Grafos?ssl=true&replicaSet=atlas-9cwijg-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client['Grafos']
        col=db['GRA']
        for doc in col.find(): 
            cargarDocumento_Formato_JSON(doc)
        messagebox.showinfo("¡!Exit!¡")
    except:
        messagebox.showinfo("Error_Base_datos")

def Importar_Json():
   
    
    try:
        
        filename = askopenfile(title="Abrir JSON", filetypes=[("Formato Json", "*.json")])
        documento=json.load(filename)
        cargarDocumento_Formato_JSON(documento)
    except:
        messagebox.showinfo("Error_ .Json")

barra_menu=Menu(Ventana)
Ventana.config(menu= barra_menu)
    
#canvas3.bind("<Double-1>", dobleclick) 
    
Archivo=tk.Menu(barra_menu, tearoff=0)
Editar=tk.Menu(barra_menu, tearoff=0)
Analizar=tk.Menu(barra_menu, tearoff=0)
Herramienta=tk.Menu(barra_menu, tearoff=0)
Aplicacion=tk.Menu(barra_menu, tearoff=0)
Ventana=tk.Menu(barra_menu, tearoff=0)
Ayuda=tk.Menu(barra_menu, tearoff=0)

################################################################## SubMenu Archivo

##SubMenu Nuevo Grafo del SubMenu Archivo
sub_Nuevo_Grafo=tk.Menu(Archivo,tearoff=False)
sub_Nuevo_Grafo.add_command(label='Personalizado')
sub_Nuevo_Grafo.add_command(label='Aleatorio')
Archivo.add_cascade(label = 'Nuevo Grafo', menu=sub_Nuevo_Grafo)

Archivo.add_command(label='Abrir',command=cargarmapa)
Archivo.add_command(label='cerrar',command=quit)
Archivo.add_command(label='Guardar',command=Guaradar_JSON)

Sub_Guardar_datos=tk.Menu(Archivo, tearoff=False)
Sub_Guardar_datos.add_command(label='XML', command=Guardar_Como_XML)
Sub_Guardar_datos.add_command(label='JSON',command=Guaradar_Como_JSON)
Archivo.add_cascade(label='Guardar Como',menu=Sub_Guardar_datos)
#Archivo.add_command(label='Guardar Como',command=Guardar_Como_XML)

##subMenu exportar datos del subMenu Archivo
Sub_Exportar_datos=tk.Menu(Archivo, tearoff=False)
Sub_Exportar_datos.add_command(label='Excel',command=Guardar_EXCEL)
Sub_Exportar_datos.add_command(label='imagen', command=GuardarImagen)
Sub_Exportar_datos.add_command(label='PDF', command=Guaradar_PDF)
Archivo.add_cascade(label = 'Exportar Grafo', menu=Sub_Exportar_datos)


Sub_Importar_datos=tk.Menu(Archivo, tearoff=False)
Sub_Importar_datos.add_command(label='Desde la Base de datos',command=Importar_Base)
Sub_Importar_datos.add_command(label='Formato .JSON',command=Importar_Json)
Sub_Importar_datos.add_command(label='Formato .XML')
Archivo.add_cascade(label = 'Importar Grafo', menu=Sub_Importar_datos)

#Archivo.add_command(label='Importar datos',command=Importar_Base)

Archivo.add_command(label='inicio')
Archivo.add_command(label='Imprimir')


#####################################################  SubMenu Editar 

Editar.add_command(label='Deshacer')

## SubMenu Nodo del SubMenu Editar
Sub_Nodo=tk.Menu(Editar, tearoff=False)
Sub_Nodo.add_command(label='Agregar',command=dobleclick )
Sub_Nodo.add_command(label='Editar')
Sub_Nodo.add_command(label='Eliminar', command=clickeliminarv)
Editar.add_cascade(label = 'Nodo', menu=Sub_Nodo)

## SubMenu Archo del SubMenu Editar
Sub_Arco=tk.Menu(Editar, tearoff=False)
Sub_Arco.add_command(label='Agregar',command=clickrelacion)
Sub_Arco.add_command(label='Eliminar', command=clickeliminara)
Sub_Arco.add_command(label='Editar')
Editar.add_cascade(label = 'Arco', menu=Sub_Arco)



####################################################### SubMenu Algoritmos

## SubMenu Algoritmo del SubMenu Algoritmo
Sub_Algoritmo=tk.Menu(Analizar, tearoff=False)


disjtra_Todas_Rutas=tk.Menu(sub_Nuevo_Grafo, tearoff=False)
disjtra_Todas_Rutas.add_command(label='Todas las rutas mas cortas ', command=algoritmo1)
disjtra_Todas_Rutas.add_command(label='Mostrar Ruta', command=algoritmo2)
Sub_Algoritmo.add_cascade(label='Disjtra',menu=disjtra_Todas_Rutas)

Sub_Algoritmo.add_command(label='Floyd-Warshall')
Sub_Algoritmo.add_command(label=' Kruskal')
Sub_Algoritmo.add_command(label=' Prim')
Sub_Algoritmo.add_command(label=' otros sin considerar')

Analizar.add_cascade(label = 'Algoritmos', menu=Sub_Algoritmo)

######################################################## SubMenu Herramientas

Herramienta.add_command(label='Ejecusion',command=Ejecusion)

######################################################## SubMenu Aplicacion 
Aplicacion.add_command(label='Aplicacion 1')
Aplicacion.add_command(label='Aplicacion 2')
Aplicacion.add_command(label='Agregar las demas')


####################################################### SubMenu Vnetana
Ventana.add_command(label='Grafica',command=ventan_grafica)
Ventana.add_command(label='Tabla',command=ventan_tabla)

####################################################### SubMenu ventana
Ayuda.add_command(label='Ayuda')
Ayuda.add_command(label='Acerca de Grafos')


barra_menu.add_cascade(label='Archivo',menu=Archivo)
barra_menu.add_cascade(label='Editar',menu=Editar)
barra_menu.add_cascade(label='Analizar',menu=Analizar)
barra_menu.add_cascade(label='Herrameienta',menu=Herramienta)
barra_menu.add_cascade(label='Aplicacion',menu=Aplicacion)
barra_menu.add_cascade(label='Ventana',menu=Ventana)
barra_menu.add_cascade(label='Ayuda',menu=Ayuda)

def actualizar():
    num = ancho / 2

    canvas3.delete("all")
    for i in range(len(g.listav)):
        canvas3.create_oval(g.listav[i].x, g.listav[i].y, g.listav[i].x + ancho, g.listav[i].y + ancho, fill="#3498DB", width=0)
        canvas3.create_oval(g.listav[i].x+5, g.listav[i].y+5, g.listav[i].x + ancho-5, g.listav[i].y + ancho-5, fill="#3498DB", activefill="#E67E22", width=0)
            
    for i in range(len(g.listaA)):
        if g.listaA[i].x1 >= g.listaA[i].x2 and g.listaA[i].y1 > g.listaA[i].y2:
            canvas3.create_line(g.listaA[i].x1 + num, g.listaA[i].y1, g.listaA[i].x2 + ancho, g.listaA[i].y2 + num,
                            width=3, fill="#A3E4D7", arrow="last", smooth=True)
        
            
        if g.listaA[i].x1 > g.listaA[i].x2 and g.listaA[i].y1 < g.listaA[i].y2:
            canvas3.create_line(g.listaA[i].x1 + num, g.listaA[i].y1 + ancho, g.listaA[i].x2 + ancho,
                            g.listaA[i].y2 + num, width=3, fill="#A3E4D7", arrow="last", smooth=True)
        
        if g.listaA[i].x1 <= g.listaA[i].x2 and g.listaA[i].y1 > g.listaA[i].y2:
            canvas3.create_line(g.listaA[i].x1 + num, g.listaA[i].y1, g.listaA[i].x2, g.listaA[i].y2 + num, width=3,
                            fill="#A3E4D7", joint=None)
        
        if g.listaA[i].x1 < g.listaA[i].x2 and g.listaA[i].y1 < g.listaA[i].y2:
            canvas3.create_line(g.listaA[i].x1 + num, g.listaA[i].y1 + ancho, g.listaA[i].x2, g.listaA[i].y2 + num,
                            width=3, fill="#A3E4D7", arrow="last", smooth=True)
        

    for i in range(len(g.listaA)):

        if g.listaA[i].x1 >= g.listaA[i].x2 and g.listaA[i].y1 > g.listaA[i].y2:
            tx1 = ((g.listaA[i].x1 + num) + (g.listaA[i].x2 + ancho)) / 2
            ty1 = (g.listaA[i].y1 + (g.listaA[i].y2 - num)) / 2
            canvas3.create_text([tx1, ty1 + num], text=str(g.listaA[i].distancia) )
            
            
        if g.listaA[i].x1 > g.listaA[i].x2 and g.listaA[i].y1 < g.listaA[i].y2:
            tx1 = ((g.listaA[i].x1 + num) + (g.listaA[i].x2 + ancho)) / 2
            ty1 = ((g.listaA[i].y1 - ancho) + (g.listaA[i].y2 + num)) / 2
            canvas3.create_text(tx1, ty1 + ancho, text=str(g.listaA[i].distancia) )
                    
        if g.listaA[i].x1 <= g.listaA[i].x2 and g.listaA[i].y1 > g.listaA[i].y2:
            tx1 = ((g.listaA[i].x1 + num) + g.listaA[i].x2) / 2
            ty1 = (g.listaA[i].y1 + (g.listaA[i].y2 - num)) / 2
            canvas3.create_text(tx1, ty1 + num, text=str(g.listaA[i].distancia) )
                    
        if g.listaA[i].x1 < g.listaA[i].x2 and g.listaA[i].y1 < g.listaA[i].y2:
            tx1 = (g.listaA[i].x1 + (num + g.listaA[i].x2)) / 2
            ty1 = ((g.listaA[i].y1 - ancho) + (g.listaA[i].y2 + num)) / 2
            canvas3.create_text(tx1, ty1 + ancho, text=str(g.listaA[i].distancia) )          

    for i in range(len(g.listav)):
        nombre = str(g.listav[i].nombre)
        if len(nombre) > 5:
            nombre = nombre[0:4] + ".."
        canvas3.create_text(g.listav[i].x + num, g.listav[i].y + num, text=nombre, fill="#A93226", font="bold")
    
# Agregar vertice al mapa



Ventana.mainloop()
