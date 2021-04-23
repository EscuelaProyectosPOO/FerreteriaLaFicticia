#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from Manejar_archivos import Manejar_archivos

class Manejar_archivos_productos(Manejar_archivos):

    def __init__(self):
        Manejar_archivos()

    def insertar_nuevo_producto(self, codigo, nombre, precio, tipo_de_producto, cantidad, marca):
    
        try:
            self.abrir_archivo("Base_Productos")
            self.registro_nuevo = codigo + "  "+ nombre + "  "+ precio + "  " + tipo_de_producto + "  "+ cantidad + "  "+ marca 
            self.identificador_producto = codigo
            self.bandera = self.insertar_linea_en_archivo_de_texto(self.registro_nuevo, self.identificador_producto)
            return self.bandera
        except:
            print("Error en insertar producto")

    def buscar_producto(self, codigo_producto):
        
        try:
            self.abrir_archivo("Base_Productos")
            self.identificador_producto = codigo_producto
            self.lista_datos_productos = self.buscar_linea_en_archivo_de_texto(self.identificador_producto)
            return self.lista_datos_productos
        except:
            print("Error en buscar productos")

    def modificar_producto(self, codigo, nombre, precio, tipo_de_producto, cantidad, marca):
        
        try:
            self.abrir_archivo("Base_Productos")
            self.registro_nuevo = codigo + "  "+ nombre + "  "+ precio + "  " + tipo_de_producto + "  "+ cantidad + "  "+ marca
            self.identificador_producto = codigo
            self.bandera = self.modificar_linea_en_archivo_texto(self.registro_nuevo, self.identificador_producto)
            return self.bandera
        except:
            print("Error en modificar productos")

    def eliminar_producto(self, codigo_producto):

        try:
            self.abrir_archivo("Base_Productos")
            self.identificador_producto = codigo_producto
            self.bandera = self.eliminar_linea_en_archivo_texto(self.identificador_producto)
            return self.bandera

        except:
            print("Error en eliminar productos")




