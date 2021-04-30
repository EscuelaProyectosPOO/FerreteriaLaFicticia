#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Manejar_archivos import Manejar_archivos


class Archivos_administrador(Manejar_archivos):
    def __init__(self):
        Manejar_archivos()

    def nuevo_usuario(self, Nombre, Contra, Tipo):
        try:
            self.abrir_archivo('Base_empleados')
            self.usuario_nuevo = Nombre + '  ' + Contra + '  ' + Tipo
            print self.usuario_nuevo
            self.identificador = Nombre
            print self.identificador
            self.band = self.insertar_linea_en_archivo_de_texto(self.usuario_nuevo, self.identificador)
            return self.band

        except:
            print 'Error al registrar usuario'

    def eliminar_usuario(self, Nombre):
        try:
            self.abrir_archivo('Base_empleados')
            self.linea_a_eliminar = Nombre
            print self.linea_a_eliminar
            self.band = self.eliminar_linea_en_archivo_texto(self.linea_a_eliminar)
            return self.band
        except:
            print 'Error al eliminar usuario'

    def editar_usuario(self, Nombre, Contra, Tipo):
        try:
            self.abrir_archivo('Base_empleados')
            self.usuario_editado = Nombre + '  ' + Contra + '  ' + Tipo
            print self.usuario_editado
            self.identificador = Nombre
            print self.identificador
            self.band = self.modificar_linea_en_archivo_texto(self.usuario_editado, self.identificador)
            return self.band

        except:
            print 'Error al editar usuario'

    def buscar(self, Nombre):
        try:
            self.abrir_archivo('Base_empleados')
            self.identificador = Nombre
            print self.identificador
            self.linea = self.buscar_linea_en_archivo_de_texto(self.identificador)
            print self.linea
            return self.linea
        except:
            print 'Usuario no encontrado'