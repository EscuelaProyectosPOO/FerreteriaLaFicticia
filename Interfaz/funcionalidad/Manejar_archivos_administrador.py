#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Manejar_archivos import Manejar_archivos
from interfaz_CRUD import CRUD

class Archivos_administrador(Manejar_archivos, CRUD):
    def __init__(self):
        Manejar_archivos()

    def Insertar(self, Nombre, Contra, Tipo):
        self.abrir_archivo('Base_empleados')
        self.usuario_nuevo = Nombre + '  ' + Contra + '  ' + Tipo
        self.identificador = Nombre
        self.band = self.insertar_linea_en_archivo_de_texto(self.usuario_nuevo, self.identificador)
        return self.band

    def Eliminar(self, Nombre):
        try:
            self.abrir_archivo('Base_empleados')
            self.linea_a_eliminar = Nombre
            self.band = self.eliminar_linea_en_archivo_texto(self.linea_a_eliminar)
            return self.band
        except:
            print 'Error al eliminar usuario'

    def Modificar(self, Nombre, Contra, Tipo):
        try:
            self.abrir_archivo('Base_empleados')
            self.usuario_editado = Nombre + '  ' + Contra + '  ' + Tipo
            self.identificador = Nombre
            self.band = self.modificar_linea_en_archivo_texto(self.usuario_editado, self.identificador)
            return self.band

        except:
            print 'Error al editar usuario'

    def Buscar(self, Nombre):
        try:
            self.abrir_archivo('Base_empleados')
            self.identificador = Nombre
            self.linea = self.buscar_linea_en_archivo_de_texto(self.identificador)
            return self.linea
        except:
            print 'Usuario no encontrado'

    def info(self):
        self.abrir_archivo("Base_empleados")
        self.informacion_del_archivo = self.archivo.readlines()
        self.archivo.close()
        return self.informacion_del_archivo

