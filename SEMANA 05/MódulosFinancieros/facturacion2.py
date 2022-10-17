# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:28:20 2022

@author: FerSo
"""

# Dado el total, calcular el IGV y el subtotal

import financiero

total = 1000.49

print(f"Subtotal: {financiero.obtenerSubtotalconTotal(total):.2f}")
print(f"IGV: {financiero.obtenerIGVconTotal(total):.2f}")
print(f"Total: {total}")