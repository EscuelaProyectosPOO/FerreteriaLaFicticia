#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from Manejar_archivos import Manejar_archivos
from interfaz_CRUD import CRUD

class Manejar_archivos_ventas(Manejar_archivos):

    def __init__(self):
        Manejar_archivos()


    def Insertar(self, fecha_de_registro, codigo_producto, nombre_producto, precio_unitario, cantidad, total_por_piezas):
    
        try:
            self.abrir_archivo("Base_Ventas")
            self.registro_nuevo = fecha_de_registro + "  " + codigo_producto + "  " + nombre_producto + "  " + precio_unitario +  "  " + cantidad + "  " + total_por_piezas
            self.identificador_venta = " "
            self.bandera = self.insertar_linea_en_archivo_de_texto(self.registro_nuevo, self.identificador_venta)
        except:
            print("Error en insertar venta")
        
    def Modificar(self, informacion_nueva):
        
        self.__direccion_archivo = os.getcwd() +"/Base_Ventas.txt"
        os.remove(self.__direccion_archivo)
        self.abrir_archivo("Base_Ventas")
        self.archivo.write(informacion_nueva)


    def traer_informacion(self):
        try:
            self.abrir_archivo("Base_Ventas")
            self.informacion_del_archivo = self.archivo.readlines()
            self.archivo.close()
            return self.informacion_del_archivo
        except:
            print("Error en traer la informacion")
        

    
   

        


        

        



