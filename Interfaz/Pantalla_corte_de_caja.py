import Tkinter as tk
from funcionalidad.Evento_regresar import Cerrar_Ventanas

class Corte_caja(Cerrar_Ventanas):

    def __init__(self, pantalla_principal):
        self.pantalla_principal1 = pantalla_principal
        self.raiz = tk.Toplevel(self.pantalla_principal1)
        self.raiz.geometry('1170x564')
        self.raiz.title("Corte de caja")
        self.raiz.resizable(False, False)
        self.raiz.iconbitmap('../imagenes/logo.ico')
        self.imagen = tk.PhotoImage(file="../imagenes/fondo_sin_nada.GIF")
        self.fondo = tk.Label(self.raiz, image=self.imagen).place(x=0, y=0, relwidth=1, relheight=1)
        self.raiz.bind("<Destroy>",lambda event: self.volver_con_cerrado_ventana(event,self.pantalla_principal1))

    def ventana_principal(self):
        self.imagen_boton_regresar = tk.PhotoImage(file="../imagenes/boton_regresar.GIF")
        self.Boton_regresar = tk.Button(self.raiz, image=self.imagen_boton_regresar, width=120, height=65,cursor="hand2", border=0, command=lambda: self.volver(self.raiz, self.pantalla_principal1))
        self.Boton_regresar.grid(row=2, column=10, sticky='we')

        self.pantalla_principal1.withdraw()

    def volver(self, nombre_ventana_actual, nombre_ventana_anterior):
        nombre_ventana_anterior.deiconify()
        nombre_ventana_actual.destroy()

if __name__ == "__main__":
    raiz = tk.Tk()
    uno = Corte_caja(raiz)
    uno.ventana_principal()
    raiz.mainloop()