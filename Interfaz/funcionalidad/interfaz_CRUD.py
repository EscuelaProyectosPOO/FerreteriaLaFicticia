import abc
from abc import ABCMeta

class CRUD(object):
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def Insertar(self):
        pass

    @abc.abstractmethod
    def Buscar(self):
        pass

    @abc.abstractmethod
    def Modificar(self):
        pass

    @abc.abstractmethod
    def Eliminar(self):
        pass