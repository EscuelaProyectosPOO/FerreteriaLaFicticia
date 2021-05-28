#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from Tkinter import *
#import tkMessageBox as mensajes
from funcionalidad.Manejar_archivos_administrador import Archivos_administrador
from funcionalidad.Evento_regresar import Cerrar_Ventanas
import ttk
from funcionalidad.Exepciones import *


class Administrador(Cerrar_Ventanas):
    def __init__(self, pantalla_principal):
        self.pantalla_Principal1 = pantalla_principal
        self.Raiz = Toplevel(self.pantalla_Principal1)
        self.Raiz.geometry('390x310')
        self.Raiz.title('Administrar usuarios')
        self.Raiz.resizable(0, 0)
        self.Raiz.iconbitmap('logo.ico')
        self.imagen = PhotoImage(file='fondo_admin.GIF')
        self.fondo = Label(self.Raiz, image=self.imagen)
        self.fondo.place(x=0, y=0)
        self.menu = Menu(self.Raiz)
        self.Raiz.config(menu=self.menu)
        self.Raiz.bind("<Destroy>", lambda event: self.volver_con_cerrado_ventana(event, self.pantalla_Principal1))

    def limpiar(self):
        self.NombreText.set('')
        self.contraText.set('')
        self.rangoText.set('')

    def registrar(self):
        band = True
        var = 0
        try:
            if self.NombreText.get() == '' or self.contraText.get() == '' or self.rangoText.get() == '':
                raise Vacio
        except Vacio as v:
            print Vacio, v
            band = False

        num = True
        try:
            var = int(self.rangoText.get())
        except ValueError:
            num = False

        try:
            if num == False and band == True:
                raise Numeros
            try:
                if var <= -1:
                    raise Negativos
            except Negativos as N:
                band = False
        except Numeros as n:
            print Numeros, n
            band = False

        if band == True:
            self.instancia_crear = Archivos_administrador()
            self.indicador = self.instancia_crear.Insertar(self.NombreText.get(), self.contraText.get(), self.rangoText.get())
            if (self.indicador):
                mensajes.showinfo('', 'Elemento registrado con éxito')
                self.limpiar()
            else:
                mensajes.showerror('', 'Este usuario ya existe')

    def eliminar(self):
        self.instancia_borrar = Archivos_administrador()
        self.indicador = self.instancia_borrar.Eliminar(self.NombreText.get())
        if (self.indicador):
            mensajes.showinfo('', 'Elemento eliminado exitosamente')
            self.limpiar()
        else:
            mensajes.showerror('ERROR', 'No se encontró este usuario')

    def editar(self):
        band = True
        var = 0
        try:
            if self.NombreText.get() == '' or self.contraText.get() == '' or self.rangoText.get() == '':
                raise Vacio
        except Vacio as v:
            print Vacio, v
            band = False

        num = True
        try:
            var = int(self.rangoText.get())
        except ValueError:
            num = False

        try:
            if num == False and band == True:
                raise Numeros
            try:
                if var <= -1:
                    raise Negativos
            except Negativos as N:
                band = False
        except Numeros as n:
            print Numeros, n
            band = False

        if band == True:
            self.instancia_editar = Archivos_administrador()
            self.indicador = self.instancia_editar.Modificar(self.NombreText.get(), self.contraText.get(),
                                                                self.rangoText.get())
            if (self.indicador):
                mensajes.showinfo('', 'Elemento modificado con éxito')
                self.limpiar()
            else:
                mensajes.showerror('ERROR', 'No se encuentra el usuario')

    def buscar(self):
        self.instancia_buscar = Archivos_administrador()
        self.linea_devuelta = self.instancia_buscar.Buscar(self.NombreText.get())
        try:
            self.NombreText.set(self.linea_devuelta[0])
            self.contraText.set(self.linea_devuelta[1])
            self.rangoText.set(self.linea_devuelta[2])
        except TypeError:
            print 'Elemento no encontrado'
            mensajes.showerror('ERROR', 'No se encuentra el usuario')

    def reporte(self):
        self.reporte_usuarios = Toplevel(self.Raiz)
        self.reporte_usuarios.title('Reporte de usuarios')
        self.reporte_usuarios.resizable(0, 0)
        self.reporte_usuarios.iconbitmap('logo.ico')
        self.tabla = ttk.Treeview(self.reporte_usuarios, show='headings',
                                  columns=("nombre", "rango"), height=12)
        self.tabla.grid(row=0, column=0)

        self.tabla.column("nombre", anchor="center")
        self.tabla.column("rango", anchor="center")

        self.tabla.heading("nombre", text='Nombre')
        self.tabla.heading("rango", text='Rango')

        self.barra = Scrollbar(self.reporte_usuarios, orient="vertical", command=self.tabla.yview())
        self.barra.grid(row=0, column=2, sticky="ns")
        self.tabla.config(yscrollcommand=self.barra.set)

        self.muestra_datos()

    def muestra_datos(self):
        self.llamada = Archivos_administrador()
        self.muestra = self.llamada.info()
        for i in self.muestra:
            self.linea = i.split("  ")
            self.tabla.insert("", END, text="", values=(self.linea[0], self.linea[2]))

    def ventana_principal(self):
        self.menu.add_command(label="Lista de usuarios", command=lambda:self.reporte())
        self.fodo_crear = PhotoImage(file='Boton_crear_usuario.gif')
        self.Bagregar = Button(self.Raiz, image=self.fodo_crear, command=lambda: self.registrar())
        self.Bagregar.place(x=140, y=205)
        self.Bagregar.config(bd=0)

        self.fodo_borrar = PhotoImage(file='Boton_borrar_usuario.gif')
        self.Bborrar = Button(self.Raiz, image=self.fodo_borrar, command=lambda: self.eliminar())
        self.Bborrar.place(x=140, y=245)
        self.Bborrar.config(bd=0)

        self.fodo_buscar = PhotoImage(file='fondo_buscar.gif')
        self.Bbuscar = Button(self.Raiz, image=self.fodo_buscar, command=lambda: self.buscar())
        self.Bbuscar.place(x=260, y=205)
        self.Bbuscar.config(bd=0)

        self.fodo_editar = PhotoImage(file='Boton_editar_usuario.gif')
        self.Beditar = Button(self.Raiz, image=self.fodo_editar, command=lambda: self.editar())
        self.Beditar.place(x=260, y=245)
        self.Beditar.config(bd=0)

        self.imagen_boton_regresar = PhotoImage(file="boton_regresar.GIF")
        self.Boton_regresar = Button(self.Raiz, image=self.imagen_boton_regresar, width=120, height=65,
                                        cursor="hand2", border=0,
                                        command=lambda: self.volver(self.Raiz, self.pantalla_Principal1))
        self.Boton_regresar.place(x=2, y=220)

        self.NombreText = StringVar()
        self.Nombre = Entry(self.Raiz, textvariable=self.NombreText, width=30)
        self.Nombre.place(x=170, y=35)

        self.contraText = StringVar()
        self.Contra = Entry(self.Raiz, textvariable=self.contraText, width=30)
        self.Contra.place(x=170, y=93)
        #self.Contra.config(show='*')

        self.rangoText = StringVar()
        self.Rango = Entry(self.Raiz, textvariable=self.rangoText, width=30)
        self.Rango.place(x=170, y=150)

        self.pantalla_Principal1.withdraw()

    def volver(self, nombre_ventana_actual, nombre_ventana_anterior):
        nombre_ventana_anterior.deiconify()
        nombre_ventana_actual.destroy()