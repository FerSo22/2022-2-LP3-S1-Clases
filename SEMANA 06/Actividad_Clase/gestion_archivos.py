# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 09:41:21 2022

@author: FerSo
"""
import os

def crear_archivo(nombreArchivo, contenido):
    archivo = open(nombreArchivo + ".txt", "wt")
    archivo.write(contenido)
    archivo.close()

def eliminar_archivo(nombreArchivo):
    os.remove(nombreArchivo + ".txt")
    
def agregar_contenido(nombreArchivo, contenido):
    archivo = open(nombreArchivo + ".txt", "at")
    archivo.write(contenido)
    archivo.close()
    
def leer_archivo(nombreArchivo):
    archivo = open(nombreArchivo + ".txt", encoding="utf8")
    datos_archivo = archivo.read()

    return datos_archivo