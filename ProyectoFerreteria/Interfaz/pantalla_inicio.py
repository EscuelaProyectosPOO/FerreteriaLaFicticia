#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        Imagen_provedores = Image.open(file="Ventas.GIF")
        Boton_provedores = Button(self.raiz, image=Imagen_provedores, width=20)
        Boton_provedores.place(x=20, y=35)

        Boton_productos = Button(self.raiz, text="Productos", width=20, height=1, relief="ridge", borderwidth=5, bg="black", fg="white", font="Arial" )
        Boton_productos.place(x=20, y=135)

        Boton_inventario = Button(self.raiz, text="Inventario", width=20, height=1, relief="ridge", borderwidth=5, bg="black", fg="white", font="Arial")
        Boton_inventario.place(x=20, y=235)

        Boton_ventas = Button(self.raiz, text="Ventas", width=20, height=1, relief="ridge", borderwidth=5, bg="black", fg="white", font="Arial" )
        Boton_ventas.place(x=20, y=335)

        Boton_admin = Button(self.raiz, text="Administrador", width=20, height=1, relief="ridge", borderwidth=5, bg="black", fg="white", font="Arial" )
        Boton_admin.place(x=20, y=435)
        

       


uno = Pantalla_de_inicio()


