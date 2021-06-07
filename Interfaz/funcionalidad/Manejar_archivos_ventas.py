#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from Manejar_archivos import Manejar_archivos
from interfaz_CRUD import CRUD

class Manejar_archivos_ventas(Manejar_archivos):

    def __init__(self):
        Manejar_archivos()


    def Insertar(self, fecha_de_registro, hora, codigo_producto, nombre_producto, precio_unitario, cantidad, total_por_piezas):
        """ Insertar venta """
        try:
            self.abrir_archivo("Base_Ventas")
            self.registro_nuevo = fecha_de_registro + "  " + hora + "  " + codigo_producto + "  " + nombre_producto + "  " + precio_unitario +  "  " + cantidad + "  " + total_por_piezas
            self.identificador_venta = " "
            self.bandera = self.insertar_linea_en_archivo_de_texto(self.registro_nuevo, self.identificador_venta)
        except Exception as e:

            print("Error en insertar venta", e)
    

    def traer_informacion(self):
        """Retorna informancio de ventas"""
        try:
            self.abrir_archivo("Base_Ventas")
            self.informacion_del_archivo = self.archivo.readlines()
            self.archivo.close()
            return self.informacion_del_archivo
        except Exception as e:
            print("Error en traer la informacion", type(e).__name__ )
        
    def buscar_linea_en_archivo_de_texto(self, identificador):
        """Busca lo que se le manda en el archivo """
        self.informacion_del_archivo = self.traer_informacion()
        self.__inicio = []
        try:
            for linea in self.informacion_del_archivo:
                self.lineas = linea.split("  ")
                
                for dato in self.lineas:
        
                    if(identificador == dato):
                        self.__inicio.append(linea)
                        break
        except Exception as e:
            print("buscar_linea_en_archivo_de_texto Manejar_archivos_venta", type(e).__name__ )

        return self.__inicio

    def buscar_venta_fecha_hora(self, fecha, hora):
        self.informacion_del_archivo = self.traer_informacion()
        self.__inicio = []
        try:
            for linea in self.informacion_del_archivo:
                self.lineas = linea.split("  ")
                if (fecha == self.lineas[0] and hora == self.lineas[1]):
                    self.__inicio.append(linea)
                    break
        except Exception as e:
            print("buscar_linea_en_archivo_de_texto Manejar_archivos_venta", type(e).__name__)

        return self.__inicio


if __name__ == "__main__":
    uno = Manejar_archivos_ventas()
    uno.buscar_venta_fecha_hora()


        


        

        



