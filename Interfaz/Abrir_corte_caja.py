#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter as tk
from datetime import datetime
import tkMessageBox as ms
from funcionalidad.Manejo_archivos_corte_caja import Manejar_archivos_corte_caja
from funcionalidad.Exepciones import Campos_vacios_en_ventas
import ttk



class Abrir_corte():

    def __init__(self, pantalla_principal):
        self.pantalla_principal1 = pantalla_principal
        self.raiz = tk.Toplevel(self.pantalla_principal1)
        self.raiz.geometry('472x292')
        self.raiz.title("Abrir corte caja")
        self.raiz.resizable(False, False)
        self.raiz.iconbitmap('imagenes/logo.ico')
        self.imagen = tk.PhotoImage(file="imagenes/abrir_corte.GIF")
        self.fondo = tk.Label(self.raiz, image=self.imagen).place(x=0, y=0, relwidth=1, relheight=1)
        self.Barra_menu_principal = tk.Menu(self.raiz)
        self.tiempo = datetime.now()
        self.manejar_archivos_corte_caja = Manejar_archivos_corte_caja()
        self.datos_numero_caja = tk.StringVar()
        self.datos_nombre_usuario = tk.StringVar()
        self.datos_fecha = tk.StringVar()
        self.datos_hora = tk.StringVar()
        self.datos_fondo_recibido = tk.StringVar()


    def ventana_principal(self):
        self.imagen_fondo_a_entregar = tk.PhotoImage(file="imagenes/fondo_a_entregar.GIF")
        self.label_fondo_a_entregar = tk.Label(self.raiz, image=self.imagen_fondo_a_entregar, width=180, height=20)
        
        self.entry_numero_caja = tk.Entry(self.raiz, fg="grey", textvariable=self.datos_numero_caja)
        self.entry_numero_caja.place(x=90, y=27)
        self.entry_numero_caja.insert(0,"Numero de caja")
        self.entry_numero_caja.bind("<FocusIn>", lambda event: self.default(event,self.entry_numero_caja,"Numero de caja"))
        self.entry_numero_caja.bind("<FocusOut>", lambda event: self.default(event, self.entry_numero_caja,"Numero de caja"))

        self.entry_nombre_usuario = tk.Entry(self.raiz, fg="grey", textvariable=self.datos_nombre_usuario)
        self.entry_nombre_usuario.place(x=90, y=62)
        self.entry_nombre_usuario.insert(0, "Nombre de usuario")
        self.entry_nombre_usuario.bind("<FocusIn>",lambda event: self.default(event, self.entry_nombre_usuario, "Nombre de usuario"))
        self.entry_nombre_usuario.bind("<FocusOut>", lambda event: self.default(event, self.entry_nombre_usuario, "Nombre de usuario"))


        self.fecha_de_hoy = str(self.tiempo.day) + "/" + str(self.tiempo.month) + "/" + str(self.tiempo.year)
        self.entry_fecha_apertura = tk.Entry(self.raiz, textvariable=self.datos_fecha)
        self.entry_fecha_apertura.place(x=333,y=27)
        self.entry_fecha_apertura.insert(0, self.fecha_de_hoy)
        self.entry_fecha_apertura.bind("<FocusIn>", lambda event: self.default(event, self.entry_fecha_apertura,"DD/M/AAAA"))
        self.entry_fecha_apertura.bind("<FocusOut>", lambda event: self.default(event, self.entry_fecha_apertura,"DD/M/AAAA"))

        self.hora_correcta()
        self.entry_hora_apertura= tk.Entry(self.raiz, textvariable=self.datos_hora)
        self.entry_hora_apertura.place(x=333, y=62)
        self.entry_hora_apertura.insert(0, self.hora)
        self.entry_hora_apertura.bind("<FocusIn>", lambda event: self.default(event, self.entry_hora_apertura, "Hora"))
        self.entry_hora_apertura.bind("<FocusOut>", lambda event: self.default(event, self.entry_hora_apertura, "Hora"))

        self.entry_fondo_recibido = tk.Entry(self.raiz, textvariable=self.datos_fondo_recibido)
        self.entry_fondo_recibido.place(x=100, y=184)

        self.combo_box = ttk.Combobox(self.raiz, values=["Abrir corte de caja", "Cerrar corte de caja"], state="readonly")
        self.combo_box.place(x=99, y=220)
        self.combo_box.current(0)
        self.combo_box.bind("<<ComboboxSelected>>", lambda event: self.obtener_combo(event, self.combo_box.current()))

        self.imagen_boton_abrir_corte = tk.PhotoImage(file="imagenes/Abrir_corte_boton.GIF")
        self.Boton_abrir_corte = tk.Button(self.raiz, image=self.imagen_boton_abrir_corte, width=128, height=28, cursor="hand2", border=0, command=lambda: self.abrir_corte())
        self.Boton_abrir_corte.place(x=330, y=260)

        self.imagen_boton_cerrar_corte = tk.PhotoImage(file="imagenes/cerrar_corte.GIF")
        self.Boton_cerrar_corte = tk.Button(self.raiz, image=self.imagen_boton_cerrar_corte, width=128, height=28,cursor="hand2", border=0, command=lambda: self.cerrar_corte())

    def obtener_combo(self, event, index):
        try:
            if(index == 0):
                if(self.Boton_cerrar_corte.place_info() != {}):
                    self.Boton_cerrar_corte.place_forget()
                    self.label_fondo_a_entregar.place_forget()
                self.Boton_abrir_corte.place(x=330, y=260)
            else:
                if (self.Boton_abrir_corte.place_info() != {}):
                    self.Boton_abrir_corte.place_forget()
                self.Boton_cerrar_corte.place(x=330, y=260)
                self.label_fondo_a_entregar.place(x=90, y=148)
        except Exception as e:
            ms.showerror("Error!!!", e)


    def abrir_corte(self):
        try:
            
            self.numero_caja = (self.datos_numero_caja.get()).strip()
            self.nombre_usuario = (self.datos_nombre_usuario.get()).strip()
            self.fecha = (self.datos_fecha.get()).strip()
            self.hora = (self.datos_hora.get()).strip()
            self.efectivo_dado = (self.datos_fondo_recibido.get()).strip()
            if( self.numero_caja == "" or self.nombre_usuario == "" or self.fecha == "" or self.hora == "" or self.efectivo_dado == "" or 
            self.numero_caja == "Numero de caja" or self.nombre_usuario == "Nombre de usuario" or self.fecha == "DD/M/AAAA" or self.hora == "Hora" ):
                ms.showerror("Error!!!", "Debes llenar todos los campos para abrir el corte ")
            else:
                self.manejar_archivos_corte_caja.Insertar(self.numero_caja, self.nombre_usuario, self.fecha, self.hora, self.efectivo_dado)
                ms.showinfo("info", "El corte de apertura se ha registrado con exito")
                self.borrar_campos()
        except ValueError as e:
            ms.showerror("", "No se aceptan los caracteres especiales")
        except Exception as e:
            ms.showerror("", e)

    def cerrar_corte(self):
        try:
            

            self.numero_caja = (self.datos_numero_caja.get()).strip()
            self.nombre_usuario = (self.datos_nombre_usuario.get()).strip()
            self.fecha = (self.datos_fecha.get()).strip()
            self.hora = (self.datos_hora.get()).strip()
            self.efectivo_dado = (self.datos_fondo_recibido.get()).strip()
            if( self.numero_caja == "" or self.nombre_usuario == "" or self.fecha == "" or self.hora == "" or self.efectivo_dado == "" or 
            self.numero_caja == "Numero de caja" or self.nombre_usuario == "Nombre de usuario" or self.fecha == "DD/M/AAAA" or self.hora == "Hora" ):
                ms.showerror("Error!!!", "Debes llenar todos los campos para Cerrar el corte ")
            else:
                self.respuesta = self.manejar_archivos_corte_caja.Insertar_cierre_caja(self.numero_caja, self.nombre_usuario, self.fecha, self.hora, self.efectivo_dado)

                if(self.respuesta):
            
                    ms.showinfo("info", "El corte de cierre se ha registrado con exito")
                else: 
                    ms.showerror("Problema con corte de caja", "Necesita abrir primero el corte para cerrarlo")
                self.borrar_campos()
                    
        except ValueError as e:
            ms.showerror("", "No se aceptan los caracteres especiales")
        except Exception as e:
            ms.showerror("", e)

    def hora_correcta(self):
        if(len(str(self.tiempo.minute)) == 1):
            self.minutos = "0" + str(self.tiempo.minute)
        else:
            self.minutos = str(self.tiempo.minute)
        self.hora = str(self.tiempo.hour) + ":" + self.minutos

    def borrar_campos(self):
        self.entry_numero_caja.config(fg="grey")
        self.entry_nombre_usuario.config(fg="grey")
        self.entry_hora_apertura.config(fg="grey")
        self.datos_numero_caja.set("Numero de caja")
        self.datos_nombre_usuario.set("Nombre de usuario")
        self.datos_hora.set("Hora")
        self.datos_fondo_recibido.set("")

    def default(self, event, entry, texto_insertado):
        """ Coloca las indicaciones temporales en los entrys """
        self.informacion_entry = entry.get()
        if (self.informacion_entry == "Numero de caja" or self.informacion_entry == "Nombre de usuario" or self.informacion_entry == "DD/M/AAAA" or self.informacion_entry == "Hora"):
            entry.delete(0, tk.END)
            entry.config(fg="black")

        elif (self.informacion_entry == ""):

            entry.insert(0, texto_insertado)
            entry.config(fg="grey")


if __name__ == "__main__":
    raiz = tk.Tk()
    uno = Abrir_corte(raiz)
    uno.ventana_principal()
    raiz.mainloop()