# -*- coding: utf-8 -*-
# #!/usr/bin/env python
from Manejar_archivos import Manejar_archivos
from interfaz_CRUD import CRUD


class Archivos_proveedores(Manejar_archivos, CRUD):
    def __init__(self):
        Manejar_archivos()

    def Insertar(self, Nombre, Direccion, Productos, precio):
        try:
            self.abrir_archivo('Base_proveedores')
            self.proveedor_nuevo = Nombre + '  ' +Direccion + '  ' + Productos + '  ' + precio
            print self.proveedor_nuevo
            self.identificador = Nombre
            print self.identificador
            self.band = self.insertar_linea_en_archivo_de_texto(self.proveedor_nuevo, self.identificador)
            return self.band

        except:
            print 'Error al registrar usuario'

    def Modificar(self, Nombre, Direccion, Productos, precio):
        try:
            self.abrir_archivo('Base_proveedores')
            self.proveedor_editado = Nombre + '  ' +Direccion + '  ' + Productos + '  ' + precio
            print self.proveedor_editado
            self.identificador = Nombre
            print self.identificador
            self.band = self.modificar_linea_en_archivo_texto(self.proveedor_editado, self.identificador)
            return self.band

        except:
            print 'Error al editar proveedor'

    def Eliminar(self, Nombre):
        try:
            self.abrir_archivo('Base_proveedores')
            self.identificador = Nombre
            print self.identificador
            self.band = self.eliminar_linea_en_archivo_texto(self.identificador)
            return self.band

        except:
            print 'Error al eliminar usuario'

    def Buscar(self, Nombre):
        try:
            self.abrir_archivo('Base_proveedores')
            self.identificador = Nombre
            print self.identificador
            self.band = self.buscar_linea_en_archivo_de_texto(self.identificador)
            return self.band

        except:
            print 'Error al encontrar proveedor'

    def info(self):
        try:
            self.abrir_archivo("Base_proveedores")
            self.informacion_del_archivo = self.archivo.readlines()
            self.archivo.close()
            return self.informacion_del_archivo
        except Exception as e:
            print("Error en traer la informacion", type(e).__name__)




