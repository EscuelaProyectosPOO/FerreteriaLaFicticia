#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

class Pantalla_administrador:

    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry('1169x563')
        self.raiz.title("tk")
        self.raiz.resizable(False, False)
        #self.frame = Frame(self.raiz)
       # self.frame.pack(fill="both", expand=1)
        self.raiz.mainloop()

