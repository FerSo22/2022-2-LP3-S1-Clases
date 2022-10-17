# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:21:18 2022

@author: FerSo
"""

import financiero

subtotal = 800.77

print(f"Subtotal: {subtotal}")
print(f"IGV: {financiero.obtenerIGVconSubtotal(subtotal):.2f}")
print(f"Total: {financiero.obtenerTotalconSubtotal(subtotal):.2f}")

