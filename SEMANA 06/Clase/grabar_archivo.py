# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 09:23:52 2022

@author: FerSo
"""

archivo = open("archivo_de_prueba.txt", "wt")
contenido = "Línea1 Hola amigos cómo estan?\nLínea2 Bievenido a la UNTELS"
archivo.write(contenido)
archivo.close()