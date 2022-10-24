# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 08:39:36 2022

@author: FerSo
"""

# Importamos librería
import camelcase

nombre = "paolo jeanpier fernandez sotelo"

print(f"Mayúsculas: {nombre.upper()}")
print(f"Formato Título: {nombre.title()}")

# Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con CamelCase: ")

# Imprimimos el nombre en formato título utilizando CamelCase
print(cam.hump(nombre))

# En caso se nos pida que los nombres "paolo" y "sotelo" no se muestren con formato título

# Creamos otro objeto llamado cam2, pero a este le pasamos como argumentos los nombres que
# queremos que tengan formato título ("jeanpier" y "fernandez")

cam2 = camelcase.CamelCase('paolo', 'sotelo')
print(cam2.hump(nombre))