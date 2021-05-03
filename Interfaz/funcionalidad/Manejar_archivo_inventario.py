from Manejar_archivos import Manejar_archivos

class Manejar_archivo_inventario(Manejar_archivos):

    def traer_informacion_de_archivo_productos(self):
        """Trae informacion de la el archivo de texto de productos"""
        self.abrir_archivo("Base_Productos")
        self.__leer_archivo()
        return self.informacion_del_archivo

    
    def __leer_archivo(self):
        """Reescribe este metodo para que le entregue la informacion en lineas"""
        self.informacion_del_archivo = self.archivo.readlines()
        self.archivo.close()
    

