#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter as tk
import ttk
import os
import sys
from funcionalidad.Manejar_archivo_inventario import Manejar_archivo_inventario
from funcionalidad.Evento_regresar import Cerrar_Ventanas
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
        
    def ventana_principal(self):
        """ Muestra todos los productos"""
        self.Entry_ = tk.Entry(self.raiz, textvariable=self.Codigo_producto, width=25)
        self.Entry_Codigo_producto.place(x=255, y =23)
        self.tabla = ttk.Treeview(self.raiz, show='headings', columns=("#1", "#2", "#3", "#4"), height=10)
        self.tabla.grid(row=3, column=10)

        self.tabla.column("#1", width=150, anchor="center")
        self.tabla.column("#2", width=150, anchor="center")
        self.tabla.column("#3", width=100, anchor="center")
        self.tabla.column("#4", width=100, anchor="center")
        

        self.tabla.heading("#1", text="Codigo de Producto")
        self.tabla.heading("#2", text="Nombre")
        self.tabla.heading("#3", text="Precio unitario")
        self.tabla.heading("#4", text="Cantidad")
        

        self.scrollbar = tk.Scrollbar(self.raiz, orient="vertical", command=self.tabla.yview)
        self.scrollbar.grid(row=3, column=11,sticky='ns')
        self.tabla.config(yscrollcommand=self.scrollbar.set)

        self.Actualizar_inventario()

        self.imagen_boton_regresar = tk.PhotoImage(file="boton_regresar.GIF")
        self.Boton_regresar = tk.Button(self.raiz, image=self.imagen_boton_regresar, width=120, height=65,cursor="hand2",border=0,  command=lambda:self.volver(self.raiz, self.pantalla_principal1) )
        self.Boton_regresar.grid(row=4, column=3,padx=0, sticky='we')
        
        self.pantalla_principal1.withdraw()

    def Actualizar_inventario(self):
            for i in range(100):
                self.tabla.insert("",tk.END,text="", values=( i,"Creama Ponss", "345" ))

               

    def volver(self, nombre_ventana_actual, nombre_ventana_anterior):
        nombre_ventana_anterior.deiconify()
        nombre_ventana_actual.destroy()

root = tk.Tk()
uno = Ventas(root)
uno.ventana_principal()
root.mainloop()