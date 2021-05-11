#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from Manejar_archivos import Manejar_archivos
from interfaz_CRUD import CRUD

class Manejar_archivos_productos(Manejar_archivos, CRUD):

    def __init__(self):
        Manejar_archivos()

    def Insertar(self, codigo, nombre, precio, cantidad, marca, proveedor, fecha_de_entrega):
    
        try:
            self.abrir_archivo("Base_Productos")
            self.registro_nuevo = codigo + "  "+ nombre + "  "+ precio +  "  "+ cantidad + "  "+ marca + "  " + proveedor + "  " + fecha_de_entrega
            self.identificador_producto = codigo
            self.bandera = self.insertar_linea_en_archivo_de_texto(self.registro_nuevo, self.identificador_producto)
            return self.bandera
        except EOFError:
            print("Error linea 21 al abrir base_productos")
        except IOError:
            print("Error linea al abrir base_productos")

    def Buscar(self, codigo_producto):
        
        try:
            self.abrir_archivo("Base_Productos")
            self.identificador_producto = codigo_producto
            self.lista_datos_productos = self.buscar_linea_en_archivo_de_texto(self.identificador_producto)
            return self.lista_datos_productos
        except EOFError:
            print("Error linea al abrir base_productos")
        except IOError:
            print("Error linea al abrir base_productos")
        except:
            print("Error en buscar productos")

    def Modificar(self, codigo, nombre, precio, cantidad, marca, proveedor, fecha_de_entrega):
        
        try:
            self.abrir_archivo("Base_Productos")
            self.registro_nuevo = codigo + "  "+ nombre + "  "+ precio +  "  "+ cantidad + "  "+ marca + "  " + proveedor + "  " + fecha_de_entrega
            self.identificador_producto = codigo
            self.bandera = self.modificar_linea_en_archivo_texto(self.registro_nuevo, self.identificador_producto)
            return self.bandera
        except EOFError:
            print("Error linea al abrir base_productos")
        except IOError:
            print("Error linea al abrir base_productos")
        except:
            print("Error en modificar productos")

    def Eliminar(self, codigo_producto):

        try:
            self.abrir_archivo("Base_Productos")
            self.identificador_producto = codigo_producto
            self.bandera = self.eliminar_linea_en_archivo_texto(self.identificador_producto)
            return self.bandera
        except EOFError:
            print("Error linea al abrir base_productos")
        except IOError:
            print("Error linea al abrir base_productos")
        except:
            print("Error en eliminar productos")




