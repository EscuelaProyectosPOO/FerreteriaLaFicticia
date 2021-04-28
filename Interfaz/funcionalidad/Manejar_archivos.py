#from __future__ import unicode_literals#para resolver el problema de unicode, aca lo necesita unicode no str, si no se puede casteamos con nuevostring =unicode(string)
from io import open #para manejar archivos
import re #para usar expresiones reguares
import os #borrar archivos




#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Manejar_archivos():
    def __init__(self):
        self.__linea_antigua = ""

    def abrir_archivo(self, nombre_del_archivo):
        """Abre el archivo """
        self.__nombre_archivo_de_texto = nombre_del_archivo 
        try:
            self.archivo = open(self.__nombre_archivo_de_texto + ".txt", "r+")
        except:
            self.archivo = open(self.__nombre_archivo_de_texto + ".txt", "w")
            self.archivo.close()
            self.archivo = open(self.__nombre_archivo_de_texto + ".txt", "r+")
        
       

    def __leer_archivo(self):
        """lee el archivo de texto """
        self.informacion_del_archivo = self.archivo.read()
       

    def __escribir_en_archivo(self, linea_a_escribir):
        """Escribe en el archivo """
        self.archivo.writelines(linea_a_escribir)
       
        

    def __cerrar_archivo(self):
        """cierra el archivo """
        self.archivo.close()

    def __eliminar_archivo_de_texto(self):
        """elimina el archivo de texto """
        self.__direccion_archivo = os.getcwd() +"/" + self.__nombre_archivo_de_texto + ".txt"
        os.remove(self.__direccion_archivo)
    
    def insertar_linea_en_archivo_de_texto(self, linea_a_insertar, identificador):
        """incerta la linea mandada en el archivo"""
        self.__leer_devolver_linea_a_antigua(identificador)
        if(self.__existe == False):
            if(os.stat(self.__nombre_archivo_de_texto + ".txt").st_size == 0):#para saber si esta vacio el documento
                self.__linea_a_insertar = unicode(linea_a_insertar)
            else:
                self.__linea_a_insertar = unicode("\n"+ linea_a_insertar)#por alguna razon me pide unicode
            self.__escribir_en_archivo(self.__linea_a_insertar)

            self.__cerrar_archivo()
            return True
        else:
            return False
        self.__cerrar_archivo()
            
            
        
    def buscar_linea_en_archivo_de_texto(self, identificador):
        """Busca lo que se le manda en el archivo """
        self.__leer_devolver_linea_a_antigua(identificador)
        self.__cerrar_archivo()
        if(self.__existe):
            self.__inicio = []

            for dato in self.__valoresdei:
                
                self.__inicio += [dato]

            
            return self.__inicio
        else:
            return 0
        

        

          
    def modificar_linea_en_archivo_texto(self, linea_modificada_a_insertar, identificador):
        """modifica la linea anterior, remplazandola con la nueva linea en el archivo """
        self.__linea_modificada_a_insertar = unicode(linea_modificada_a_insertar)
        self.__leer_devolver_linea_a_antigua(identificador)
        self.__cerrar_archivo()
        if(self.__existe):
            self.informacion_del_archivo = self.informacion_del_archivo.replace(self.__linea_antigua, self.__linea_modificada_a_insertar )
            self.__actualizar_archivo_texto(self.informacion_del_archivo)
            return True
        else:
            return False


    def eliminar_linea_en_archivo_texto(self, identificador):
        """borra la linea en el archivo, basandose en un identificador """
        self.__leer_devolver_linea_a_antigua(identificador)
        self.__cerrar_archivo()
        if(self.__existe):
            self.__posicion_cadena_a_eliminar = re.search(self.__linea_antigua, self.informacion_del_archivo)
            self.informacion_del_archivo = self.informacion_del_archivo[:self.__posicion_cadena_a_eliminar.start()] + self.informacion_del_archivo[(self.__posicion_cadena_a_eliminar.end()+1):]
            self.__actualizar_archivo_texto(self.informacion_del_archivo)
            return True
        else:
            return False 
        
        

    def __leer_devolver_linea_a_antigua(self, identificador):
        """busca con ayuda del identificador la linea que le corresponde
            para regresarla, con el objetivo de utilizarla en el futuro"""
        self.__leer_archivo()

        self.__existe = False
        self.__banderaFor = False
        
        self.informacion_del_archivo_dividida = self.informacion_del_archivo.splitlines()

        for linea in self.informacion_del_archivo_dividida:
            self.__valoresdei = linea.split("  ")
            for lista_de_linea in self.__valoresdei:
                if(lista_de_linea == identificador):
                    self.__linea_antigua = linea
                    self.__existe = True
                    self.__banderaFor = True
                    break
            if(self.__banderaFor):
                break




    def __actualizar_archivo_texto(self, informacion_sin_linea):
        """se elimina el anterior y se crea uno totalmente nuevo con el mismo nombre
            que el archivo eliminado anteriormente"""
        self.__eliminar_archivo_de_texto()
        self.abrir_archivo(self.__nombre_archivo_de_texto)
        self.__escribir_en_archivo(informacion_sin_linea)
        self.__cerrar_archivo()




#-----------------------------------------------------ejemplo de uso de los metodos de la clase---------------------------------------------------------
#uno = Manejar_archivos()
#uno.abrir_archivo("Base_Productos")
#print uno.insertar_linea_en_archivo_de_texto("Maria Juana Hernandez Sanchez", "0")
#lista = uno.buscar_linea_en_archivo_de_texto("0")
#print(lista)

#print(uno.modificar_linea_en_archivo_texto("A chuchita la bolsearon Juana Hernandez Sanchez  1shsuh8u37gw7w7d", "Maria Juana Hernandez Sanchez"))
#print(uno.eliminar_linea_en_archivo_texto("A chuchita la bolsearon Juana Hernandez Sanchez"))












