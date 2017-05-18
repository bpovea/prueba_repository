# -*- coding: utf-8 -*-
import string
class Asegurado() :
    dni = ''
    nombre = ''
    hasta = ''
    def __init__(self,dni,nombre,hasta):
        self.dni = dni
        self.nombre = nombre
        self.hasta = hasta

    def getAs(self):
        return self.nombre

    def __str__(self):
        cadena = self.nombre
        return cadena



