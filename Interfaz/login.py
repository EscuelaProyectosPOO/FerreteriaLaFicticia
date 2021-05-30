# -*- coding: utf-8 -*-
# #!/usr/bin/env python

from pantalla_inicio import Pantalla_de_inicio
from Tkinter import *
import tkMessageBox as mensajes
from funcionalidad.Manejar_archivos_administrador import Archivos_administrador
from funcionalidad.Exepciones import Vacio
import os


class Usuarios:
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title('Inicio de sesión')
        self.raiz.geometry('330x280')
        self.raiz.iconbitmap('logo.ico')
        self.fondo = PhotoImage(file="login.gif")
        self.Lfondo = Label(self.raiz, image=self.fondo)
        self.Lfondo.place(x=-1, y=-1)
        self.raiz.resizable(False, False)
        self.nombretext = StringVar()
        self.contra = StringVar()
        self.respuesta = False
        self.ventana_principal()
        self.raiz.mainloop()

    def comprueba(self):
        try:
            if self.nombretext.get() == 'Usuario' or self.contra.get() == 'Clave':
                raise Vacio
            else:
                if os.path.isfile('Base_empleados') == False:
                    crear = Archivos_administrador()
                    crear.Insertar('Admin', 'qwerty', '1')
                comp = Archivos_administrador()
                self.linea_retornada = comp.Buscar(self.nombretext.get())
            if self.linea_retornada == 0:
                mensajes.showerror('ERROR', 'Este usuario no existe')

            else:
                if self.linea_retornada[0] == self.nombretext.get() and self.linea_retornada[1] == self.contra.get():
                    if self.linea_retornada[2] == '1':
                        self.respuesta = True
                        llamada = Pantalla_de_inicio(self.raiz, self.respuesta)
                        self.nombretext.set('')
                        self.tn.config(fg='grey')
                        self.contra.set('')
                        self.tn.insert(0, 'Usuario')
                        self.tn.bind("<FocusIn>", lambda event: self.default(event, self.tn, "Usuario"))
                        self.tn.bind("<FocusOut>", lambda event: self.default(event, self.tn, "Usuario"))


                    else:
                        self.respuesta = False
                        llamada = Pantalla_de_inicio(self.raiz, self.respuesta)
                        self.nombretext.set('')
                        self.tn.config(fg='grey')
                        self.contra.set('')
                        self.tn.insert(0, 'Usuario')
                        self.tn.bind("<FocusIn>", lambda event: self.default(event, self.tn, "Usuario"))
                        self.tn.bind("<FocusOut>", lambda event: self.default(event, self.tn, "Usuario"))

                else:
                    mensajes.showerror('ERROR', 'Contraseña incorrecta')
        except Vacio as v:
            print Vacio, v
        except Exception as e:
            print type(e).__name__, e

    def ventana_principal(self):
        self.tn = Entry(self.raiz, textvariable=self.nombretext,  fg = 'grey')
        self.tn.config(font=35)
        self.tn.place(x=45, y=80, width=250, height=30)
        self.tn.insert(0, 'Usuario')
        self.tn.bind("<FocusIn>", lambda event: self.default(event,self.tn, "Usuario"))
        self.tn.bind("<FocusOut>", lambda event: self.default(event,self.tn, "Usuario"))

        self.tc = Entry(self.raiz, textvariable=self.contra, fg = 'grey')
        self.tc.config(font=35)
        self.tc.place(x=45, y=135,  width=250, height=30)
        self.tc.insert(0, 'Clave')
        self.tc.bind("<FocusIn>", lambda event: self.default(event, self.tc, "Clave"))
        self.tc.bind("<FocusOut>", lambda event: self.default(event, self.tc, "Clave"))


        self.fondo_entrar = PhotoImage(file='boton_entrar.gif')
        self.be = Button(self.raiz, image=self.fondo_entrar, command=lambda:self.comprueba())
        self.be.place(x=100, y=195)
        self.be.config(border=0)


    def Evento_admin(event,self):
        return self.respuesta

    def default(self, event, entry, texto_insertado):
        self.informacion_entry = entry.get()
        if(self.informacion_entry == "Usuario"):
            entry.delete(0, END)
            entry.config(fg="black")
        elif (self.informacion_entry == 'Clave'):
            entry.delete(0, END)
            entry.config(fg="black", show='*')

        elif(self.informacion_entry == ""):
            entry.insert(0,texto_insertado)
            entry.config(fg="grey")

if __name__ == "__main__":
    uno = Usuarios()