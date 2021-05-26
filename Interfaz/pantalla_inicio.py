#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from pantalla_administrador import Pantalla_administrador
from pantalla_inventario import Inventario
from pantalla_productos import Productos
from pantalla_administrador import  Administrador
from pantalla_proveedores import Proveedores
from pantalla_ventas import Ventas
from login import Usuarios
from Tkinter import *

class Pantalla_de_inicio:

    def __init__(self):
        self.raiz_pantalle_inicio = Tk()
        self.raiz_pantalle_inicio.geometry('1212x581')
        self.raiz_pantalle_inicio.title("Inicio")
        self.raiz_pantalle_inicio.resizable(False, False) 
        self.imagen = PhotoImage(file="fondo.GIF")
        self.fondo = Label(self.raiz_pantalle_inicio, image=self.imagen).place(x=0, y=0, relwidth=1, relheight=1)
        self.es_usuario_admin = False
        self.usuarios = Usuarios(self.raiz_pantalle_inicio)
        self.ventana_principal()

    def ventana_principal(self):
        """ Muestra los botones de las distintas pestañas que tenemos,asi como el nombre de la ferreteria"""
        self.es_usuario_admin=(self.usuarios.ventana_principal())
        #print self.es_usuario_admin
        self.imagen_proveedores = PhotoImage(file="Proveedores.GIF")
        self.Boton_proveedores = Button(self.raiz_pantalle_inicio, image=self.imagen_proveedores, width=234, height=91, cursor="hand2", border=0, command=lambda:self.proveedores_llamada())
        self.Boton_proveedores.place(x=2, y=50)

        self.imagen_productos = PhotoImage(file="Productos.GIF")
        self.Boton_productos = Button(self.raiz_pantalle_inicio, image=self.imagen_productos, width=228, height=87,cursor="hand2",border=0,  command=lambda:self.productos_llamada())
        self.Boton_productos.place(x=2, y=150)

        self.imagen_inventario = PhotoImage(file="Inventario.GIF")
        self.Boton_inventario = Button(self.raiz_pantalle_inicio, image=self.imagen_inventario, width=230, height=82,cursor="hand2",border=0,  command=lambda:self.inventario_llamada())
        self.Boton_inventario.place(x=2, y=250)

        self.imagen_ventas = PhotoImage(file="Ventas.GIF")
        self.Boton_ventas = Button(self.raiz_pantalle_inicio, image=self.imagen_ventas, width=233, height=80,cursor="hand2",border=0,  command=lambda:self.ventas_llamada() )
        self.Boton_ventas.place(x=2, y=350)

        self.imagen_admin = PhotoImage(file="Administrador.GIF")    
        self.Boton_admin = Button(self.raiz_pantalle_inicio, image=self.imagen_admin, width=235, height=85,cursor="hand2",border=0,  command=lambda:self.administrador_llamada() )
        self.Boton_admin.place(x=2, y=450)

        
        self.raiz_pantalle_inicio.mainloop()

    def inventario_llamada(self):
        self.inventario_objeto = Inventario(self.raiz_pantalle_inicio)
        self.inventario_objeto.ventana_principal()

    def productos_llamada(self):
        self.productos_objeto = Productos(self.raiz_pantalle_inicio)
        self.productos_objeto.ventana_principal()

    def proveedores_llamada(self):
        self.proveedores_objeto = Proveedores(self.raiz_pantalle_inicio)
        self.proveedores_objeto.ventana_principal()
        
    def ventas_llamada(self):
        self.ventas_objeto = Ventas(self.raiz_pantalle_inicio)
        self.ventas_objeto.ventana_principal()

    def administrador_llamada(self):
        self.administrador_llamada_objeto =  Administrador(self.raiz_pantalle_inicio)
        self.administrador_llamada_objeto.ventana_principal()



uno = Pantalla_de_inicio()




