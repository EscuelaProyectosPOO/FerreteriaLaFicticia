# -*- coding: utf-8 -*-
# #!/usr/bin/env python

from Tkinter import *


class Usuarios:
    def __init__(self):

        raiz = Tk()
        raiz.title('Inicio de sesión')
        raiz.geometry('250x200')
        raiz.config(bg='#f0ab3f')
        raiz.resizable(False, False)
        espacio = Label(raiz)
        espacio.grid(row=1)
        espacio.config(bg='#f0ab3f')

        nombretext = StringVar()
        nombre = nombretext.get()
        print nombre

        nl = Label(raiz, text='Usuario:', font=18)
        nl.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        nl.config(bg='#f0ab3f')
        tn = Entry(raiz, textvariable=nombretext)
        tn.grid(row=2, column=1)

        cl = Label(raiz, text='Contraseña', font=18)
        cl.grid(row=3, column=0, sticky='e', padx=10, pady=5)
        cl.config(bg='#f0ab3f')
        tc = Entry(raiz)
        tc.grid(row=3, column=1)
        tc.config(show='*')

        be = Button(raiz, text='Entrar', font=18, command=comprueba(nombre))
        be.grid(row=4, column=0, pady=20)
        be.config(justify=LEFT, bg='#172caa')

        br = Button(raiz, text='Registrar usuario', font=18)
        br.grid(row=4, column=1, pady=20)
        br.config(justify=LEFT, bg='#172caa')
        raiz.mainloop()


def comprueba(nom):
    if nom == 'Ana':
        print 'Hola'
    elif nom == '':
        print 'vacío'
    else:
        print 'Nombre incorrecto'


Inicio = Usuarios()
