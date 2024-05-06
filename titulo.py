# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:09:32 2024

@author: Dell
"""

import camelcasex|

nombre="diego jeremy caballero villazana"
print(nombre.upper())
print(nombre.title())

#Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con camelcase....")

# imprimimos el nombre en formato título
# utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# creamos otro objeto llamado cam2
# al definir el objeto, incluimos los argumentos
# 'flor' y 'león' 
cam2 = camelcase.CamelCase('diego','villazana')
print(cam2.hump(nombre))
