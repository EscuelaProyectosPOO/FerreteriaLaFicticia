#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pantalla_inventario import Inventario
from pantalla_productos import Productos
from pantalla_administrador import  Administrador
from pantalla_proveedores import Proveedores
from pantalla_ventas import Ventas
from Abrir_corte_caja import Abrir_corte
from funcionalidad.Evento_regresar import Cerrar_Ventanas
from Tkinter import *
import os

class Pantalla_de_inicio(Cerrar_Ventanas):

    def __init__(self, pantalla_principal, rango):
        self.pantalla_principal1 = pantalla_principal
        self.es_usuario_admin = rango
        self.raiz_pantalle_inicio = Toplevel(self.pantalla_principal1)
        self.raiz_pantalle_inicio.geometry('1212x600')
        self.raiz_pantalle_inicio.title("Inicio")
        self.raiz_pantalle_inicio.resizable(False, False)
        self.raiz_pantalle_inicio.iconbitmap('imagenes/logo.ico')
        self.imagen = PhotoImage(file="imagenes/fondo.GIF")
        self.fondo = Label(self.raiz_pantalle_inicio, image=self.imagen).place(x=0, y=0, relwidth=1, relheight=1)
        self.Barra_menu_principal = Menu(self.raiz_pantalle_inicio)
        self.raiz_pantalle_inicio.config(menu=self.Barra_menu_principal)
        self.raiz_pantalle_inicio.bind("<Destroy>", lambda event: self.volver_con_cerrado_ventana(event, self.pantalla_principal1))
        self.pantalla_principal1.withdraw()
        self.ventana_principal()
        

    def ventana_principal(self):
        """ Muestra los botones de las distintas pestañas que tenemos,asi como el nombre de la ferreteria"""
        self.Barra_menu_principal.add_command(label="Manual de usuario", command=lambda:self.abrir_manual_de_usuario())

        self.imagen_proveedores = PhotoImage(file="imagenes/Proveedores.GIF")
        self.Boton_proveedores = Button(self.raiz_pantalle_inicio, image=self.imagen_proveedores, width=234, height=91, cursor="hand2", border=0, command=lambda:self.proveedores_llamada())
        self.Boton_proveedores.place(x=2, y=50)

        self.imagen_productos = PhotoImage(file="imagenes/Productos.GIF")
        self.Boton_productos = Button(self.raiz_pantalle_inicio, image=self.imagen_productos, width=228, height=87,cursor="hand2",border=0,  command=lambda:self.productos_llamada())
        self.Boton_productos.place(x=2, y=150)

        self.imagen_inventario = PhotoImage(file="imagenes/Inventario.GIF")
        self.Boton_inventario = Button(self.raiz_pantalle_inicio, image=self.imagen_inventario, width=230, height=82,cursor="hand2",border=0,  command=lambda:self.inventario_llamada())
        self.Boton_inventario.place(x=2, y=250)

        self.imagen_ventas = PhotoImage(file="imagenes/Ventas.GIF")
        self.Boton_ventas = Button(self.raiz_pantalle_inicio, image=self.imagen_ventas, width=233, height=80,cursor="hand2",border=0,  command=lambda:self.ventas_llamada() )
        self.Boton_ventas.place(x=2, y=350)

        self.colocar_boton_administrador()

        

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
        """"Muestra la ventana con el mismo nombre"""
        self.administrador_llamada_objeto =  Administrador(self.raiz_pantalle_inicio)
        self.administrador_llamada_objeto.ventana_principal()

    def corte_de_caja_llamada(self):
        self.corte_llamada_objeto = Abrir_corte(self.raiz_pantalle_inicio)
        self.corte_llamada_objeto.ventana_principal()

    def abrir_manual_de_usuario(self):
        """Muestra el manual de usuario en el navegador"""
        self.direccion_manual = os.getcwd()  + "/Manual_de_usuario.pdf"
        os.system(self.direccion_manual)

    def colocar_boton_administrador(self):
        self.imagen_corte_caja = PhotoImage(file="imagenes/corte_de_caja.GIF")
        self.Boton_corte_caja = Button(self.raiz_pantalle_inicio, image=self.imagen_corte_caja, width=223, height=75,cursor="hand2",border=0,  command=lambda:self.corte_de_caja_llamada() )

        if(self.es_usuario_admin == True):
            self.imagen_admin = PhotoImage(file="imagenes/Administrador.GIF")
            self.Boton_admin = Button(self.raiz_pantalle_inicio, image=self.imagen_admin, width=235, height=85,cursor="hand2",border=0,  command=lambda:self.administrador_llamada() )
            self.Boton_admin.place(x=0, y=400)

            self.Boton_corte_caja.place(x=0, y=500)
            self.Boton_proveedores.place(x=0, y=0)
            self.Boton_productos.place(x=0, y=100)
            self.Boton_inventario.place(x=0, y=200)
            self.Boton_ventas.place(x=0, y=300)
        else:
            self.Boton_corte_caja.place(x=2, y=445)


    def volver(self, nombre_ventana_actual, nombre_ventana_anterior):
        nombre_ventana_anterior.deiconify()
        nombre_ventana_actual.destroy()








