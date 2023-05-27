# -*- coding: utf-8 -*-
"""
Created on Thu May 18 23:02:49 2023

@author: alang
"""

class Fecha:
    
    def __init__(self, fecha_str):
        """
        Inicializa una instancia de Fecha.

        Args:
            fecha_str (str): Una cadena en formato "dd/mm/aaaa" que representa la fecha.
        """
        self.dia, self.mes, self.anio = map(int, fecha_str.split('/'))
        self.verificar_fecha()

    def verificar_fecha(self):
        """
        Verifica si la fecha es válida.

        Lanza un ValueError si la fecha es inválida.
        """
        if self.dia < 1 or self.dia > 31:
            raise ValueError("El día debe estar en el rango de 1 a 31.")

        if self.mes < 1 or self.mes > 12:
            raise ValueError("El mes debe estar en el rango de 1 a 12.")

    def __repr__(self):
        """
        Devuelve una representación de cadena str de la fecha.

        Returns:
            str: La representación de cadena de la fecha en formato "Fecha(dd/mm/aaaa)".
        """
        return f"Fecha({self.dia:02d}/{self.mes:02d}/{self.anio})"

    def __eq__(self, other):
        """
        Compara si dos fechas son iguales.

        Args:
            other (Fecha): La otra fecha a comparar.

        Returns:
            bool: True si las fechas son iguales, False en caso contrario.
        """
        if isinstance(other, Fecha):
            return self.dia == other.dia and self.mes == other.mes and self.anio == other.anio
        return False

    def __lt__(self, other):
        """
        Compara si una fecha es menor que otra.

        Args:
            other (Fecha): La otra fecha a comparar.

        Returns:
            bool: True si la fecha es menor que la otra, False en caso contrario.
        """
        if isinstance(other, Fecha):
            if self.anio < other.anio:
                return True
            elif self.anio == other.anio:
                if self.mes < other.mes:
                    return True
                elif self.mes == other.mes:
                    return self.dia < other.dia
        return False

    def __le__(self, other):
        """
        Compara si una fecha es menor o igual que otra.

        Args:
            other (Fecha): La otra fecha a comparar.

        Returns:
            bool: True si la fecha es menor o igual que la otra, False en caso contrario.
        """
        return self.__lt__(other) or self.__eq__(other)

    def __str__(self):
        """
        Devuelve una representación de cadena str de la fecha.

        Returns:
            str: La representación de cadena de la fecha en formato "dd/mm/aaaa".
        """
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio:04d}"


