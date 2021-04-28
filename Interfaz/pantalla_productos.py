#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter as tk
import ttk
import tkMessageBox as ms
from funcionalidad.Manejar_archivos_productos import Manejar_archivos_productos

class Productos:


    def __init__(self, pantalla_principal):
        self.raiz = tk.Toplevel(pantalla_principal)
        self.raiz.geometry('533x425')
        self.raiz.title("Registro Productos")
        self.raiz.resizable(False, False) 
        self.imagen = tk.PhotoImage(file="fondoProductos.GIF")
        self.fondo = tk.Label(self.raiz, image=self.imagen).place(x=0, y=0)
        self.instanciaManejarProductos = Manejar_archivos_productos()
        self.NombreProducto = tk.StringVar()
        self.Codigo_producto = tk.StringVar()
        self.Precio_producto = tk.StringVar()
        self.Cantidad_producto = tk.StringVar()
        self.Marca_producto =  tk.StringVar()
        self.Proveedor = tk.StringVar() 
        self.Fecha_de_entrega = tk.StringVar()


        self.ventana_principal()

    def ventana_principal(self):
        """ muestra los campos para insertar informacion de los productos"""
        
        self.Entry_Codigo_producto = tk.Entry(self.raiz, textvariable=self.Codigo_producto, width=25)
        self.Entry_Codigo_producto.place(x=255, y =23)

        self.Entry_NombreProducto = tk.Entry(self.raiz, textvariable=self.NombreProducto, width=25)
        self.Entry_NombreProducto.place(x=255, y =63)
        
        self.Entry_Precio_producto = tk.Entry(self.raiz, textvariable=self.Precio_producto, width=25)
        self.Entry_Precio_producto.place(x=255, y =98)

        self.Entry_Cantidad_producto = tk.Entry(self.raiz, textvariable=self.Cantidad_producto, width=25)
        self.Entry_Cantidad_producto.place(x=255, y =134)

        self.Entry_Marca_producto = tk.Entry(self.raiz, textvariable=self.Marca_producto, width=25)
        self.Entry_Marca_producto.place(x=255, y =167)

        self.Entry_Proveedor = tk.Entry(self.raiz, textvariable=self.Proveedor, width=25)
        self.Entry_Proveedor.place(x=255, y =201)

        self.Entry_Fecha_de_entrega = tk.Entry(self.raiz, textvariable=self.Fecha_de_entrega, width=25)
        self.Entry_Fecha_de_entrega.place(x=255, y =237)

        self.imagen_boton_CrearProductos = tk.PhotoImage(file="crearProductos.GIF")
        self.Boton_regresar = tk.Button(self.raiz, image=self.imagen_boton_CrearProductos, width=66, height=30,cursor="hand2",border=0,  command=lambda:self.crear_registro()) 
        self.Boton_regresar.place(x=20, y=270)

        self.imagen_boton_ModificarProductos = tk.PhotoImage(file="ModificarProducto.GIF")
        self.Boton_regresar = tk.Button(self.raiz, image=self.imagen_boton_ModificarProductos, width=84, height=35,cursor="hand2",border=0,  command=lambda:self.Modificar_registro())
        self.Boton_regresar.place(x=100, y=267)

        self.imagen_boton_BuscarProductos = tk.PhotoImage(file="BuscarProducto.GIF")
        self.Boton_regresar = tk.Button(self.raiz, image=self.imagen_boton_BuscarProductos, width=68, height=31,cursor="hand2",border=0,  command=lambda:self.Buscar_registro() )
        self.Boton_regresar.place(x=200, y=269)

        self.imagen_boton_EliminarProductos = tk.PhotoImage(file="EliminarProducto.GIF")
        self.Boton_regresar = tk.Button(self.raiz, image=self.imagen_boton_EliminarProductos, width=80, height=33,cursor="hand2",border=0,  command=lambda:self.Eliminar_registro() )
        self.Boton_regresar.place(x=280, y=269)

        self.imagen_boton_regresar = tk.PhotoImage(file="boton_regresar.GIF")
        self.Boton_regresar = tk.Button(self.raiz, image=self.imagen_boton_regresar, width=120, height=65,cursor="hand2",border=0,  command=lambda:instaciaciones() )
        self.Boton_regresar.place(x=2, y=340)
        
        self.raiz.mainloop()

    def Borrar_entrys(self):
        self.Codigo_producto.set("")
        self.NombreProducto.set("")
        self.Precio_producto.set("")
        self.Cantidad_producto.set("")
        self.Marca_producto.set("")
        self.Proveedor.set("")
        self.Fecha_de_entrega.set("")

    def crear_registro(self):
        self.bandera = self.instanciaManejarProductos.insertar_nuevo_producto(self.Codigo_producto.get(),
            self.NombreProducto.get(), self.Precio_producto.get(), self.Cantidad_producto.get(), self.Marca_producto.get(), self.Proveedor.get(), self.Fecha_de_entrega.get())
        if(self.bandera):
            ms.showinfo("", "El producto se ha registrado con exito!")
        else:
            ms.showerror("ERROR!!!", "El producto no ha podido ser registrado" )
        self.Borrar_entrys()

    def Modificar_registro(self):
        self.bandera = self.instanciaManejarProductos.modificar_producto(self.Codigo_producto.get(),
            self.NombreProducto.get(), self.Precio_producto.get(), self.Cantidad_producto.get(), self.Marca_producto.get(), self.Proveedor.get(), self.Fecha_de_entrega.get())
        if(self.bandera):
            ms.showinfo("", "El producto se ha modificado con exito!")
        else:
            ms.showerror("ERROR!!!", "El producto no ha podido ser modificado" )
        self.Borrar_entrys()


    def Buscar_registro(self):
        self.listaDevuelta = self.instanciaManejarProductos.buscar_producto(self.Codigo_producto.get())
        if(self.listaDevuelta != 0):
            ms.showinfo("", "Los datos se ha encontrado!")
            self.Codigo_producto.set(self.listaDevuelta[0])
            self.NombreProducto.set(self.listaDevuelta[1])
            self.Precio_producto.set(self.listaDevuelta[2])
            self.Cantidad_producto.set(self.listaDevuelta[3])
            self.Marca_producto.set(self.listaDevuelta[4])
            self.Proveedor.set(self.listaDevuelta[5])
            self.Fecha_de_entrega.set(self.listaDevuelta[6])
            
        else:
            ms.showerror("ERROR!!!", "Este producto no exite, porfavor revise el codigo del producto" )
    
    def Eliminar_registro(self):
        self.bandera = self.instanciaManejarProductos.eliminar_producto(self.Codigo_producto.get())
        if(self.bandera):
            ms.showinfo("", "El producto se ha borrado con exito!")
        else:
            ms.showerror("ERROR!!!", "El producto no ha podido ser borrado" )
        self.Borrar_entrys()

        

