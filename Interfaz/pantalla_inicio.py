#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from pantalla_administrador import Pantalla_administrador
from Tkinter import *

class Pantalla_de_inicio:

    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry('1212x581')
        self.raiz.title("Inicio")
        self.raiz.resizable(False, False) 
        self.imagen = PhotoImage(file="fondo.GIF")
        self.fondo = Label(self.raiz, image=self.imagen).place(x=-1, y=0)
        self.ventana_principal()

    def ventana_principal(self):
        """ Muestra los botones de las distintas pestañas que tenemos,asi como el nombre de la ferreteria"""
        self.imagen_proveedores = PhotoImage(file="Proveedores.GIF")
        self.Boton_proveedores = Button(self.raiz, image=self.imagen_proveedores, width=234, height=91, cursor="hand2", border=0, command=lambda:instaciaciones())
        self.Boton_proveedores.place(x=0, y=50)

        self.imagen_productos = PhotoImage(file="Productos.GIF")
        self.Boton_productos = Button(self.raiz, image=self.imagen_productos, width=228, height=87,cursor="hand2",border=0,  command=lambda:instaciaciones() )
        self.Boton_productos.place(x=0, y=150)

        self.imagen_inventario = PhotoImage(file="Inventario.GIF")
        self.Boton_inventario = Button(self.raiz, image=self.imagen_inventario, width=230, height=82,cursor="hand2",border=0,  command=lambda:instaciaciones() )
        self.Boton_inventario.place(x=0, y=250)

        self.imagen_ventas = PhotoImage(file="Ventas.GIF")
        self.Boton_ventas = Button(self.raiz, image=self.imagen_ventas, width=233, height=80,cursor="hand2",border=0,  command=lambda:instaciaciones() )
        self.Boton_ventas.place(x=0, y=350)

        self.imagen_admin = PhotoImage(file="Administrador.GIF")
        self.Boton_admin = Button(self.raiz, image=self.imagen_admin, width=235, height=85,cursor="hand2",border=0,  command=lambda:instaciaciones() )
        self.Boton_admin.place(x=0, y=450)

        
        self.raiz.mainloop()

    def instaciaciones(self):
            pass




