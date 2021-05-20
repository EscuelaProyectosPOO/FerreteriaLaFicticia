#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from Tkinter import *
import ttk
#import tkMessageBox as mensajes
from funcionalidad.Exepciones import *
from funcionalidad.Manejar_archivos_proveedores import Archivos_proveedores
from funcionalidad.Evento_regresar import Cerrar_Ventanas

class Proveedores(Cerrar_Ventanas):
    def __init__(self, pantalla_principal):
        self.pantalla_principal1 = pantalla_principal
        self.Raiz = Toplevel(self.pantalla_principal1)
        self.Raiz.geometry('390x335')
        self.Raiz.title('Proveedores')
        self.Raiz.resizable(0, 0)
        self.imagen = PhotoImage(file='fondo_proveeores.gif')
        self.fondo = Label(self.Raiz, image=self.imagen)
        self.fondo.place(x=0, y=0)
        self.menu = Menu(self.Raiz)
        self.Raiz.config(menu=self.menu)
        self.Raiz.bind("<Destroy>", lambda event: self.volver_con_cerrado_ventana(event, self.pantalla_principal1))


    def limpiar(self):
        self.NombreText.set('')
        self.direcText.set('')
        self.precioText.set('')
        self.productoText.set('')

    def buscar(self):
        print self.NombreText.get(), '\n', self.direcText.get(), '\n', self.productoText.get()
        self.instancia_buscar = Archivos_proveedores()
        self.linea_devuelta = self.instancia_buscar.Buscar(self.NombreText.get())
        print self.linea_devuelta
        if self.linea_devuelta == 0:
            mensajes.showerror('ERROR', 'Elemento no encontrado')
        else:
            self.NombreText.set(self.linea_devuelta[0])
            self.direcText.set(self.linea_devuelta[1])
            self.productoText.set(self.linea_devuelta[2])
            self.precioText.set(self.linea_devuelta[3])

    def registrar(self):
        band = True
        try:
            if self.NombreText.get() == '' or self.direcText.get() == '' or self.precioText.get() == '' or self.productoText.get() == '':
                raise Vacio
        except Vacio as v:
            print Vacio, v
            band = False

        num = True
        try:
            var = int(self.precioText.get())
        except:
            num= False

        try:
            if num == False:
                raise Numeros
        except Numeros as n:
            print Numeros, n
            band = False

        if band == True:
            self.instancia_insertar = Archivos_proveedores()
            self.indicador = self.instancia_insertar.Insertar(self.NombreText.get(), self.direcText.get(), self.productoText.get(), self.precioText.get())
            if (self.indicador):
                mensajes.showinfo('', 'Registro exitoso')
                self.limpiar()
            else:
                mensajes.showerror('Error', 'Ya existe un proveedor con este nombre')

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

    def reporte(self):
        self.reporte_proveeores = Toplevel(self.Raiz)
        self.tabla = ttk.Treeview(self.reporte_proveeores, show='headings', columns=("nombre", "direccion", "producto", "precio"), height=12)
        self.tabla.grid(row=0, column=0)

        self.tabla.column("nombre", anchor="center")
        self.tabla.column("direccion", anchor="center")
        self.tabla.column("producto", anchor="center")
        self.tabla.column("precio", anchor="center")

        self.tabla.heading("nombre", text='Nombre')
        self.tabla.heading("direccion", text='Dirección')
        self.tabla.heading("producto", text='Producto')
        self.tabla.heading("precio", text='Precio unitario')

        self.barra = Scrollbar(self.reporte_proveeores, orient="vertical", command=self.tabla.yview())
        self.barra.grid(row=0, column=2, sticky="ns")
        self.tabla.config(yscrollcommand=self.barra.set)

        self.muestra_datos()

    def muestra_datos(self):
        self.llamada = Archivos_proveedores()
        self.muestra = self.llamada.info()
        for i in self.muestra:
            self.linea = i.split("  ")
            self.tabla.insert("", END, text="", values=(self.linea[0], self.linea[1], self.linea[2], self.linea[3]))

    def ventana_principal(self):

        self.menu.add_command(label="Lista de proveedores", command=lambda:self.reporte())
        self.fondo_crear = PhotoImage(file='Boton_nuevo_proveedor.gif')
        self.Bagregar = Button(self.Raiz, image=self.fondo_crear, command=lambda: self.registrar())
        self.Bagregar.place(x=140, y=220)
        self.Bagregar.config(bd=0)

        self.fondo_borrar = PhotoImage(file='boton_eliminar_proveedor.gif')
        self.Bborrar = Button(self.Raiz, image=self.fondo_borrar, command=lambda: self.eliminar())
        self.Bborrar.place(x=140, y=275)
        self.Bborrar.config(bd=0)

        self.fodo_buscar = PhotoImage(file='boton_buscar.gif')
        self.Bbuscar = Button(self.Raiz, image=self.fodo_buscar, command=lambda: self.buscar())
        self.Bbuscar.place(x=260, y=220)
        self.Bbuscar.config(bd=0)

        self.fondo_editar = PhotoImage(file='boton_editar_proveedor.gif')
        self.Beditar = Button(self.Raiz, image=self.fondo_editar, cursor="hand2", command=lambda: self.editar())
        self.Beditar.place(x=260, y=275)
        self.Beditar.config(bd=0)

        self.imagen_boton_regresar = PhotoImage(file="boton_regresar.GIF")
        self.Boton_regresar = Button(self.Raiz, image=self.imagen_boton_regresar, width=120, height=65,
                                        cursor="hand2", border=0,
                                        command=lambda: self.volver(self.Raiz, self.pantalla_principal1))
        self.Boton_regresar.place(x=2, y=240)

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

