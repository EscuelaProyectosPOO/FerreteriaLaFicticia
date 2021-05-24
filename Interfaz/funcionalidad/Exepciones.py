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



class inexistencia_producto_tabla(Exception):
    def __init__(self):
        print "Error en agregar producto inexistente en la tabla a la tabla de ventas"
        mensajes.showerror("", "el producto que intentas agregar no existe")


class Campos_vacios_en_ventas(Exception):
    def __init__(self):
        mensajes.showerror("", "Debes llenar todos los campos para podera gregar el producto")
        print "Error en la tabla por no llenar los campos"

 
class Negativos(Exception):
    def __init__(self):
        print 'Vacío'
        mensajes.showerror('ERROR', 'No puedes poner valores negativos')


class CodigoProducto(Exception):
    def __init__(self):
        mensajes.showerror("", "Para realizar la operacion debe que colocar el código del producto")