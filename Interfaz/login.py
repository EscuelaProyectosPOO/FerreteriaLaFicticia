# -*- coding: utf-8 -*-
# #!/usr/bin/env python
from pantalla_inicio import Pantalla_de_inicio
from Tkinter import *

class Usuarios:
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title('Inicio de sesión')
        self.raiz.geometry('250x200')
        #self.raiz.config(bg='#f0ab3f')
        self.raiz.resizable(False, False)
        self.ventana()

        self.raiz.mainloop()

    def ventana(self):


        self.espacio = Label(self.raiz)
        self.espacio.grid(row=1)
        #self.espacio.config(bg='#f0ab3f')

        self.nombretext = StringVar()
        self.nombre = self.nombretext.get()
        #print self.nombre

        self.nl = Label(self.raiz, text='Usuario:', font=18)
        self.nl.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        #self.nl.config(bg='#f0ab3f')
        self.tn = Entry(self.raiz, textvariable=self.nombretext)
        self.tn.grid(row=2, column=1)

        self.cl = Label(self.raiz, text='Contraseña', font=18)
        self.cl.grid(row=3, column=0, sticky='e', padx=10, pady=5)
        self.tc = Entry(self.raiz)
        self.tc.grid(row=3, column=1)
        self.tc.config(show='*')

        
        self.be = Button(self.raiz, text='Entrar', font=18, command=lambda:comprueba())
        self.be.grid(row=4, column=0, pady=20)

        self.br = Button(self.raiz, text='Registrar usuario', font=18)
        self.br.grid(row=4, column=1, pady=20)

    def comprueba(self):
            print '...'
            self.nom = self.nombretext.get()
            if nom == 'Ana':
                print 'Bienvenida'
                uno = Pantalla_de_inicio().ventana_principal()
            elif nom == '' or nom ==' ':
                print 'vacío'
            else:
                print 'nombre incorrecto'
       




Inicio = Usuarios()
