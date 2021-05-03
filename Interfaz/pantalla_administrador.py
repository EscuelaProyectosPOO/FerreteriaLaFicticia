#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkMessageBox as mensajes
from funcionalidad.Manejar_archivos_administrador import Archivos_administrador
from funcionalidad.Evento_regresar import Cerrar_Ventanas



class Administrador(Cerrar_Ventanas):
    def __init__(self, Pantalla_principal):
        self.pantalla_principal1 = Pantalla_principal
        self.Raiz = Toplevel(self.pantalla_principal1)
        self.Raiz.geometry('390x280')
        self.Raiz.title('Administrar usuarios')
        self.Raiz.resizable(0, 0)
        self.imagen = PhotoImage(file='fondo_admin.GIF')
        self.fondo = Label(self.Raiz, image=self.imagen)
        self.fondo.place(x=0, y=0)
        self.Raiz.bind("<Destroy>", lambda event: self.volver_con_cerrado_ventana(event, self.pantalla_principal1))

    def registrar(self):
        print self.NombreText.get(), '\n', self.contraText.get(), '\n', self.rangoText.get()
        self.instancia_crear = Archivos_administrador()
        self.indicador = self.instancia_crear.nuevo_usuario(self.NombreText.get(), self.contraText.get(), self.rangoText.get())
        if (self.indicador):
            mensajes.showinfo('', 'Elemento registrado con éxito')
        else:
            mensajes.showerror('ERROR', 'No se puede registrar el usuario')

    def eliminar(self):
        print self.NombreText.get()
        self.instancia_borrar = Archivos_administrador()
        self.indicador = self.instancia_borrar.eliminar_usuario(self.NombreText.get())
        if (self.indicador):
            mensajes.showinfo('', 'Elemento eliminado exitosamente')
        else:
            mensajes.showerror('ERROR', 'No se encontró este usuario')

    def editar(self):
        print self.NombreText.get(), '\n', self.contraText.get(), '\n', self.rangoText.get()
        self.instancia_editar = Archivos_administrador()
        self.indicador = self.instancia_editar.editar_usuario(self.NombreText.get(), self.contraText.get(),
                                                            self.rangoText.get())
        if (self.indicador):
            mensajes.showinfo('', 'Elemento modificado con éxito')
        else:
            mensajes.showerror('ERROR', 'No se encuentra el usuario')

    def ventana_principal(self):
        self.fodo_crear = PhotoImage(file='Boton_crear_usuario.gif')
        self.Bagregar = Button(self.Raiz, image=self.fodo_crear, command=lambda: self.registrar())
        self.Bagregar.place(x=20, y=205)
        self.Bagregar.config(bd=0)

        self.fodo_borrar = PhotoImage(file='Boton_borrar_usuario.gif')
        self.Bborrar = Button(self.Raiz, image=self.fodo_borrar, command=lambda: self.eliminar())
        self.Bborrar.place(x=140, y=205)
        self.Bborrar.config(bd=0)

        self.fodo_editar = PhotoImage(file='Boton_editar_usuario.gif')
        self.Beditar = Button(self.Raiz, image=self.fodo_editar, command=lambda: self.editar())
        self.Beditar.place(x=260, y=205)
        self.Beditar.config(bd=0)

        self.imagen_boton_regresar = PhotoImage(file="boton_regresar.GIF")
        self.Boton_regresar = Button(self.raiz, image=self.imagen_boton_regresar, width=120, height=65,
                                        cursor="hand2", border=0,
                                        command=lambda: self.volver(self.raiz, self.pantalla_principal1))
        self.Boton_regresar.place(x=2, y=340)

        self.NombreText = StringVar()
        self.Nombre = Entry(self.Raiz, textvariable=self.NombreText, width=30)
        self.Nombre.place(x=170, y=35)

        self.contraText = StringVar()
        self.Contra = Entry(self.Raiz, textvariable=self.contraText, width=30)
        self.Contra.place(x=170, y=93)
        self.Contra.config(show='*')

        self.rangoText = StringVar()
        self.Rango = Entry(self.Raiz, textvariable=self.rangoText, width=30)
        self.Rango.place(x=170, y=150)

        self.pantalla_principal1.withdraw()

    def volver(self, nombre_ventana_actual, nombre_ventana_anterior):
        nombre_ventana_anterior.deiconify()
        nombre_ventana_actual.destroy()

