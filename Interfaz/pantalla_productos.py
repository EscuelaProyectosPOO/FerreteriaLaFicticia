#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter as tk
import ttk
import tkMessageBox as ms
from funcionalidad.Manejar_archivos_productos import Manejar_archivos_productos
from funcionalidad.Evento_regresar import Cerrar_Ventanas
from funcionalidad.Exepciones import Vacio
from funcionalidad.Exepciones import CodigoProducto

class Productos(Cerrar_Ventanas):
    def __init__(self, pantalla_principal):
        self.pantalla_principal1 = pantalla_principal
        self.raiz = tk.Toplevel(self.pantalla_principal1)
        self.raiz.geometry('533x425')
        self.raiz.title("Registro Productos")
        self.raiz.resizable(False, False)
        self.raiz.iconbitmap('logo.ico')
        self.imagen = tk.PhotoImage(file="fondoProductos.GIF")
        self.fondo = tk.Label(self.raiz, image=self.imagen).place(x=0, y=0, relwidth=1, relheight=1)
        self.instanciaManejarProductos = Manejar_archivos_productos()
        self.NombreProducto = tk.StringVar()
        self.Codigo_producto = tk.StringVar()
        self.Precio_producto = tk.StringVar()
        self.Cantidad_producto = tk.StringVar()
        self.Marca_producto =  tk.StringVar()
        self.Proveedor = tk.StringVar() 
        self.Fecha_de_entrega = tk.StringVar()
        self.pantalla_principal1.withdraw()
        self.raiz.bind("<Destroy>",lambda event: self.volver_con_cerrado_ventana(event,self.pantalla_principal1))
        
        



    def ventana_principal(self):
        """ muestra los campos para insertar informacion de los productos"""
        
        self.Entry_Codigo_producto = tk.Entry(self.raiz, textvariable=self.Codigo_producto, width=25, fg = 'grey')
        self.Entry_Codigo_producto.place(x=255, y =23)
        self.Entry_Codigo_producto.insert(0, "Codigo de producto")
        self.Entry_Codigo_producto.bind("<FocusIn>", lambda event: self.default(event,self.Entry_Codigo_producto, "Codigo de producto"))
        self.Entry_Codigo_producto.bind("<FocusOut>", lambda event: self.default(event,self.Entry_Codigo_producto, "Codigo de producto"))

        self.Entry_NombreProducto = tk.Entry(self.raiz, textvariable=self.NombreProducto, width=25, fg = 'grey')
        self.Entry_NombreProducto.place(x=255, y =63)
        self.Entry_NombreProducto.insert(0, "Nombre")
        self.Entry_NombreProducto.bind("<FocusIn>", lambda event: self.default(event,self.Entry_NombreProducto, "Nombre"))
        self.Entry_NombreProducto.bind("<FocusOut>", lambda event: self.default(event,self.Entry_NombreProducto, "Nombre"))
        
        self.Entry_Precio_producto = tk.Entry(self.raiz, textvariable=self.Precio_producto, width=25, fg = 'grey')
        self.Entry_Precio_producto.place(x=255, y =98)
        self.Entry_Precio_producto.insert(0, "Precio")
        self.Entry_Precio_producto.bind("<FocusIn>", lambda event: self.default(event,self.Entry_Precio_producto, "Precio"))
        self.Entry_Precio_producto.bind("<FocusOut>", lambda event: self.default(event,self.Entry_Precio_producto, "Precio"))

        self.Entry_Cantidad_producto = tk.Entry(self.raiz, textvariable=self.Cantidad_producto, width=25, fg = 'grey')
        self.Entry_Cantidad_producto.place(x=255, y =134)
        self.Entry_Cantidad_producto.insert(0, "Cantidad")
        self.Entry_Cantidad_producto.bind("<FocusIn>", lambda event: self.default(event,self.Entry_Cantidad_producto, "Cantidad"))
        self.Entry_Cantidad_producto.bind("<FocusOut>", lambda event: self.default(event,self.Entry_Cantidad_producto, "Cantidad"))

        self.Entry_Marca_producto = tk.Entry(self.raiz, textvariable=self.Marca_producto, width=25, fg = 'grey')
        self.Entry_Marca_producto.place(x=255, y =167)
        self.Entry_Marca_producto.insert(0, "Marca")
        self.Entry_Marca_producto.bind("<FocusIn>", lambda event: self.default(event,self.Entry_Marca_producto, "Marca"))
        self.Entry_Marca_producto.bind("<FocusOut>", lambda event: self.default(event,self.Entry_Marca_producto, "Marca"))

        self.Entry_Proveedor = tk.Entry(self.raiz, textvariable=self.Proveedor, width=25, fg = 'grey')
        self.Entry_Proveedor.place(x=255, y =201)
        self.Entry_Proveedor.insert(0, "Proveedor")
        self.Entry_Proveedor.bind("<FocusIn>", lambda event: self.default(event,self.Entry_Proveedor, "Proveedor"))
        self.Entry_Proveedor.bind("<FocusOut>", lambda event: self.default(event,self.Entry_Proveedor, "Proveedor"))

        self.Entry_Fecha_de_entrega = tk.Entry(self.raiz, textvariable=self.Fecha_de_entrega, width=25, fg = 'grey')
        self.Entry_Fecha_de_entrega.place(x=255, y =237)
        self.Entry_Fecha_de_entrega.insert(0, "Fecha de entrega")
        self.Entry_Fecha_de_entrega.bind("<FocusIn>", lambda event: self.default(event,self.Entry_Fecha_de_entrega, "Fecha de entrega"))
        self.Entry_Fecha_de_entrega.bind("<FocusOut>", lambda event: self.default(event,self.Entry_Fecha_de_entrega, "Fecha de entrega"))

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
        self.Boton_regresar = tk.Button(self.raiz, image=self.imagen_boton_regresar, width=120, height=65,cursor="hand2",border=0,  command=lambda:self.volver(self.raiz, self.pantalla_principal1) )
        self.Boton_regresar.place(x=2, y=340)
        
        

    def Borrar_entrys(self):
        self.Codigo_producto.set("Codigo de producto")
        self.Entry_Codigo_producto.config(fg="grey") 
        self.NombreProducto.set("Nombre")
        self.Entry_NombreProducto.config(fg="grey") 
        self.Precio_producto.set("Precio")
        self.Entry_Precio_producto.config(fg="grey") 
        self.Cantidad_producto.set("Cantidad")
        self.Entry_Cantidad_producto.config(fg="grey") 
        self.Marca_producto.set("Marca")
        self.Entry_Marca_producto.config(fg="grey") 
        self.Proveedor.set("Proveedor")
        self.Entry_Proveedor.config(fg="grey") 
        self.Fecha_de_entrega.set("Fecha de entrega")
        self.Entry_Fecha_de_entrega.config(fg="grey") 
    
    def Colocar_color_entrys(self):

        self.Entry_Codigo_producto.config(fg="black") 
        self.Entry_NombreProducto.config(fg="black") 
        self.Entry_Precio_producto.config(fg="black") 
        self.Entry_Cantidad_producto.config(fg="black") 
        self.Entry_Marca_producto.config(fg="black") 
        self.Entry_Proveedor.config(fg="black") 
        self.Entry_Fecha_de_entrega.config(fg="black")
        

    def crear_registro(self):
        try:
            if((self.Codigo_producto.get()).strip() == "" or (self.NombreProducto.get()).strip() == ""
             or (self.Precio_producto.get()).strip() == "" or (self.Cantidad_producto.get()).strip() == "" 
             or (self.Marca_producto.get()).strip() == "" or (self.Proveedor.get()).strip() == "" or (self.Fecha_de_entrega.get()).strip() == "" 
             or (self.NombreProducto.get()).strip() == "Nombre" or (self.Codigo_producto.get()).strip() == "Codigo de producto" or (self.Precio_producto.get()).strip() == "Precio"
             or (self.Cantidad_producto.get()).strip() == "Cantidad" or (self.Marca_producto.get()).strip() == "Marca" or (self.Proveedor.get()).strip() == "Proveedor"
             or (self.Fecha_de_entrega.get()).strip() == "Fecha de entrega"):
                raise Vacio

            else:

                if(float(self.Precio_producto.get()) <=0 or  int(self.Cantidad_producto.get()) <= 0):

                    ms.showerror("", "El precio o la cantidad de producto no debe ser negativa ni nula")
                else:
                    self.respuesta_busqueda = self.instanciaManejarProductos.Buscar(self.Codigo_producto.get())
                    if(self.respuesta_busqueda != 0):
                        ms.showinfo("", "Este Producto ya ha sido registrado en el sistema")
                    else:
                        self.bandera = self.instanciaManejarProductos.Insertar(self.Codigo_producto.get(),
                            self.NombreProducto.get(), self.Precio_producto.get(), self.Cantidad_producto.get(), self.Marca_producto.get(), self.Proveedor.get(), self.Fecha_de_entrega.get())
                        if(self.bandera):
                            ms.showinfo("", "El producto se ha registrado con exito!")
                        else:
                            ms.showerror("ERROR!!!", "El producto no ha podido ser registrado" )
                        self.Borrar_entrys()
           
        except Vacio as e:
            print e
        except Exception as e:
            ms.showerror("", e)


    def Modificar_registro(self):
        try:
            if((self.Codigo_producto.get()).strip() == "" or (self.NombreProducto.get()).strip() == ""
             or (self.Precio_producto.get()).strip() == "" or (self.Cantidad_producto.get()).strip() == "" 
             or (self.Marca_producto.get()).strip() == "" or (self.Proveedor.get()).strip() == "" or (self.Fecha_de_entrega.get()).strip() == "" 
             or (self.NombreProducto.get()).strip() == "Nombre" or (self.Codigo_producto.get()).strip() == "Codigo de producto" or (self.Precio_producto.get()).strip() == "Precio"
             or (self.Cantidad_producto.get()).strip() == "Cantidad" or (self.Marca_producto.get()).strip() == "Marca" or (self.Proveedor.get()).strip() == "Proveedor"
             or (self.Fecha_de_entrega.get()).strip() == "Fecha de entrega"):
             
                raise Vacio

            else:
                self.bandera = self.instanciaManejarProductos.Modificar(self.Codigo_producto.get(),
                    self.NombreProducto.get(), self.Precio_producto.get(), self.Cantidad_producto.get(), self.Marca_producto.get(), self.Proveedor.get(), self.Fecha_de_entrega.get())
                if(self.bandera):
                    ms.showinfo("", "El producto se ha modificado con exito!")
                else:
                    ms.showerror("ERROR!!!", "El producto no ha podido ser modificado" )
                self.Borrar_entrys()
        except Vacio as e:
            print e
        except Exception as e:
            ms.showerror("", e)



    def Buscar_registro(self):
        try:
            if(self.Codigo_producto.get() == "" or self.Codigo_producto.get() == "Codigo de producto"):
                raise CodigoProducto
            else:
                self.listaDevuelta = self.instanciaManejarProductos.Buscar(self.Codigo_producto.get())
                if(self.listaDevuelta != 0):
                    ms.showinfo("", "Los datos se ha encontrado!")
                    self.Codigo_producto.set(self.listaDevuelta[0])
                    self.NombreProducto.set(self.listaDevuelta[1])
                    self.Precio_producto.set(self.listaDevuelta[2])
                    self.Cantidad_producto.set(self.listaDevuelta[3])
                    self.Marca_producto.set(self.listaDevuelta[4])
                    self.Proveedor.set(self.listaDevuelta[5])
                    self.Fecha_de_entrega.set(self.listaDevuelta[6]) 
                    self.Colocar_color_entrys()
                else:
                    ms.showerror("ERROR!!!", "Este producto no exite, porfavor revise el  código del producto" )
        except CodigoProducto as e:
            print type(e).__name__
        
    
    def Eliminar_registro(self):
        try:
            if(self.Codigo_producto.get() == "" or self.Codigo_producto.get() == "Codigo de producto"):
                raise CodigoProducto
            else:
                self.bandera = self.instanciaManejarProductos.Eliminar(self.Codigo_producto.get())
                if(self.bandera):
                    ms.showinfo("", "El producto se ha borrado con exito!")
                else:
                    ms.showerror("ERROR!!!", "El producto no ha podido ser borrado" )
                self.Borrar_entrys()
        except CodigoProducto as e:
            print type(e).__name__
            
    
    def volver(self, nombre_ventana_actual, nombre_ventana_anterior):
        nombre_ventana_anterior.deiconify()
        nombre_ventana_actual.destroy()

    def default(self, event, entry, texto_insertado):
        """ Coloca las indicaciones temporales en los entrys """
        self.informacion_entry = entry.get()
        if(self.informacion_entry == "Nombre" or self.informacion_entry == "Codigo de producto" or self.informacion_entry == "Precio"
            or self.informacion_entry == "Cantidad" or self.informacion_entry == "Marca" or self.informacion_entry == "Proveedor"
            or self.informacion_entry == "Fecha de entrega"):
            entry.delete(0, tk.END)
            entry.config(fg="black")

        elif(self.informacion_entry == ""):

            entry.insert(0,texto_insertado)
            entry.config(fg="grey") 
            
         
        