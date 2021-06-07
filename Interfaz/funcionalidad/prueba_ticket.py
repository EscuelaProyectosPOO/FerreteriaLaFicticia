class NewFile:
    def __init__(self):
        print "Creando el archivo"
    def crear(self):
        file = open("Tickets.txt", "w")
        print "El archivo esta creado"
        file.close()

    def guardarDatos(self, producto, precio, cantidad):
        
        file = open("Tickets.txt", "a")
        titulo = 'Ferreteria la Ficticia' + '\n'
        file.write(titulo)
        encabezados = 'Producto  Precio  Cantidad  Total \n'
        file.write(encabezados)
        for i in list()
            total = precio * cantidad
            linea = ''
            linea = producto+"     "+str(precio)+"     "+str(cantidad)+ "       "+str(total)+ "\n"
            file.write(linea)
        file.close()

    def leer(self):
        with open("Tickets.txt", "r") as f:
            read_data=f.read()
            print read_data
            f.close()

archi=NewFile()
archi.crear()
archi.guardarDatos('paletas', 1.5, 5)
archi.leer()