#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox as mensajes
from funcionalidad.Manejar_archivos_proveedores import Archivos_proveedores
from funcionalidad.Evento_regresar import Cerrar_Ventanas

class Proveedores(Cerrar_Ventanas):
    def __init__(self, pantalla_principal):
        self.pantalla_principal1 = pantalla_principal
        self.Raiz = Toplevel(self.pantalla_principal1)
        self.Raiz.geometry('390x310')
        self.Raiz.title('Proveedores')
        self.Raiz.resizable(0, 0)
        self.imagen = PhotoImage(file='fondo_proveeores.gif')
        self.fondo = Label(self.Raiz, image=self.imagen)
        self.fondo.place(x=0, y=0)
        self.Raiz.bind("<Destroy>", lambda event: self.volver_con_cerrado_ventana(event, self.pantalla_principal1))


    def limpiar(self):
        self.NombreText.set('')
        self.direcText.set('')
        self.precioText.set('')
        self.productoText.set('')

    def registrar(self):
        self.instancia_crear = Archivos_proveedores()
        self.indicador = self.instancia_crear.Insertar(self.NombreText.get(), self.direcText.get(), self.productoText.get(), self.precioText.get())
        if (self.indicador):
            mensajes.showinfo('', 'Elemento registrado con éxito')
        else:
            mensajes.showerror('ERROR', 'No se puede registrar el proveedor')
        self.limpiar()

    def eliminar(self):
        self.instancia_borrar = Archivos_proveedores()
        self.indicador = self.instancia_borrar.Eliminar(self.NombreText.get())
        if (self.indicador):
            mensajes.showinfo('', 'Elemento eliminado exitosamente')
        else:
            mensajes.showerror('ERROR', 'No se encontró este proveedor')
        self.limpiar()

    def editar(self):
        self.instancia_editar = Archivos_proveedores()
        self.indicador = self.instancia_editar.Modificar(self.NombreText.get(), self.direcText.get(), self.productoText.get(), self.precioText.get())
        if (self.indicador):
            mensajes.showinfo('', 'Elemento modificado con éxito')
        else:
            mensajes.showerror('ERROR', 'No se encuentra el proveedor')
        self.limpiar()

    def ventana_principal(self):
        self.fondo_crear = PhotoImage(file='Boton_crear_usuario.gif')
        self.Bagregar = Button(self.Raiz, image=self.fondo_crear, command=lambda: self.registrar())
        self.Bagregar.place(x=20, y=240)
        self.Bagregar.config(bd=0)

        self.fondo_borrar = PhotoImage(file='Boton_borrar_usuario.gif')
        self.Bborrar = Button(self.Raiz, image=self.fondo_borrar, command=lambda: self.eliminar())
        self.Bborrar.place(x=140, y=240)
        self.Bborrar.config(bd=0)

        self.fondo_borrar = PhotoImage(file='Boton_borrar_usuario.gif')
        self.Bborrar = Button(self.Raiz, image=self.fondo_borrar, command=lambda: self.eliminar())
        self.Bborrar.place(x=140, y=240)
        self.Bborrar.config(bd=0)

        self.fondo_editar = PhotoImage(file='Boton_editar_usuario.gif')
        self.Beditar = Button(self.Raiz, image=self.fondo_editar, cursor="hand2", command=lambda: self.editar())
        self.Beditar.place(x=260, y=240)
        self.Beditar.config(bd=0)

        self.imagen_boton_regresar = PhotoImage(file="boton_regresar.GIF")
        self.Boton_regresar = Button(self.Raiz, image=self.imagen_boton_regresar, width=120, height=65,
                                        cursor="hand2", border=0,
                                        command=lambda: self.volver(self.Raiz, self.pantalla_principal1))
        self.Boton_regresar.place(x=2, y=340)

        self.NombreText = StringVar()
        self.Nombre = Entry(self.Raiz, textvariable=self.NombreText, width=30)
        self.Nombre.place(x=170, y=25)

        self.direcText = StringVar()
        self.Direccion = Entry(self.Raiz, textvariable=self.direcText, width=30)
        self.Direccion.place(x=170, y=70)

        self.productoText = StringVar()
        self.Producto = Entry(self.Raiz, textvariable=self.productoText, width=30)
        self.Producto.place(x=170, y=120)

        self.precioText = StringVar()
        self.Precio = Entry(self.Raiz, textvariable=self.precioText, width=30)
        self.Precio.place(x=170, y=170)

        self.pantalla_principal1.withdraw()

    def volver(self, nombre_ventana_actual, nombre_ventana_anterior):
        nombre_ventana_anterior.deiconify()
        nombre_ventana_actual.destroy()

