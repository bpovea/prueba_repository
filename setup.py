# -*- coding: utf-8 -*-

from distutils.core import setup 
import py2exe 
 
setup(name="Correspondencia", 
 version="1.0", 
 description="prueba ejecutable para generar correspondencia automática", 
 author="byrOZ", 
 author_email="byron.povea@espol.edu.ec", 
 url="none", 
 license="GNU - estandar", 
 scripts=["prueba.py"],
 #"Email_package.__init__.py","Email_package.asegurado.py","Email_package.ejecutivo.py","Email_package.emailPropio.py","Email_package.mensaje.py"], 
 console=["prueba.py"], 
 #options={"py2exe": {"bundle_files": 1}}, 
 ascii = True,
 zipfile=None,
)