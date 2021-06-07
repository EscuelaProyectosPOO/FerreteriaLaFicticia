#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter as tk
import ttk
from funcionalidad.Evento_regresar import Cerrar_Ventanas
from Abrir_corte_caja import Abrir_corte

class Corte_caja(Cerrar_Ventanas):

    def __init__(self, pantalla_principal):
        self.pantalla_principal1 = pantalla_principal
        self.raiz = tk.Toplevel(self.pantalla_principal1)
        self.raiz.geometry('580x510')
        self.raiz.title("Corte de caja")
        self.raiz.resizable(False, False)
        self.raiz.iconbitmap('../imagenes/logo.ico')
        self.imagen = tk.PhotoImage(file="../imagenes/Registrar_corte_caja_fondo.GIF")
        self.fondo = tk.Label(self.raiz, image=self.imagen).place(x=0, y=0, relwidth=1, relheight=1)
        self.Barra_menu_principal = tk.Menu(self.raiz)
        self.raiz.config(menu=self.Barra_menu_principal)
        self.raiz.bind("<Destroy>",lambda event: self.volver_con_cerrado_ventana(event,self.pantalla_principal1))

    def ventana_principal(self):
        self.Barra_menu_principal.add_command(label="Abrir o cerrar corte", command=lambda:self.abrir_cerrar_corte())


        self.imagen_boton_regresar = tk.PhotoImage(file="../imagenes/boton_regresar.GIF")
        self.Boton_regresar = tk.Button(self.raiz, image=self.imagen_boton_regresar, width=120, height=65,cursor="hand2", border=0, command=lambda: self.volver(self.raiz, self.pantalla_principal1))
        self.Boton_regresar.place(x=0, y=430)

        self.imagen_boton_registrar_corte = tk.PhotoImage(file="../imagenes/registra_corte_caja.GIF")
        self.Boton_registrar_corte = tk.Button(self.raiz, image=self.imagen_boton_registrar_corte, width=230, height=44,
                                        cursor="hand2", border=0,
                                        command=lambda: self.volver(self.raiz, self.pantalla_principal1))
        #self.Boton_registrar_corte.place(x=300, y=420)

        self.entry_numero_caja = tk.Entry(self.raiz, fg="grey", text="Numero de caja", state="disabled")
        self.entry_numero_caja.place(x=125, y = 10)

        self.entry_fecha_apertura = tk.Entry(self.raiz, fg="grey",  state="disabled")
        self.entry_fecha_apertura.place(x=125, y=43)

        self.entry_hora_apertura = tk.Entry(self.raiz, width=10, fg="grey", state="disabled")
        self.entry_hora_apertura.place(x=275, y=43)


        self.entry_fecha_cierre = tk.Entry(self.raiz, fg="grey", state="disabled" )
        self.entry_fecha_cierre.place(x=125, y=76)


        self.entry_hora_cierre = tk.Entry(self.raiz, width=10, fg="grey", state="disabled")
        self.entry_hora_cierre.place(x=275, y=76)


        self.tabla = ttk.Treeview(self.raiz, show='headings', columns=("#1", "#2", "#3"), height=10)
        self.tabla.grid(row=1, column=9, pady=170, columnspan=3, padx=100)

        self.tabla.column("#1", width=150, anchor="center")
        self.tabla.column("#2", width=150, anchor="center")
        self.tabla.column("#3", width=110, anchor="center")


        self.tabla.heading("#1", text="Descripcion")
        self.tabla.heading("#2", text="Importe")
        self.tabla.heading("#3", text="Divisa")

        self.scrollbar = tk.Scrollbar(self.raiz, orient="vertical", command=self.tabla.yview)
        self.scrollbar.grid(row=1, column=11, sticky='ns', pady=170)
        self.tabla.config(yscrollcommand=self.scrollbar.set)

        self.pantalla_principal1.withdraw()

    def volver(self, nombre_ventana_actual, nombre_ventana_anterior):
        nombre_ventana_anterior.deiconify()
        nombre_ventana_actual.destroy()

    def abrir_cerrar_corte(self):
        self.abrir_corte_caja_objeto = Abrir_corte(self.raiz)
        self.abrir_corte_caja_objeto.ventana_principal()


if __name__ == "__main__":
    raiz = tk.Tk()
    uno = Corte_caja(raiz)
    uno.ventana_principal()
    raiz.mainloop()