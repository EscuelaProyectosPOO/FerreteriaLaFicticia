#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter as tk
import ttk
import os
import sys
from funcionalidad.Manejar_archivo_inventario import Manejar_archivo_inventario
from funcionalidad.Evento_regresar import Cerrar_Ventanas
class Inventario(Cerrar_Ventanas):

    def __init__(self, pantalla_principal):
        self.pantalla_principal1 = pantalla_principal
        self.raiz = tk.Toplevel(self.pantalla_principal1)
        self.raiz.geometry('1169x563')
        self.raiz.title("Inventario")
        self.raiz.resizable(False, False) 
        self.imagen = tk.PhotoImage(file="fondo_sin_nada.GIF")
        self.fondo = tk.Label(self.raiz, image=self.imagen).place(x=0, y=0)
        
    def ventana_principal(self):
        """ Muestra todos los productos"""
        label = tk.Label(self.raiz).grid(row=0, column=30)
        self.tabla = ttk.Treeview(self.raiz, show='headings', columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7"), height=20)
        self.tabla.grid(row=1, column=30)

        self.tabla.column("#1", width=150, anchor="center")
        self.tabla.column("#2", width=150, anchor="center")
        self.tabla.column("#3", width=100, anchor="center")
        self.tabla.column("#4", width=100, anchor="center")
        self.tabla.column("#5", width=150, anchor="center")
        self.tabla.column("#6", width=150, anchor="center")
        self.tabla.column("#7", width=100, anchor="center")

        self.tabla.heading("#1", text="Codigo de Producto")
        self.tabla.heading("#2", text="Nombre")
        self.tabla.heading("#3", text="Precio")
        self.tabla.heading("#4", text="Cantidad")
        self.tabla.heading("#5", text="Marca")
        self.tabla.heading("#6", text="Proveedor")
        self.tabla.heading("#7", text="Fecha de entrega")

        self.scrollbar = tk.Scrollbar(self.raiz, orient="vertical", command=self.tabla.yview)
        self.scrollbar.grid(row=1, column=31, sticky='ns')
        self.tabla.config(yscrollcommand=self.scrollbar.set)

        self.Actualizar_inventario()

        self.imagen_boton_regresar = tk.PhotoImage(file="boton_regresar.GIF")
        self.Boton_regresar = tk.Button(self.raiz, image=self.imagen_boton_regresar, width=120, height=65,cursor="hand2",border=0,  command=lambda:self.volver(self.raiz, self.pantalla_principal1) )
        self.Boton_regresar.grid(row=2, column=10, sticky='we')
        
        self.pantalla_principal1.withdraw()

    def Actualizar_inventario(self):
        try:
            manejar_archivo_inventario = Manejar_archivo_inventario()
            self.informacion = manejar_archivo_inventario.traer_informacion_de_archivo_productos()
            for linea in self.informacion:
                #self.tabla.insert("",tk.END,text="", values=("12gjgee8","Creama Ponss", "345", "cuidado personal", "200", "Ponss" ))
                self.nueva_linea = linea.split("  ")
                self.tabla.insert("",tk.END,text="", values=(self.nueva_linea[0], self.nueva_linea[1], self.nueva_linea[2], self.nueva_linea[3], self.nueva_linea[4], self.nueva_linea[5], self.nueva_linea[6] ))
        except:
            print ("Error en actualizar inventario")

    def volver(self, nombre_ventana_actual, nombre_ventana_anterior):
        nombre_ventana_anterior.deiconify()
        nombre_ventana_actual.destroy()


