#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter as tk
import ttk
import tkMessageBox as ms
from datetime import datetime
from funcionalidad.Manejar_archivos_productos import Manejar_archivos_productos
from funcionalidad.Evento_regresar import Cerrar_Ventanas
from funcionalidad.Manejar_archivos_ventas import Manejar_archivos_ventas
from funcionalidad.Exepciones import inexistencia_producto_tabla
from funcionalidad.Exepciones import Campos_vacios_en_ventas
from funcionalidad.Exepciones import Negativos
from funcionalidad.Exepciones import Registrar_venta
from pantalla_reporte_ventas import Pantalla_reporte_ventas


class Ventas(Cerrar_Ventanas):

    def __init__(self, pantalla_principal):
        self.pantalla_principal1 = pantalla_principal
        self.raiz = tk.Toplevel(self.pantalla_principal1)
        self.raiz.geometry('988x515')
        self.raiz.title("Ventas")
        self.raiz.resizable(False, False)
        self.raiz.iconbitmap('imagenes/logo.ico')
        self.imagen = tk.PhotoImage(file="imagenes/fondo_ventas.GIF")
        self.fondo = tk.Label(self.raiz, image=self.imagen).place(x=0, y=0, relwidth=1, relheight=1)
        #evento accionado cuando la ventana es destruida
        self.raiz.bind("<Destroy>",lambda event: self.volver_con_cerrado_ventana(event,self.pantalla_principal1))
        self.manejar_archivos_productos = Manejar_archivos_productos()
        self.manejar_archivos_venta = Manejar_archivos_ventas()
        
        self.Barra_menu_principal = tk.Menu(self.raiz)
        self.raiz.config(menu=self.Barra_menu_principal)
        self.tiempo = datetime.now()
        self.mostrar_total = tk.StringVar()
        self.mostrar_cambio = tk.StringVar()
        self.Codigo_producto = tk.StringVar()
        self.Cantidad = tk.StringVar()
        self.acumulador = 0
        
    def ventana_principal(self):
        """ Muestra todos los productos"""
        self.Barra_menu_principal.add_command(label="Reporte", command=lambda:self.reporte())

        self.Entry_Codigo_producto = tk.Entry(self.raiz, textvariable=self.Codigo_producto, width=25)
        self.Entry_Codigo_producto.place(x=35, y=61)

        self.Entry_Cantidad = tk.Entry(self.raiz, textvariable=self.Cantidad, width=10)
        self.Entry_Cantidad.place(x=270, y=61)

        self.Entry_Cantidad_recibida_cliente = tk.Entry(self.raiz, textvariable=self.mostrar_cambio, width=25)
        self.Entry_Cantidad_recibida_cliente.place(x=400, y=61)

        self.mostrar_total_a_pagar = tk.Label(self.raiz, textvariable= self.mostrar_total, font=("Verdana",24), width=10, bg="white")
        self.mostrar_total_a_pagar.place(x=30, y=180)

        self.mostrar_cambio_del_cliente = tk.Label(self.raiz, font=("Verdana",24), width=10, bg="white")
        self.mostrar_cambio_del_cliente.place(x=30, y=280)

        self.tabla = ttk.Treeview(self.raiz, show='headings', columns=("#1", "#2", "#3", "#4", "#5"), height=12)
        self.tabla.grid(row=1, column=9, pady=150, columnspan=2, padx=300)

        self.tabla.column("#1", width=150, anchor="center")
        self.tabla.column("#2", width=150, anchor="center")
        self.tabla.column("#3", width=100, anchor="center")
        self.tabla.column("#4", width=80, anchor="center")
        self.tabla.column("#5", width=100, anchor="center")
        

        self.tabla.heading("#1", text="Codigo de Producto")
        self.tabla.heading("#2", text="Nombre")
        self.tabla.heading("#3", text="Precio unitario")
        self.tabla.heading("#4", text="Cantidad")
        self.tabla.heading("#5", text="Total por piezas")
        

        self.scrollbar = tk.Scrollbar(self.raiz, orient="vertical", command=self.tabla.yview)
        self.scrollbar.grid(row=1, column=10, sticky='ns', pady=150)
        self.tabla.config(yscrollcommand=self.scrollbar.set)


        self.imagen_boton_agregar_venta = tk.PhotoImage(file="imagenes/agregar_venta_tabla.GIF")
        self.Boton_agregar_venta = tk.Button(self.raiz, image=self.imagen_boton_agregar_venta, width=71, height=28,cursor="hand2",border=0,  command=lambda:self.Agregar_item() )
        self.Boton_agregar_venta.place(x=590, y=55)

        self.imagen_boton_remover_venta = tk.PhotoImage(file="imagenes/remover_venta_tabla.GIF")
        self.Boton_remover_venta = tk.Button(self.raiz, image=self.imagen_boton_remover_venta, width=89, height=27,cursor="hand2",border=0,  command=lambda:self.Remover_item() )
        self.Boton_remover_venta.place(x=680, y=55)

        self.imagen_boton_calcular_cambio_venta = tk.PhotoImage(file="imagenes/calcular_cambio_ventas.GIF")
        self.Boton_calcular_cambio_venta = tk.Button(self.raiz, image=self.imagen_boton_calcular_cambio_venta, width=129, height=27,cursor="hand2",border=0,  command=lambda:self.calcular_cambio_cliente() )
        self.Boton_calcular_cambio_venta.place(x=790, y=55)

        self.imagen_boton_regresar = tk.PhotoImage(file="imagenes/boton_regresar.GIF")
        self.Boton_regresar = tk.Button(self.raiz, image=self.imagen_boton_regresar, width=120, height=65,cursor="hand2",border=0,  command=lambda:self.volver(self.raiz, self.pantalla_principal1) )
        self.Boton_regresar.place(x=2, y=430)

        self.imagen_boton_venta = tk.PhotoImage(file="imagenes/registrar_venta.GIF")
        self.Boton_venta = tk.Button(self.raiz, image=self.imagen_boton_venta, width=250, height=40,cursor="hand2",border=0,  command=lambda:self.Registrar_venta() )
        self.Boton_venta.place(x=670, y=430)

    
        self.pantalla_principal1.withdraw()

    def Agregar_item(self):
        """Agrega un producto a la tabla"""
        try:
            self.codigo_de_producto = (self.Codigo_producto.get()).strip() 
            self.cantidad_de_producto = (self.Cantidad.get()).strip()

            if(self.codigo_de_producto == "" or self.cantidad_de_producto == ""):
                raise Campos_vacios_en_ventas
            elif(int(self.cantidad_de_producto) < 0 ):
                raise Negativos
            elif(int(self.cantidad_de_producto) == 0):
                ms.showerror("Error!!!", "No podemos poner operar sobre la cantidad 0")
            else:
                self.cantidad_de_producto = int(self.cantidad_de_producto)
                self.datos_producto = self.manejar_archivos_productos.Buscar(self.codigo_de_producto)

                if(self.datos_producto == 0):
                    raise inexistencia_producto_tabla
                else: 
                    self.nombre = self.datos_producto[1] 
                    self.precio_unitario = float(self.datos_producto[2])
                    self.cantidad_por_precio = self.precio_unitario * self.cantidad_de_producto
                    self.cantidad_en_existencia = int(self.datos_producto[3])

                    if(self.cantidad_en_existencia >= self.cantidad_de_producto):
                        self.tabla.insert("",tk.END,text="", iid=self.codigo_de_producto, values=(self.codigo_de_producto, self.nombre, self.precio_unitario, self.cantidad_de_producto, self.cantidad_por_precio) )
                        self.acumulador += self.cantidad_por_precio
                        self.mostrar_total.set( "$" + str(self.acumulador))
                    else:
                        ms.showinfo("Informaci??n", "El producto " + self.nombre + " solo cuenta con " + str(self.cantidad_en_existencia) + " unidades")
        except Negativos as e:
            print Negativos, e

        except Campos_vacios_en_ventas as e:
            print Campos_vacios_en_ventas, e

        except inexistencia_producto_tabla as e:
            print  inexistencia_producto_tabla, e
        except ValueError as e:
            ms.showerror("Error!!!", "No se aceptan esos datos")
            print type(e).__name__
        except Exception as e :
            ms.showerror("Error!!!", "Ya has agregado este producto")
        finally:
            self.limpiar_campos()
            

    def Remover_item(self):
        """Elimina el producto con el ide indicado"""
        try:
            self.codigo_de_producto = (self.Codigo_producto.get()).strip() 
        
            self.lista_valores_item = self.tabla.item(self.codigo_de_producto)
            self.acumulador -= float(self.lista_valores_item["values"][4])
            self.mostrar_total.set("$" + str(self.acumulador))
            self.tabla.delete(self.codigo_de_producto)

        except IndexError as e:
            ms.showerror("Error!!!", "No podemos eliminar un elemento que no existe")
        except Exception as e :
            print  type(e).__name__
            ms.showerror("Error!!!", "Ya ha sido eliminado ese producto de la tabla")
        finally:
            self.limpiar_campos()

    def Registrar_venta(self):
        """Manda a la base de de datos la venta"""
        self.fecha_de_hoy = str(self.tiempo.day) + "/" + str(self.tiempo.month) + "/" + str(self.tiempo.year)
        if(len(str(self.tiempo.minute)) == 1):
            self.minutos = "0" + str(self.tiempo.minute)
        else:
            self.minutos = str(self.tiempo.minute)

        self.hora = str(self.tiempo.hour) + ":" + self.minutos
    
        self.lista = self.tabla.get_children()
        try:
            if(len(self.lista)==0 ):
                raise Registrar_venta
            else:
                for i in self.lista:
                    diccionario = self.tabla.item(i)
                    self.manejar_archivos_venta.Insertar(self.fecha_de_hoy, self.hora, str(diccionario["values"][0]), diccionario["values"][1], str(diccionario["values"][2]), str(diccionario["values"][3]), str(diccionario["values"][4]))
                    self.buscar_modificar_producto(str(diccionario["values"][0]), str(diccionario["values"][3]))
                    self.tabla.delete(i)
                ms.showinfo("Felicidades!!", "La venta se ha registrado con exito ")
                self.limpiar_campos()
        except IndexError:
            ms.showerror("Error!!", "salida de rango")

        except Registrar_venta as e:
            print  type(e).__name__
            
        self.limpiar_campos()
        self.acumulador = 0
        self.mostrar_total.set("$0.0")

    def limpiar_campos(self):
        self.Codigo_producto.set("")
        self.Cantidad.set("")
        self.mostrar_cambio.set("")
        self.mostrar_cambio_del_cliente.config(text="$0.0")

    def buscar_modificar_producto(self, codigo_producto, unidades_vendidas):
        self.datos_producto = self.manejar_archivos_productos.Buscar(codigo_producto)
        if(self.datos_producto == 0):
            ms.showerror("", "El producto que intentas agregar no existe")
        else: 
            self.nueva_cantidad = str(int(self.datos_producto[3]) - int(unidades_vendidas))
            self.manejar_archivos_productos.Modificar(self.datos_producto[0], self.datos_producto[1], self.datos_producto[2], self.nueva_cantidad, self.datos_producto[4], self.datos_producto[5], self.datos_producto[6])
            
    def calcular_cambio_cliente(self):
        try:
            self.vuelto = (self.mostrar_cambio.get()).strip()
            if(self.vuelto == ""):
                raise Campos_vacios_en_ventas
            elif(float(self.vuelto) <=0):
                raise Negativos
            elif(self.acumulador == 0):
                ms.showerror("", "Necesita tener una cantidad total a pagar primero")
            elif(float(self.vuelto)< self.acumulador):
                ms.showerror("", "El cliente debe dar una cantidad mayor o igual al total a pagar")
            else:
                self.vuelto =  str(float(self.vuelto) - self.acumulador)
                self.mostrar_cambio_del_cliente.config(text="$"+self.vuelto)

        except Negativos as e:
            print Negativos, e

        except Campos_vacios_en_ventas as e:
            print Campos_vacios_en_ventas, e
        except ValueError as e:
            ms.showerror("Error!!!", "No se aceptan esos datos")
            print type(e).__name__
        except Exception as e :
            ms.showerror("Error!!!", "Ya has agregado este producto")



    def volver(self, nombre_ventana_actual, nombre_ventana_anterior):
        nombre_ventana_anterior.deiconify()
        nombre_ventana_actual.destroy()

    def reporte(self):
        """Visualizar los datos de la Base_Ventas"""
        self.pantalla_reporte_ventas = Pantalla_reporte_ventas(self.raiz)
        self.pantalla_reporte_ventas.ventana_principal()

if __name__ == "__main__":
    raiz = tk.Tk()
    uno = Ventas(raiz)
    uno.ventana_principal()
    raiz.mainloop()
