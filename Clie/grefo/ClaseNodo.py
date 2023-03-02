import sys
from tkinter import *
import heapq
from grefo.Clases import *
from tkinter import messagebox
global ancho
ancho=40
g=grafo()
def actualizar(canvas3):
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

#canvas3.bind("<Double-1>", dobleclick) 
