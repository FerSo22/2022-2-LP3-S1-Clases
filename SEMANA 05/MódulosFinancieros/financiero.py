# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:13:11 2022

@author: FerSo

Los módulos te permiten crear librerías de funcionalidades que puedas utilizar
o reutilizar en cualquier momento en tu proyecto
"""

igv = 0.18

def obtenerIGVconSubtotal(subtotal):
    return subtotal * igv

def obtenerTotalconSubtotal(subtotal):
    # subtotal + igv * subtotal
    # subtotal * (1 + igv)
    return subtotal * (1 + igv)

def obtenerSubtotalconTotal(total):
    return total / (1 + igv)

def obtenerIGVconTotal(total):
    return total - obtenerSubtotalconTotal(total)

    