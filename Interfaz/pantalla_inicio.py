#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from pantalla_administrador import Pantalla_administrador
from Tkinter import *

class Pantalla_de_inicio:

    def __init__(self):
        self.raiz = Toplevel()
        self.raiz.geometry('1169x563')
        self.raiz.title("Inicio")
        self.raiz.resizable(False, False) 
        self.imagen = PhotoImage(file="fondo.GIF")
        self.fondo = Label(self.raiz, image=self.imagen).place(x=0, y=0)
        self.ventana_principal()

    def ventana_principal(self):
        """ Muestra los botones de las distintas pestañas que tenemos,asi como el nombre de la ferreteria"""
        self.imagen_provedores = PhotoImage(file="Provedores.GIF")
        self.Boton_provedores = Button(self.raiz, image=self.imagen_provedores, width=131, height=19, cursor="hand2", border=0, command=lambda:instaciaciones())
        self.Boton_provedores.place(x=40, y=50)

        self.imagen_productos = PhotoImage(file="Productos.GIF")
        self.Boton_productos = Button(self.raiz, image=self.imagen_productos, width=119, height=19,cursor="hand2",border=0,  command=lambda:instaciaciones() )
        self.Boton_productos.place(x=45, y=150)

        self.imagen_inventario = PhotoImage(file="Inventario.GIF")
        self.Boton_inventario = Button(self.raiz, image=self.imagen_inventario, width=121, height=20,cursor="hand2",border=0,  command=lambda:instaciaciones() )
        self.Boton_inventario.place(x=55, y=250)

        self.imagen_ventas = PhotoImage(file="Ventas.GIF")
        self.Boton_ventas = Button(self.raiz, image=self.imagen_ventas, width=86, height=20,cursor="hand2",border=0,  command=lambda:instaciaciones() )
        self.Boton_ventas.place(x=60, y=345)

        self.imagen_admin = PhotoImage(file="Administrador.GIF")
        self.Boton_admin = Button(self.raiz, image=self.imagen_admin, width=169, height=26,cursor="hand2",border=0,  command=lambda:instaciaciones() )
        self.Boton_admin.place(x=33, y=443)
        self.raiz.mainloop()

    def instaciaciones(self):
            pass
            



