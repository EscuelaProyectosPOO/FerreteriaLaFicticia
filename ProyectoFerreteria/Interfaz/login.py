# -*- coding: utf-8 -*-
# #!/usr/bin/env python
from Tkinter import  *
class Usuarios:
    def __init__(self):
        Raiz=Tk()
        Raiz.title('Inicio de sesión')
        Raiz.geometry('450x500')
        Raiz.config()
        Raiz.resizable(0,0)
        Msg=Label(Raiz, text='Bienvenido', font=('Arial Black', 20))
        Msg.grid(row=0, column=2)
        espacio=Label(Raiz)
        Nl=Label(Raiz, text='Nombre de usuario:' ,font=18)
        Nl.grid(row=2, column=0)
        Raiz.mainloop()

Inicio = Usuarios()
