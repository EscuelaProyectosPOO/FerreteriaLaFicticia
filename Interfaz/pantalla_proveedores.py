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
        self.Raiz.iconbitmap('imagenes/logo.ico')
        self.imagen = PhotoImage(file='imagenes/fondo_proveeores.gif')
        self.fondo = Label(self.Raiz, image=self.imagen)
        self.fondo.place(x=0, y=0)
        self.NombreText = StringVar()
        self.menu = Menu(self.Raiz)
        self.Raiz.config(menu=self.menu)

        self.Raiz.bind("<Destroy>", lambda event: self.volver_con_cerrado_ventana(event, self.pantalla_principal1))


    def limpiar(self):
        self.NombreText.set('')
        self.direcText.set('')
        self.precioText.set('')
        self.productoText.set('')
        self.Nombre.insert(0, 'Nombre')
        self.Nombre.config(fg="grey")
        self.Nombre.bind("<FocusIn>", lambda event: self.default(event, self.Nombre, "Nombre"))
        self.Nombre.bind("<FocusOut>", lambda event: self.default(event, self.Nombre, "Nombre"))

        self.Direccion.insert(0, 'Direccion')
        self.Direccion.config(fg="grey")
        self.Direccion.bind("<FocusIn>", lambda event: self.default(event, self.Direccion, "Direccion"))
        self.Direccion.bind("<FocusOut>", lambda event: self.default(event, self.Direccion, "Direccion"))

        self.Producto.insert(0, 'Producto')
        self.Producto.config(fg="grey")
        self.Producto.bind("<FocusIn>", lambda event: self.default(event, self.Producto, "Producto"))
        self.Producto.bind("<FocusOut>", lambda event: self.default(event, self.Producto, "Producto"))

        self.Precio.insert(0, 'Precio')
        self.Precio.config(fg="grey")
        self.Precio.bind("<FocusIn>", lambda event: self.default(event, self.Precio, "Precio"))
        self.Precio.bind("<FocusOut>", lambda event: self.default(event, self.Precio, "Precio"))

    def buscar(self):
        self.instancia_buscar = Archivos_proveedores()
        self.linea_devuelta = self.instancia_buscar.Buscar(self.NombreText.get())
        if self.linea_devuelta == 0:
            mensajes.showerror('ERROR', 'Elemento no encontrado')
        else:
            self.NombreText.set(self.linea_devuelta[0])
            self.Nombre.config(fg='black')
            self.direcText.set(self.linea_devuelta[1])
            self.Direccion.config(fg='black')
            self.productoText.set(self.linea_devuelta[2])
            self.Producto.config(fg='black')
            self.precioText.set(self.linea_devuelta[3])
            self.Precio.config(fg='black')

    def registrar(self):
        band = True
        var = 0
        try:
            if self.NombreText.get() == '' or self.direcText.get() == '' or self.precioText.get() == '' or self.productoText.get() == '':
                raise Vacio
        except Vacio as v:
            print Vacio, v
            band = False

        num = True
        try:
            var = float(self.precioText.get())
        except ValueError:
            num= False

        try:
            if num == False and band == True:
                raise Numeros
            try:
                if var <= -1:
                    raise Negativos
            except Negativos as N:
                print Negativos, N
                band = False

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
        band = True
        var = 0
        try:
            if self.NombreText.get() == '' or self.direcText.get() == '' or self.precioText.get() == '' or self.productoText.get() == '':
                raise Vacio
        except Vacio as v:
            print Vacio, v
            band = False

        num = True
        try:
            var = float(self.precioText.get())
        except ValueError:
            num = False

        try:
            if num == False and band == True:
                raise Numeros
            try:
                if var <= -1:
                    raise Negativos
            except Negativos as N:
                print Negativos, N
                band = False

        except Numeros as n:
            print Numeros, n
            band = False

        if band == True:
            self.instancia_editar = Archivos_proveedores()
            self.indicador = self.instancia_editar.Modificar(self.NombreText.get(), self.direcText.get(), self.productoText.get(), self.precioText.get())
            if (self.indicador):
                mensajes.showinfo('', 'Elemento modificado con éxito')
            else:
                mensajes.showerror('ERROR', 'No se encuentra el proveedor')
            self.limpiar()

    def reporte(self):
        self.reporte_proveeores = Toplevel(self.Raiz)
        self.reporte_proveeores.title('Reporte de proveedores')
        self.reporte_proveeores.resizable(0, 0)
        self.reporte_proveeores.iconbitmap('imagenes/logo.ico')
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
        self.fondo_crear = PhotoImage(file='imagenes/Boton_nuevo_proveedor.gif')
        self.Bagregar = Button(self.Raiz, image=self.fondo_crear, command=lambda: self.registrar())
        self.Bagregar.place(x=140, y=220)
        self.Bagregar.config(bd=0)

        self.fondo_borrar = PhotoImage(file='imagenes/boton_eliminar_proveedor.gif')
        self.Bborrar = Button(self.Raiz, image=self.fondo_borrar, command=lambda: self.eliminar())
        self.Bborrar.place(x=140, y=275)
        self.Bborrar.config(bd=0)

        self.fodo_buscar = PhotoImage(file='imagenes/boton_buscar.gif')
        self.Bbuscar = Button(self.Raiz, image=self.fodo_buscar, command=lambda: self.buscar())
        self.Bbuscar.place(x=260, y=220)
        self.Bbuscar.config(bd=0)

        self.fondo_editar = PhotoImage(file='imagenes/boton_editar_proveedor.gif')
        self.Beditar = Button(self.Raiz, image=self.fondo_editar, cursor="hand2", command=lambda: self.editar())
        self.Beditar.place(x=260, y=275)
        self.Beditar.config(bd=0)

        self.imagen_boton_regresar = PhotoImage(file="imagenes/boton_regresar.GIF")
        self.Boton_regresar = Button(self.Raiz, image=self.imagen_boton_regresar, width=120, height=65,
                                        cursor="hand2", border=0,
                                        command=lambda: self.volver(self.Raiz, self.pantalla_principal1))
        self.Boton_regresar.place(x=2, y=240)


        self.Nombre = Entry(self.Raiz, textvariable=self.NombreText, width=30, fg='grey')
        self.Nombre.place(x=170, y=25)
        self.Nombre.insert(0, 'Nombre')
        self.Nombre.bind("<FocusIn>", lambda event: self.default(event, self.Nombre, "Nombre"))
        self.Nombre.bind("<FocusOut>", lambda event: self.default(event, self.Nombre, "Nombre"))

        self.direcText = StringVar()
        self.Direccion = Entry(self.Raiz, textvariable=self.direcText, width=30, fg='grey')
        self.Direccion.place(x=170, y=70)
        self.Direccion.insert(0, 'Direccion')
        self.Direccion.bind("<FocusIn>", lambda event: self.default(event, self.Direccion, "Direccion"))
        self.Direccion.bind("<FocusOut>", lambda event: self.default(event, self.Direccion, "Direccion"))

        self.productoText = StringVar()
        self.Producto = Entry(self.Raiz, textvariable=self.productoText, width=30, fg='grey')
        self.Producto.place(x=170, y=120)
        self.Producto.insert(0, 'Producto')
        self.Producto.bind("<FocusIn>", lambda event: self.default(event, self.Producto, "Producto"))
        self.Producto.bind("<FocusOut>", lambda event: self.default(event, self.Producto, "Producto"))

        self.precioText = StringVar()
        self.Precio = Entry(self.Raiz, textvariable=self.precioText, width=30, fg='grey')
        self.Precio.place(x=170, y=170)
        self.Precio.insert(0, 'Precio')
        self.Precio.bind("<FocusIn>", lambda event: self.default(event, self.Precio, "Precio"))
        self.Precio.bind("<FocusOut>", lambda event: self.default(event, self.Precio, "Precio"))

        self.pantalla_principal1.withdraw()

    def volver(self, nombre_ventana_actual, nombre_ventana_anterior):
        nombre_ventana_anterior.deiconify()
        nombre_ventana_actual.destroy()

    def default(self, event, entry, texto_insertado):
        self.informacion_entry = entry.get()
        if(self.informacion_entry == "Nombre" or self.informacion_entry == "Direccion" or self.informacion_entry == "Precio" or self.informacion_entry == "Producto"):
            entry.delete(0, END)
            entry.config(fg="black")
        elif (self.informacion_entry == ""):
            entry.insert(0, texto_insertado)
            entry.config(fg="grey")


