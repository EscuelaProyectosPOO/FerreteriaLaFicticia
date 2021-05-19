# -*- coding: utf-8 -*-
# #!/usr/bin/env python
from Tkinter import *
import tkMessageBox as mensajes


class Numeros(Exception):
    def __init__(self):
        print 'El precio debe ser un número'
        mensajes.showerror('ERROR', 'Este campo solo debe tener valores numéricos')


class Vacio(Exception):
    def __init__(self):
        print 'Vacío'
        mensajes.showerror('ERROR', 'No deben quedar campos vacíos')