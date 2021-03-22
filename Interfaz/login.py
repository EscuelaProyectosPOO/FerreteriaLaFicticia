# -*- coding: utf-8 -*-
# #!/usr/bin/env python

from pantalla_inicio import Pantalla_de_inicio
from Tkinter import *
import tkMessageBox as ms


class Usuarios:
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title('Inicio de sesión')
        self.raiz.geometry('250x180')
        self.fondo = PhotoImage(file="login.gif")
        self.Lfondo = Label(self.raiz, image=self.fondo)
        self.Lfondo.place(x=0, y=0)
        self.raiz.resizable(False, False)

        self.ventana()

        self.raiz.mainloop()

    def ventana(self):
        self.nombretext = StringVar()
        self.nombre = self.nombretext.get()
        self.contra = StringVar()

        self.tn = Entry(self.raiz, textvariable=self.nombretext)
        self.tn.place(x=95, y=27)

        self.tc = Entry(self.raiz, textvariable=self.contra)
        self.tc.place(x=95, y=60)
        self.tc.config(show='*')

        def comprueba():
            print '...'
            nom = self.nombretext.get()
            cont = self.contra.get()
            if nom == 'Ana' and cont == 'Sistemas':
                print 'Bienvenida'
                llamas = Pantalla_de_inicio()
                llamas.ventana_principal()
                print cont
            elif nom == '' and nom == ' ':
                print 'vacío'
            else:
                print 'nombre incorrecto'
                print cont
                ms.showinfo('Error', 'Nombre de usuario o Contraseña incorrectos')
        self.be = Button(self.raiz, text='Entrar', font=18, command=lambda:comprueba())
        self.be.place(x=105, y=110)
        self.be.config(width=10, bg='#1953a7')




Inicio = Usuarios()
