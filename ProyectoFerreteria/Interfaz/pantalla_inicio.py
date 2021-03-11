#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

class Pantalla_de_inicio:

    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry('1000x700')
        self.raiz.config(bg="#3C5CE4")
        self.raiz.title("Inicio")
        self.frame = Frame(self.raiz)
        self.frame.pack()
        self.ventana_principal()
        self.raiz.mainloop()

    def ventana_principal(self):
        Boton_provedores = Button(self.frame, text="Provedores", width="50", bg="black", fg="white" )
        Boton_provedores.grid(row=2, column=0)

        Boton_productos = Button(self.frame, text="Productos", width="50", bg="black", fg="white" )
        Boton_productos.grid(row=3, column=0)

        Boton_inventario = Button(self.frame, text="Inventario", width="50", bg="black", fg="white" )
        Boton_inventario.grid(row=4, column=0)

        Boton_ventas = Button(self.frame, text="Ventas", width="50", bg="black", fg="white" )
        Boton_ventas.grid(row=5, column=0)

        Boton_admin = Button(self.frame, text="Administrador", width="50", bg="black", fg="white" )
        Boton_admin.grid(row=6, column=0)


uno = Pantalla_de_inicio()


