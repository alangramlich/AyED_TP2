# -*- coding: utf-8 -*-
"""
Created on Thu May 18 22:32:09 2023

@author: alang
"""
from modules.ArbolAVL import *
from modules.Fecha import *
def comparar_fechas(fecha1, fecha2):
    dia1, mes1, anio1 = map(int, fecha1.split('/'))
    dia2, mes2, anio2 = map(int, fecha2.split('/'))
    
    if anio1 < anio2:
        return True
    elif anio1 == anio2 and mes1 < mes2:
        return True
    elif anio1 == anio2 and mes1 == mes2 and dia1 < dia2:
        return True
    
    return False


class Temperaturas_DB:
    def __init__(self):
        """
        Inicializa una instancia de Temperaturas_DB.

        Crea un árbol AVL vacío para almacenar las temperaturas.
        """
        self.arbol = ArbolAVL()
        
        
    def guardar_temperatura(self, fecha_str, temperatura):
        """
        Guarda una temperatura en la base de datos.

        Args:
            fecha_str (str): La fecha en formato "dd/mm/aaaa".
            temperatura (float): El valor de la temperatura a guardar.
        """
        if type(fecha_str) == str and type(temperatura) == float:
            fecha=Fecha(fecha_str)
            self.arbol.agregar(fecha, temperatura)
        
        
    def devolver_temperatura(self, fecha_str):
        """
        Devuelve la temperatura asociada a una fecha específica.

        Args:
            fecha_str (str): La fecha en formato "dd/mm/aaaa".

        Returns:
            float: El valor de la temperatura asociada a la fecha, o None si no se encuentra la fecha.
        """
        if type(fecha_str) == str:
            fecha=Fecha(fecha_str)
            nodo_buscado=self.arbol.buscar_por_clave(fecha)
            if nodo_buscado is not None:
                return nodo_buscado.cargaUtil
            else:
                return None
            
    def max_temp_rango(self, fecha1_str, fecha2_str):
        """
        Devuelve la temperatura máxima dentro de un rango de fechas.

        Args:
            fecha1_str (str): La fecha inicial del rango en formato "dd/mm/aaaa".
            fecha2_str (str): La fecha final del rango en formato "dd/mm/aaaa".

        Returns:
            float: El valor de la temperatura máxima dentro del rango especificado.
        """
        if type(fecha1_str) == str and type(fecha2_str) == str and comparar_fechas(fecha1_str, fecha2_str):
            fecha1=Fecha(fecha1_str)
            fecha2=Fecha(fecha2_str)
            nodos_buscados = self.arbol.buscar_rango(fecha1, fecha2)
            lista_ordenada = sorted(nodos_buscados, key=lambda nodo: nodo.cargaUtil)
            return lista_ordenada[len(lista_ordenada)-1].cargaUtil
        
    def min_temp_rango(self, fecha1_str, fecha2_str):
        """
        Devuelve la temperatura mínima dentro de un rango de fechas.

        Args:
            fecha1_str (str): La fecha inicial del rango en formato "dd/mm/aaaa".
            fecha2_str (str): La fecha final del rango en formato "dd/mm/aaaa".

        Returns:
            float: El valor de la temperatura mínima dentro del rango especificado.
        """
        if type(fecha1_str) == str and type(fecha2_str) == str and comparar_fechas(fecha1_str, fecha2_str):
            fecha1=Fecha(fecha1_str)
            fecha2=Fecha(fecha2_str)
            nodos_buscados = self.arbol.buscar_rango(fecha1, fecha2)
            lista_ordenada = sorted(nodos_buscados, key=lambda nodo: nodo.cargaUtil)
            return lista_ordenada[0].cargaUtil
        
    def temp_extremos_rango(self, fecha1_str, fecha2_str):
        """
        Devuelve las temperaturas mínima y máxima dentro de un rango de fechas.

        Args:
            fecha1_str (str): La fecha inicial del rango en formato "dd/mm/aaaa".
            fecha2_str (str): La fecha final del rango en formato "dd/mm/aaaa".

        Returns:
            tuple: Una tupla que contiene la temperatura mínima y la temperatura máxima dentro del rango especificado.
        """
        if type(fecha1_str) == str and type(fecha2_str) == str and comparar_fechas(fecha1_str, fecha2_str):
            fecha1=Fecha(fecha1_str)
            fecha2=Fecha(fecha2_str)
            nodos_buscados = self.arbol.buscar_rango(fecha1, fecha2)
            lista_ordenada = sorted(nodos_buscados, key=lambda nodo: nodo.cargaUtil)
            minima = lista_ordenada[0].cargaUtil
            maxima = lista_ordenada[len(lista_ordenada)-1].cargaUtil
            return minima, maxima
        
    def borrar_temperatura(self, fecha_str):
        """
        Elimina una temperatura asociada a una fecha específica de la base de datos.

        Args:
            fecha_str (str): La fecha en formato "dd/mm/aaaa".
        """
        if type(fecha_str) == str:
            fecha=Fecha(fecha_str)
        self.arbol.eliminar(fecha)
        
    def mostrar_temperaturas(self, fecha1_str, fecha2_str):
        """
        Muestra las temperaturas dentro de un rango de fechas.

        Args:
            fecha1_str (str): La fecha inicial del rango en formato "dd/mm/aaaa".
            fecha2_str (str): La fecha final del rango en formato "dd/mm/aaaa".
        """
        if type(fecha1_str) == str and type(fecha2_str) == str and comparar_fechas(fecha1_str, fecha2_str):
            fecha1=Fecha(fecha1_str)
            fecha2=Fecha(fecha2_str)
        lista = self.arbol.buscar_rango(fecha1, fecha2)
        lista = sorted(lista, key=lambda nodo: nodo.clave)
        for nodo in lista:
            print(f"{nodo.clave}: {nodo.cargaUtil} °C")
            
    def mostrar_cantidad_muestras(self):
        """
        Muestra la cantidad de muestras (temperaturas) almacenadas en la base de datos.
        """
        print(f"La cantidad de muestras es: {self.arbol.tamano}")