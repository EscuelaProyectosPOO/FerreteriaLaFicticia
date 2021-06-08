#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter as tk
import ttk
import os
import sys
import tkMessageBox as ms
from datetime import datetime
from funcionalidad.Manejar_archivos_ventas import Manejar_archivos_ventas
from funcionalidad.Exepciones import Vacio
from funcionalidad.Evento_regresar import Cerrar_Ventanas
import re
import datetime


class Pantalla_reporte_ventas(Cerrar_Ventanas):

    def __init__(self, pantalla_principal):
        self.pantalla_principal1 = pantalla_principal
        self.reporte_ventas = tk.Toplevel(self.pantalla_principal1)
        self.reporte_ventas.title("Reporte de ventas")
        self.reporte_ventas.geometry('1049x499')
        self.reporte_ventas.resizable(False, False)
        self.reporte_ventas.iconbitmap('imagenes/logo.ico')
        self.imagen1 = tk.PhotoImage(file="imagenes/fondo_reporte_ventas.GIF")
        self.fondo1 = tk.Label(self.reporte_ventas, image=self.imagen1).place(x=0, y=0, relwidth=1, relheight=1)
        self.fecha_buscar = tk.StringVar()
        self.reporte_ventas.bind("<Destroy>", lambda event: self.volver_con_cerrado_ventana(event, self.pantalla_principal1))

    def ventana_principal(self):
        self.imagen_boton_reporte = tk.PhotoImage(file="imagenes/buscar_reporte_ventas.GIF")
        self.boton_reporte = tk.Button(self.reporte_ventas, image=self.imagen_boton_reporte,  width=234, height=44, cursor="hand2",border=0, command=lambda:self.buscar_ventas_fecha())
        self.boton_reporte.place(x=395, y=20)

        self.entry = tk.Entry(self.reporte_ventas, textvariable=self.fecha_buscar, width=30, fg = 'grey')
        self.entry.place(x=200, y=35)
        self.entry.insert(0, "D/M/AAAA")
        self.entry.bind("<FocusIn>", lambda event: self.default(event,self.entry, "D/M/AAAA"))
        self.entry.bind("<FocusOut>", lambda event: self.default(event,self.entry, "D/M/AAAA"))

        self.tabla1 = ttk.Treeview(self.reporte_ventas, show='headings', columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7"), height=12)
        self.tabla1.grid(row=1, column=10, sticky='nesw', pady=100, columnspan=7, padx=80)

        self.tabla1.column("#1", width=100, anchor="center")
        self.tabla1.column("#2", width=35, anchor="center")
        self.tabla1.column("#3", width=120, anchor="center")
        self.tabla1.column("#4", width=100, anchor="center")
        self.tabla1.column("#5", width=150, anchor="center")
        self.tabla1.column("#6", width=150, anchor="center")
        self.tabla1.column("#7", width=150, anchor="center")


        self.tabla1.heading("#1", text="Fecha de venta")
        self.tabla1.heading("#2",  text="Hora")
        self.tabla1.heading("#3", text="Código de Producto")
        self.tabla1.heading("#4", text="Nombre")
        self.tabla1.heading("#5", text="Precio unitario")
        self.tabla1.heading("#6", text="Cantidad")
        self.tabla1.heading("#7", text="Total por piezas")

        

        self.scrollbar = tk.Scrollbar(self.reporte_ventas, orient="vertical", command=self.tabla1.yview)
        self.scrollbar.grid(row=1, column=16, sticky='ns', pady=100)
        self.tabla1.config(yscrollcommand=self.scrollbar.set)

        self.datos_reporte()



    def datos_reporte(self):
        """Trae datos del archivo Base_Ventas"""
        self.manejar_archivos_venta = Manejar_archivos_ventas()
        self.informacion_del_archivo = self.manejar_archivos_venta.traer_informacion()
        self.informacion_del_archivo.reverse()
        for linea in self.informacion_del_archivo:
            self.lineas = linea.split("  ")
            self.tabla1.insert("",tk.END,text="", values=(self.lineas[0], self.lineas[1], self.lineas[2], self.lineas[3], self.lineas[4], self.lineas[5], self.lineas[6]))
    
    def default(self, event, entry, texto_insertado):
        """ Coloca las indicaciones temporales en los entrys """
        self.informacion_entry = entry.get()
        if(self.informacion_entry == "D/M/AAAA"):
            entry.delete(0, tk.END)
            entry.config(fg="black")

        elif(self.informacion_entry == ""):

            entry.insert(0,texto_insertado)
            entry.config(fg="grey") 

    def buscar_ventas_fecha(self):
        """ Busca las fechas indicadas en el entry de ventas  """
        try:
            self.info = (self.fecha_buscar.get()).strip()
            if(self.info == "" or self.info == "D/M/AAAA"):
                raise Vacio
            else:
                if(re.search("-", self.info)):
                    self.fecha1 = self.info[0:(re.search("-", self.info)).start()]
                    self.fecha2 = self.info[(re.search("-", self.info)).end():]
            
                    self.Info_fecha1 = self.manejar_archivos_venta.buscar_linea_en_archivo_de_texto(self.fecha1)
                    self.Info_fecha2 = self.manejar_archivos_venta.buscar_linea_en_archivo_de_texto(self.fecha2)

                    if(len(self.Info_fecha1) == 0 or len(self.Info_fecha2) == 0 ):
                        ms.showinfo("Ups!!", "No tenemos ventas registradas entre las fechas " + self.info)
                    else:
                        self.date_fecha1 = datetime.datetime(int(self.fecha1[(len(self.fecha1)-4):]),  int(self.fecha1[(re.search("/", self.fecha1)).end():len(self.fecha1)-5]),  int(self.fecha1[0:(re.search("/", self.fecha1)).start()])    )
                        self.date_fecha2 = datetime.datetime(int(self.fecha2[(len(self.fecha2)-4):]),  int(self.fecha2[(re.search("/", self.fecha2)).end():len(self.fecha2)-5]),  int(self.fecha2[0:(re.search("/", self.fecha2)).start()])    )


                        self.variable_temporal = self.manejar_archivos_venta.traer_informacion()



                        if(self.date_fecha1 < self.date_fecha2):

                            self.index_fecha1 = self.variable_temporal.index(self.Info_fecha1[0])
                            self.Info_fecha2.reverse()
                            self.index_fecha2 = self.variable_temporal.index(self.Info_fecha2[0])

                        elif(self.date_fecha1 > self.date_fecha2):

                            self.index_fecha2 = self.variable_temporal.index(self.Info_fecha2[0])
                            self.Info_fecha1.reverse()
                            self.index_fecha1 = self.variable_temporal.index(self.Info_fecha1[0])


                        if(self.index_fecha1 > self.index_fecha2):
                            self.inicio =self.index_fecha2
                            self.fin = self.index_fecha1 +1
                        else:
                            self.inicio = self.index_fecha1
                            self.fin = self.index_fecha2 +1

                        self.informacion_del_archivo =[]
                        for i in range(self.inicio, self.fin):
                            self.informacion_del_archivo.append(self.variable_temporal[i])

                        self.informacion_del_archivo.reverse()
    
                else:
                    self.informacion_del_archivo = self.manejar_archivos_venta.buscar_linea_en_archivo_de_texto(self.info)
                
                if(len(self.informacion_del_archivo) == 0):
                    ms.showinfo("Ups!!", "No tenemos ventas registradas en la fecha "+ self.info)
                else:
                    self.lista = self.tabla1.get_children()
                    for i in self.lista:
                        self.tabla1.delete(i)
                    for linea in self.informacion_del_archivo:
                        self.lineas = linea.split("  ")
                        self.tabla1.insert("",tk.END,text="", values=(self.lineas[0], self.lineas[1], self.lineas[2], self.lineas[3], self.lineas[4], self.lineas[5], self.lineas[6]))

        except Vacio as e:
            pass
        except ValueError as e:
            ms.showerror("Error!!!", "No se aceptan esos caracteres especiales")
        except Exception as e:
            ms.showerror("", e)
            print e
    def volver(self, nombre_ventana_actual, nombre_ventana_anterior):
        pass
    



