# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:38:27 2024

@author: Dell
"""

archivo = open ("archivo_de_prueba.txt","    t")
contenido = "Línea1 hola amigos como están?\nLínea2 Bienvenido a Ñaña."
archivo.write(contenido)
archivo.close()