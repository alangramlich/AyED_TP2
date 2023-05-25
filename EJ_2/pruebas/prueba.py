# -*- coding: utf-8 -*-
"""
Created on Thu May 18 23:42:40 2023

@author: alang
"""

from modules.Temperaturas_DB import *

base_de_datos = Temperaturas_DB()
base_de_datos.guardar_temperatura("19/05/2023", 1.0)
base_de_datos.guardar_temperatura("20/05/2023", 2.0)
base_de_datos.guardar_temperatura("21/05/2023", 3.0)
base_de_datos.guardar_temperatura("22/05/2023", 4.0)
base_de_datos.guardar_temperatura("23/05/2023", 5.0)
base_de_datos.guardar_temperatura("24/05/2023", 6.0)
base_de_datos.guardar_temperatura("25/05/2023", 7.0)
base_de_datos.guardar_temperatura("26/05/2023", 8.0)
base_de_datos.guardar_temperatura("27/05/2023", 9.0)
base_de_datos.guardar_temperatura("28/05/2023", 10.0)
base_de_datos.guardar_temperatura("29/05/2023", 11.0)
base_de_datos.borrar_temperatura("19/05/2023")
base_de_datos.borrar_temperatura("20/05/2023")
base_de_datos.borrar_temperatura("21/05/2023")
base_de_datos.borrar_temperatura("22/05/2023")
base_de_datos.borrar_temperatura("23/05/2023")
base_de_datos.borrar_temperatura("24/05/2023")
base_de_datos.borrar_temperatura("25/05/2023")
base_de_datos.borrar_temperatura("26/05/2023")
base_de_datos.borrar_temperatura("27/05/2023")
base_de_datos.borrar_temperatura("28/05/2023")
base_de_datos.borrar_temperatura("29/05/2023")

#temp=base_de_datos.devolver_temperatura("26/05/2023")
#print(base_de_datos.devolver_temperatura("27/05/2023"))

#base_de_datos.borrar_temperatura("28/05/2023")
#temp2=base_de_datos.devolver_temperatura("28/05/2023")
#print(base_de_datos.devolver_temperatura("28/05/2023"))
#base_de_datos.mostrar_temperaturas("19/05/2023", "29/05/2023")
#base_de_datos.mostrar_cantidad_muestras()