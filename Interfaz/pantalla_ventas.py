#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter as tk
import ttk
import os
import sys
import tkMessageBox as ms
from datetime import datetime
from funcionalidad.Manejar_archivos_productos import Manejar_archivos_productos
from funcionalidad.Evento_regresar import Cerrar_Ventanas
from funcionalidad.Manejar_archivos_ventas import Manejar_archivos_ventas

class Ventas(Cerrar_Ventanas):

    def __init__(self, pantalla_principal):
        self.pantalla_principal1 = pantalla_principal
        self.raiz = tk.Toplevel(self.pantalla_principal1)
        self.raiz.geometry('931x505')
        self.raiz.title("Ventas")
        self.raiz.resizable(False, False) 
        self.imagen = tk.PhotoImage(file="fondo_ventas.GIF")
        self.fondo = tk.Label(self.raiz, image=self.imagen).place(x=0, y=0)
        #evento accionado cuando la ventana es destruida
        self.raiz.bind("<Destroy>",lambda event: self.volver_con_cerrado_ventana(event,self.pantalla_principal1))
        self.manejar_archivos_productos = Manejar_archivos_productos()
        self.manejar_archivos_venta = Manejar_archivos_ventas()
        self.tiempo = datetime.now()
        self.mostrar_total = tk.StringVar()
        self.Codigo_producto = tk.StringVar()
        self.Cantidad = tk.IntVar()
        self.acumulador = 0
        
    def ventana_principal(self):
        """ Muestra todos los productos"""
        self.Entry_Codigo_producto = tk.Entry(self.raiz, textvariable=self.Codigo_producto, width=25)
        self.Entry_Codigo_producto.place(x=75, y=69)
        self.Entry_Cantidad = tk.Entry(self.raiz, textvariable=self.Cantidad, width=10)
        self.Entry_Cantidad.place(x=310, y=69)

        self.mostrar_total_a_pagar = tk.Label(self.raiz, textvariable= self.mostrar_total, font=("Verdana",24), width=10)
        self.mostrar_total_a_pagar.place(x=75, y=250)

        self.tabla = ttk.Treeview(self.raiz, show='headings', columns=("#1", "#2", "#3", "#4", "#5"), height=12)
        #self.tabla.place(x=330, y =150)
        self.tabla.grid(row=1, column=9, pady=150, columnspan=2, padx=300)

        self.tabla.column("#1", width=150, anchor="center")
        self.tabla.column("#2", width=150, anchor="center")
        self.tabla.column("#3", width=100, anchor="center")
        self.tabla.column("#4", width=80, anchor="center")
        self.tabla.column("#5", width=90, anchor="center")
        

        self.tabla.heading("#1", text="Codigo de Producto")
        self.tabla.heading("#2", text="Nombre")
        self.tabla.heading("#3", text="Precio unitario")
        self.tabla.heading("#4", text="Cantidad")
        self.tabla.heading("#5", text="Total por piezas")
        

        self.scrollbar = tk.Scrollbar(self.raiz, orient="vertical", command=self.tabla.yview)
        #self.scrollbar.place(x=330, y =150)
        self.scrollbar.grid(row=1, column=10, sticky='ns', pady=150)
        self.tabla.config(yscrollcommand=self.scrollbar.set)


        self.imagen_boton_agregar_venta = tk.PhotoImage(file="agregar_venta_tabla.GIF")
        self.Boton_agregar_venta = tk.Button(self.raiz, image=self.imagen_boton_agregar_venta, width=76, height=29,cursor="hand2",border=0,  command=lambda:self.Agregar_item() )
        self.Boton_agregar_venta.place(x=400, y=61)

        self.imagen_boton_remover_venta = tk.PhotoImage(file="remover_venta_tabla.GIF")
        self.Boton_remover_venta = tk.Button(self.raiz, image=self.imagen_boton_remover_venta, width=89, height=28,cursor="hand2",border=0,  command=lambda:self.Remover_item() )
        self.Boton_remover_venta.place(x=488, y=61)

        self.imagen_boton_regresar = tk.PhotoImage(file="boton_regresar.GIF")
        self.Boton_regresar = tk.Button(self.raiz, image=self.imagen_boton_regresar, width=120, height=65,cursor="hand2",border=0,  command=lambda:self.volver(self.raiz, self.pantalla_principal1) )
        self.Boton_regresar.place(x=2, y=430)

        self.imagen_boton_venta = tk.PhotoImage(file="registrar_venta.GIF")
        self.Boton_venta = tk.Button(self.raiz, image=self.imagen_boton_venta, width=250, height=40,cursor="hand2",border=0,  command=lambda:self.Registrar_venta() )
        self.Boton_venta.place(x=670, y=430)

    
        self.pantalla_principal1.withdraw()

    def Agregar_item(self):
        """Agrega un producto a la tabla"""
        try:
            self.datos_producto = self.manejar_archivos_productos.Buscar(self.Codigo_producto.get())
            if(self.datos_producto == 0):
                ms.showerror("", "el producto que intentas agregar no existe")
            else: 
                self.nombre = self.datos_producto[1] 
                self.precio_unitario = float(self.datos_producto[2])
                self.cantidad_por_precio = self.precio_unitario * self.Cantidad.get()
                self.cantidad_en_existencia = int(self.datos_producto[3])

                if(self.cantidad_en_existencia >= self.Cantidad.get()):
                    self.tabla.insert("",tk.END,text="", iid=self.Codigo_producto.get(), values=(self.Codigo_producto.get(), self.nombre, self.precio_unitario, self.Cantidad.get(), self.cantidad_por_precio) )
                    self.acumulador += self.cantidad_por_precio
                    self.mostrar_total.set( "$" + str(self.acumulador))
                else:
                    ms.showinfo("", "El producto " + self.nombre + " solo cuenta con " + str(self.cantidad_en_existencia) + " unidades")
        except:
            ms.showerror("Error!!!", "Ya has agregado este producto")
        finally:
            self.limpiar_campos()
            

    def Remover_item(self):
        """Elimina el producto con el ide indicado"""
        try:
            self.lista_valores_item = self.tabla.item(self.Codigo_producto.get())
            self.acumulador -= float(self.lista_valores_item["values"][4])
            self.mostrar_total.set("$" + str(self.acumulador))
            self.tabla.delete(self.Codigo_producto.get())
            
        except:
            ms.showerror("Error!!!", "Ya ha sido eliminado ese producto de la tabla")
        finally:
            self.limpiar_campos()

    def Registrar_venta(self):
        """Manda a la base de de datos la venta"""
        self.fecha_de_hoy = str(self.tiempo.day) + "/" + str(self.tiempo.month) + "/" + str(self.tiempo.year)
        self.lista = self.tabla.get_children()
        for i in self.lista:
            diccionario = self.tabla.item(i)
            self.manejar_archivos_venta.Insertar(self.fecha_de_hoy, str(diccionario["values"][0]), diccionario["values"][1], str(diccionario["values"][2]), str(diccionario["values"][3]), str(diccionario["values"][4]))
            self.buscar_modificar_producto(str(diccionario["values"][0]), str(diccionario["values"][3]))
            self.tabla.delete(i)
        self.limpiar_campos()
        self.acumulador = 0
        self.mostrar_total.set("$0.0")

    def limpiar_campos(self):
        self.Codigo_producto.set("")
        self.Cantidad.set("")

    def buscar_modificar_producto(self, codigo_producto, unidades_vendidas):
        self.datos_producto = self.manejar_archivos_productos.Buscar(codigo_producto)
        if(self.datos_producto == 0):
            ms.showerror("", "El producto que intentas agregar no existe")
        else: 
            self.nueva_cantidad = str(int(self.datos_producto[3]) - int(unidades_vendidas))
            self.manejar_archivos_productos.Modificar(self.datos_producto[0], self.datos_producto[1], self.datos_producto[2], self.nueva_cantidad, self.datos_producto[4], self.datos_producto[5], self.datos_producto[6])
            ms.showinfo("", "La venta se ha registrado con exito ")


    def volver(self, nombre_ventana_actual, nombre_ventana_anterior):
        nombre_ventana_anterior.deiconify()
        nombre_ventana_actual.destroy()

