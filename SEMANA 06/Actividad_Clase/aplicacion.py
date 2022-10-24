# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 09:49:42 2022

@author: FerSo
"""
import gestion_archivos

def menu():
    print("\t\t\t\t******MENU DE OPCIONES******\n")
    print("1. Crear Archivo\n" +
          "2. Eliminar Archivo\n" +
          "3. Agregar Contenido\n" +
          "4. Mostrar Contenido de Archivo\n" +
          "5. Salir\n")
    
    opcion = int(input("Digite la opción: "))
    
    if opcion == 1:
        crear()
    elif opcion == 2:
        eliminar()
    elif opcion == 3:
        agregar()     
    elif opcion == 4:
        listar() 
    elif opcion == 5:
        salir()
    else:
        error()

def crear():
    nombre = input("Introduce el nombre del archivo a crear: ")
    contenido = input(f"Introduce el contenido para el archivo '{nombre}' (Enter para terminar de digitar):\n")

    gestion_archivos.crear_archivo(nombre, contenido)

def eliminar():
    nombre = input("Introduce el nombre del archivo a eliminar: ")

    gestion_archivos.eliminar_archivo(nombre)

    print(f"Archivo '{nombre}' eliminado con éxito")

def agregar():
    nombre = input("Introduce el nombre del archivo al que se le agregará contenido: ")
    contenido = input(f"Introduce el contenido para el archivo '{nombre}' (Enter para terminar de digitar):\n")

    gestion_archivos.agregar_contenido(nombre, contenido)

def listar():
    nombre = input("Introduce el nombre del archivo del que se leerá su contenido: ")
    contenido = gestion_archivos.leer_archivo(nombre)

    print(f"El contenido del archivo '{nombre}' es el siguiente:\n{contenido}")

def salir():
    return

def error():
    print("ERROR: OPCIÓN NO VÁLIDA\nPROGRAMA FINALIZADO")

menu()
