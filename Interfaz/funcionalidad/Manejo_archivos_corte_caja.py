#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
import re
import time
import tkMessageBox as ms
from Manejar_archivos import Manejar_archivos
from interfaz_CRUD import CRUD



class Manejar_archivos_corte_caja(Manejar_archivos):

    def __init__(self):
        Manejar_archivos()

    def Insertar(self, numero_caja, nombre_quien_registra, fecha, hora, fondo_recibido):
        """ Insertar apertura de caja"""
        try:
            self.respuesta = self.verificar_si_ya_ha_sido_registrado_la_apertura(numero_caja, fecha)
            if(self.respuesta):
                ms.showinfo("Ups!!", "Ya se ha habierto el corte en esta caja")
            else:    
                self.abrir_archivo("Base_Corte_caja")
                self.registro_nuevo = "Apertura" + "  " + numero_caja + "  " + nombre_quien_registra + "  " + fecha + "  " + hora + "  " + fondo_recibido
                self.identificador_producto = " "
                self.bandera = self.insertar_linea_en_archivo_de_texto(self.registro_nuevo, self.identificador_producto)
                ms.showinfo("info", "El corte de apertura se ha registrado con exito")
        except Exception as e:
            print("Error en insertar corte", e)

    def traer_informacion(self):
        """Retorna informancio de ventas"""
        try:
            self.abrir_archivo("Base_Corte_caja")
            self.informacion_del_archivo = self.archivo.read()
            self.archivo.close()
            return self.informacion_del_archivo
        except Exception as e:
            print("Error en traer la informacion", type(e).__name__ )

    def Insertar_cierre_caja(self,  numero_caja, nombre_quien_registra, fecha, hora, fondo_recibido):
        
        try:
            self.hora_cierre = self.pasar_hora_minutos_enteros_correcto(hora)
            self.informacion_del_archivo = self.traer_informacion()
            self.informacion_del_archivo_lista = (self.informacion_del_archivo).splitlines()

            self.informacion_de_apertura = ""
            for linea in self.informacion_del_archivo_lista:

                self.lista = linea.split("  ")

                if(len(self.lista) == 6):
                    self.hora_apertura = self.pasar_hora_minutos_enteros_correcto(self.lista[4])
                    if(self.lista[0] == "Apertura" and self.lista[1] == numero_caja and  self.lista[3] == fecha and self.hora_apertura < self.hora_cierre ):
                        self.informacion_de_apertura = linea
                        break
            if(self.informacion_de_apertura == ""):
                return False
            else:

                self.linea_nueva_insertar =self.informacion_de_apertura + "  " +"Cierre" + "  " + numero_caja + "  " + nombre_quien_registra + "  " + fecha + "  " + hora + "  " + fondo_recibido
                
                self.informacion_del_archivo_nueva = self.informacion_del_archivo.replace(self.informacion_de_apertura, self.linea_nueva_insertar)
                
                self.actualizar_archivo_texto(self.informacion_del_archivo_nueva)
                
                return True

        except Exception as e:
            print("Error en agregar cierre de corte", e)

    def verificar_si_ya_ha_sido_registrado_la_apertura(self, numero_caja, fecha):
        try:
            
            self.informacion_del_archivo = self.traer_informacion()
            self.informacion_del_archivo_lista = (self.informacion_del_archivo).splitlines()

            self.existe = False

            for linea in self.informacion_del_archivo_lista:

                self.lista = linea.split("  ")

                if(len(self.lista) == 6):
                    
                    if(self.lista[0] == "Apertura" and self.lista[1] == numero_caja and  self.lista[3] == fecha ):
                        self.existe = True
                        break
            return self.existe
            
        except Exception as e:
            print("Error en agregar cierre de corte", e)


    def pasar_hora_minutos_enteros_correcto(self, hora):
        if(re.search(":0", hora)):
            self.hora = int(hora[:re.search(":0",hora).start()])
            self.minutos = int(hora[re.search(":0",hora).end():])
        else:
            self.hora = int(hora[:re.search(":",hora).start()])
            self.minutos = int(hora[re.search(":",hora).end():])

        self.hora_buena = datetime.time(self.hora, self.minutos, 0)
        return self.hora_buena


if __name__ == "__main__":
    uno = Manejar_archivos_corte_caja()
    uno.Insertar_cierre_caja( "3",  "Estefania",  "8/6/2021",  "20:39",  "200")
    
    