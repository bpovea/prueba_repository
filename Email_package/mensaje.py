# -*- coding: utf-8 -*-

class Mensaje():
    cabecera = ''
    para = ''
    filas = []
    final = ''
    textofinal = ''
    def __init__(self,ejecutivo):

        self.para =  ejecutivo.nombre

        self.cabecera = u"""
        Estimado/a %s

        Un gusto saludarle esperando se encuentre muy bien.
        Realizando el seguimiento de las Pólizas externas Homologadas de bienes en Garantía con el BANCO PICHINCHA C.A.
        dejamos a conocimiento que esta próximo el vencimiento de las pólizas de seguro de los clientes detallados
        a continuación:
        """%(ejecutivo.nombre)

        self.filas=[u"""
            Cédula/Ruc: %s
            Nombre: %s
            Fecha de vencimiento: %s
        """%(ejecutivo.asegurados[len(ejecutivo.asegurados)-1].dni,ejecutivo.asegurados[len(ejecutivo.asegurados)-1].nombre,ejecutivo.asegurados[len(ejecutivo.asegurados)-1].hasta)]


        self.final= u"""
        Es importante indicar que nosotros como NOVAECUADOR podemos gestionar la renovación de dichas pólizas, ofreciendo nuestra asesoría
        y servicio preferencial como clientes de Banco el cual consiste en mejorar las coberturas, costos, beneficios y agilidad en el proceso
        del Ingreso de los documentos a Custodia.

        Agradeceríamos nos ayuden con los datos de contactos de estos clientes para poderles ayudar con la gestión antes indicada y evitar que
        estas garantías se queden desprotegidas,regularizando a tiempo su cobertura de seguro.

        Cualquier duda que tengan al respecto, favor coméntenme.


        Saludos,

        Nora Morales P.
        EJECUTIVA COMERCIAL CORPORATIVA
        nmorales@novaecuador.com
        Telf.: (593 4) 2118-251 | 242 | 253 | 238 ext. 403
        Dir.: Av. José Santiago Castillo y Justino Cornejo Edif. Natural Vitality, Kennedy Norte Oficina 401, 4to Piso
        """

    def agregarLinea(self,ejecutivo):
            self.filas.append(u"""
            Cédula/Ruc: %s
            Nombre: %s
            Fecha de vencimiento: %s
            """ % (ejecutivo.asegurados[0].dni, ejecutivo.asegurados[0].nombre, ejecutivo.asegurados[0].hasta))



    def getMensaje(self):
        self.textofinal=self.cabecera
        for linea in self.filas:
            self.textofinal=self.textofinal+linea
        self.textofinal = self.textofinal+self.final
        return self.textofinal