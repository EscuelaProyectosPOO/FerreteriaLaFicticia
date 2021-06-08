#!/usr/bin/env python
# -*- coding: utf-8 -*-
from io import open
import  os
from Manejar_archivos import Manejar_archivos
from interfaz_CRUD import CRUD


class Manejar_archivos_corte_caja(Manejar_archivos):

    def __init__(self):
        Manejar_archivos()

    def Insertar(self, numero_caja, nombre_quien_registra, fecha, hora, fondo_recibido):
        """ Insertar venta """
        try:
            self.abrir_archivo("Base_Corte_caja")
            self.registro_nuevo = "Apertura" + "  " + numero_caja + "  " + nombre_quien_registra + "  " + fecha + "  " + hora + "  " + fondo_recibido
            self.identificador_producto = " "
            self.bandera = self.insertar_linea_en_archivo_de_texto(self.registro_nuevo, self.identificador_producto)
            return self.bandera
        except Exception as e:

            print("Error en insertar corte", e)
    def d(self):
        self.n = self.archivo.readlines()
        print self.n



if __name__ == "__main__":
    uno = Manejar_archivos_corte_caja()
    uno.Insertar("1", "Estfa", "2/2/2021", "12:23", "400")