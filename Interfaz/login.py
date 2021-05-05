# -*- coding: utf-8 -*-
# #!/usr/bin/env python

from pantalla_inicio import Pantalla_de_inicio
from Tkinter import *
import tkMessageBox as mensajes
from funcionalidad.Manejar_archivos_administrador import Archivos_administrador


class Usuarios:
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title('Inicio de sesión')
        self.raiz.geometry('260x180')
        self.fondo = PhotoImage(file="login.gif")
        self.Lfondo = Label(self.raiz, image=self.fondo)
        self.Lfondo.place(x=0, y=0)
        self.raiz.resizable(False, False)

        self.ventana()

        self.raiz.mainloop()
    def comprueba(self):
        comp = Archivos_administrador()
        self.linea_retornada = comp.buscar(self.nombretext.get())
        if self.linea_retornada[0] == self.nombretext.get() and self.linea_retornada[1] == self.contra.get():
            llamada = Pantalla_de_inicio()
        else:
            mensajes.showerror('ERROR', 'Usuario o contraseña incorrectos')
    def ventana(self):
        self.nombretext = StringVar()
        self.contra = StringVar()

        self.tn = Entry(self.raiz, textvariable=self.nombretext)
        self.tn.place(x=125, y=27)

        self.tc = Entry(self.raiz, textvariable=self.contra)
        self.tc.place(x=125, y=73)
        self.tc.config(show='*')

        self.be = Button(self.raiz, text='Entrar', font=18, command=lambda:self.comprueba())
        self.be.place(x=105, y=110)
        self.be.config(width=10, bg='#1953a7')




Inicio = Usuarios()
