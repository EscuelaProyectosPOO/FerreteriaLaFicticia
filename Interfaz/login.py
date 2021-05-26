# -*- coding: utf-8 -*-
# #!/usr/bin/env python

#from pantalla_inicio import Pantalla_de_inicio
from Tkinter import *
import tkMessageBox as mensajes
from funcionalidad.Manejar_archivos_administrador import Archivos_administrador
from funcionalidad.Exepciones import Vacio
from funcionalidad.Evento_regresar import Cerrar_Ventanas


class Usuarios(Cerrar_Ventanas):
    def __init__(self, pantalla_principal):
        self.pantallaInicio = pantalla_principal
        self.raiz = Toplevel(self.pantallaInicio)
        self.raiz.title('Inicio de sesión')
        self.raiz.geometry('260x180')
        self.fondo = PhotoImage(file="login.gif")
        self.Lfondo = Label(self.raiz, image=self.fondo)
        self.Lfondo.place(x=0, y=0)
        self.raiz.resizable(False, False)
        self.respuesta = False
        self.raiz.bind("<Destroy>", lambda event: self.Evento_admin(event))

    def comprueba(self):
        print self.nombretext.get()
        print self.contra.get()
        
        try:
            if self.nombretext.get() == '' or self.contra.get() == '':
                raise Vacio
            else:
                comp = Archivos_administrador()
                self.linea_retornada = comp.Buscar(self.nombretext.get())
                if self.linea_retornada == 0:

                    mensajes.showerror('ERROR', 'Nombre incorrecto')
                else:
                    if self.linea_retornada[0] == self.nombretext.get() and self.linea_retornada[1] == self.contra.get():
                        if self.linea_retornada[2] == 1:
                            print 'admin'
                            self.respuesta = True
                        else:
                            print 'empleado'
                    else:
                        mensajes.showerror('ERROR', 'Contraseña incorrecta')
        except Vacio as v:
            print Vacio, v

    def ventana_principal(self):
        self.nombretext = StringVar()
        self.contra = StringVar()

        self.tn = Entry(self.raiz, textvariable=self.nombretext)
        self.tn.place(x=125, y=27)

        self.tc = Entry(self.raiz, textvariable=self.contra)
        self.tc.place(x=125, y=73)
        self.tc.config(show='*')

        self.fondo_entrar = PhotoImage(file='boton_entrar.gif')
        self.be = Button(self.raiz, image=self.fondo_entrar, command=lambda:self.comprueba())
        self.be.place(x=85, y=120)
        self.be.config(border=0)


    def Evento_admin(event,self):
        return self.respuesta

    def volver(self):
        pass

