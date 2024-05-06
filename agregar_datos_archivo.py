# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:39:24 2024

@author: Dell
"""

archivo = open("archivo_de_prueba.txt","at")
# \n es para agregar el contenido en una línea al final
contenido="\nFuente: RPP"

archivo.write(contenido)

archivo.close()
