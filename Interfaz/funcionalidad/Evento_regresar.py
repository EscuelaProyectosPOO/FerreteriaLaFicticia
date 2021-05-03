import abc
from abc import ABCMeta

class Cerrar_Ventanas(object):

    __metaclass__ = ABCMeta

    def volver_con_cerrado_ventana(self, event, nombre_ventana_anterior):
        nombre_ventana_anterior.deiconify()


    @abc.abstractmethod
    def volver(self, nombre_ventana_actual, nombre_ventana_anterior):
        pass