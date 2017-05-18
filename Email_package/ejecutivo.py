# -*- coding: utf-8 -*-

class Ejecutivo():
    nombre=''
    email=[]
    cc=[]
    asegurados = []
    def __init__(self,nombre, para, cc,asegurado):
        self.nombre = nombre
        self.email = para.split(';')
        self.cc=cc.split(';')
        self.asegurados = []
        self.asegurados.append(asegurado)

    def __str__(self):
        cadena = ''
        for asegurado in self.asegurados:
            cadena += '-'+asegurado.getAs()

        return self.nombre+cadena


#    def agregarEmail(self, email):
#        self.email.append(email)

#    def agregarCc (self,cc):
#        self.cc.append(cc)

    def agregarAsegurado(self,asegurado):
        self.asegurados.append(asegurado)
