# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 09:28:01 2022

@author: FerSo
"""

archivo = open("noticia.txt", "at")
contenido = "\nFuente: RPP"

archivo.write(contenido)
archivo.close()