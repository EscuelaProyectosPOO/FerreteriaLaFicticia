#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pantalla_administrador import Pantalla_administrador

from Tkinter import *

class Pantalla_de_inicio:

    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry('1169x563')
        self.raiz.title("Inicio")
        self.raiz.resizable(False, False)
        self.imagen = PhotoImage(file="fondo.GIF")
        self.fondo = Label(self.raiz, image=self.imagen).place(x=0, y=0)
        #self.frame = Frame(self.raiz)
       # self.frame.pack(fill="both", expand=1)
        self.ventana_principal()
        self.raiz.mainloop()

    def ventana_principal(self):
        """ Muestra los botones de las distintas pestañas que tenemos,asi como el nombre de la ferreteria"""
        #imagen_provedores = PhotoImage(file="fondo.GIF").subsample(2,2)
        Boton_provedores = Button(self.raiz, bg="#FFFF00", text="Provedor",font="Arial", cursor="hand2", border=0 , width=20, command=lambda:instaciaciones())
        Boton_provedores.place(x=20, y=35)

        Boton_productos = Button(self.raiz, bg="#FFFF00", text="Productos",font="Arial", cursor="hand2", border=0 , width=20,  command=lambda:instaciaciones() )
        Boton_productos.place(x=20, y=135)

        Boton_inventario = Button(self.raiz, bg="#FFFF00", text="Inventario",font="Arial", cursor="hand2", border=0 , width=20,  command=lambda:instaciaciones())
        Boton_inventario.place(x=20, y=235)

        Boton_ventas = Button(self.raiz, bg="#FFFF00", text="Ventas",font="Arial", cursor="hand2", border=0 , width=20, command=lambda:instaciaciones() )
        Boton_ventas.place(x=20, y=335)

        Boton_admin = Button(self.raiz, bg="#FFFF00", text="Administrador",font="Arial", cursor="hand2", border=0 , width=20, command=lambda:instaciaciones())
        Boton_admin.place(x=20, y=435)

        def instaciaciones():
            uno = Pantalla_administrador()
        

       


uno = Pantalla_de_inicio()


