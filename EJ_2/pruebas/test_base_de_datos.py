# -*- coding: utf-8 -*-
"""
Created on Sat May 20 13:59:14 2023

@author: alang
"""

from modules.Temperaturas_DB import *
import unittest
import random


import unittest

class TestTemperaturasDB(unittest.TestCase):
    """Test de la clase TemperaturasDB. 
    En este test se busca probar que la base de datos TemperaturasDB guarde 
    correctamente los datos y devuelva los valores esperados.
    """
    def setUp(self):
        self.db = Temperaturas_DB()

    def test_guardar_temperatura(self):
        """
        Prueba el método guardar_temperatura de la clase Temperaturas_DB.

        Se asegura de que el método guardar_temperatura agregue temperaturas correctamente
        y que el método devolver_temperatura recupere las temperaturas guardadas correctamente.
        """
        self.db.guardar_temperatura('01/01/2023', 25.5)
        self.db.guardar_temperatura('02/01/2023', 24.8)
        self.db.guardar_temperatura('03/01/2023', 26.1)
        self.db.guardar_temperatura('04/01/2023', 23.5)
        self.db.guardar_temperatura('05/01/2023', 22.9)
        self.db.guardar_temperatura('06/01/2023', 24.3)
        self.db.guardar_temperatura('07/01/2023', 27.6)
        self.db.guardar_temperatura('08/01/2023', 25.8)
        self.db.guardar_temperatura('09/01/2023', 23.7)
        self.db.guardar_temperatura('10/01/2023', 22.1)
        temperatura = self.db.devolver_temperatura('01/01/2023')
        self.assertEqual(temperatura, 25.5)

    def test_devolver_temperatura(self):
        """
        Prueba el método devolver_temperatura de la clase Temperaturas_DB.

        Se asegura de que el método devolver_temperatura recupere correctamente las temperaturas
        guardadas previamente utilizando el método guardar_temperatura.

        """
        self.db.guardar_temperatura('01/01/2023', 25.5)
        self.db.guardar_temperatura('02/01/2023', 24.8)
        self.db.guardar_temperatura('03/01/2023', 26.1)
        self.db.guardar_temperatura('04/01/2023', 23.5)
        self.db.guardar_temperatura('05/01/2023', 22.9)
        self.db.guardar_temperatura('06/01/2023', 24.3)
        self.db.guardar_temperatura('07/01/2023', 27.6)
        self.db.guardar_temperatura('08/01/2023', 25.8)
        self.db.guardar_temperatura('09/01/2023', 23.7)
        self.db.guardar_temperatura('10/01/2023', 22.1)
        temperatura = self.db.devolver_temperatura('01/01/2023')
        self.assertEqual(temperatura, 25.5)

    def test_max_temp_rango(self):
        """
        Prueba el método max_temp_rango de la clase Temperaturas_DB.

        Se asegura de que el método max_temp_rango devuelva correctamente la temperatura máxima
        dentro de un rango de fechas específico.
        """
        self.db.guardar_temperatura('01/01/2023', 25.5)
        self.db.guardar_temperatura('02/01/2023', 24.8)
        self.db.guardar_temperatura('03/01/2023', 26.1)
        self.db.guardar_temperatura('04/01/2023', 23.5)
        self.db.guardar_temperatura('05/01/2023', 22.9)
        self.db.guardar_temperatura('06/01/2023', 24.3)
        self.db.guardar_temperatura('07/01/2023', 27.6)
        self.db.guardar_temperatura('08/01/2023', 25.8)
        self.db.guardar_temperatura('09/01/2023', 23.7)
        self.db.guardar_temperatura('10/01/2023', 22.1)
        max_temp = self.db.max_temp_rango('01/01/2023', '10/01/2023')
        self.assertEqual(max_temp, 27.6)

    def test_min_temp_rango(self):
        """
        Prueba el método min_temp_rango de la clase Temperaturas_DB.

        Se asegura de que el método min_temp_rango devuelva correctamente la temperatura mínima
        dentro de un rango de fechas específico.
        """
        self.db.guardar_temperatura('01/01/2023', 25.5)
        self.db.guardar_temperatura('02/01/2023', 24.8)
        self.db.guardar_temperatura('03/01/2023', 26.1)
        self.db.guardar_temperatura('04/01/2023', 23.5)
        self.db.guardar_temperatura('05/01/2023', 22.9)
        self.db.guardar_temperatura('06/01/2023', 24.3)
        self.db.guardar_temperatura('07/01/2023', 27.6)
        self.db.guardar_temperatura('08/01/2023', 25.8)
        self.db.guardar_temperatura('09/01/2023', 23.7)
        self.db.guardar_temperatura('10/01/2023', 22.1)
        min_temp = self.db.min_temp_rango('01/01/2023', '10/01/2023')
        self.assertEqual(min_temp, 22.1)

    def test_temp_extremos_rango(self):
        """
        Prueba el método temp_extremos_rango de la clase Temperaturas_DB.

        Se asegura de que el método temp_extremos_rango devuelva correctamente las temperaturas
        mínima y máxima dentro de un rango de fechas específico.
        """
        self.db.guardar_temperatura('01/01/2023', 25.5)
        self.db.guardar_temperatura('02/01/2023', 24.8)
        self.db.guardar_temperatura('03/01/2023', 26.1)
        self.db.guardar_temperatura('04/01/2023', 23.5)
        self.db.guardar_temperatura('05/01/2023', 22.9)
        self.db.guardar_temperatura('06/01/2023', 24.3)
        self.db.guardar_temperatura('07/01/2023', 27.6)
        self.db.guardar_temperatura('08/01/2023', 25.8)
        self.db.guardar_temperatura('09/01/2023', 23.7)
        self.db.guardar_temperatura('10/01/2023', 22.1)
        extremos = self.db.temp_extremos_rango('01/01/2023', '10/01/2023')
        self.assertEqual(extremos, (22.1, 27.6))

    def test_borrar_temperatura(self):
        """
        Prueba el método borrar_temperatura de la clase Temperaturas_DB.

        Se asegura de que el método borrar_temperatura elimine correctamente una temperatura
        para una fecha específica. Se agrega una temperatura utilizando el método guardar_temperatura,
        luego se llama al método borrar_temperatura para eliminar la temperatura agregada y finalmente
        se verifica que la temperatura no se pueda recuperar utilizando el método devolver_temperatura.
        """
        self.db.guardar_temperatura('01/01/2023', 25.5)
        self.db.borrar_temperatura('01/01/2023')
        temperatura = self.db.devolver_temperatura('01/01/2023')
        self.assertIsNone(temperatura)

    def test_mostrar_temperaturas(self):
        """
        Prueba el método mostrar_temperaturas de la clase Temperaturas_DB.

       Se asegura de que el método mostrar_temperaturas imprima correctamente las temperaturas
       en un rango de fechas específico. Se agregan varias temperaturas con fechas y valores específicos
       utilizando el método guardar_temperatura. Luego se redirige la salida estándar para capturar la
       salida impresa por el método mostrar_temperaturas. Después se restaura la salida estándar y se
       verifica que la salida capturada coincida con la salida esperada.
       """
        self.db.guardar_temperatura('01/01/2023', 25.5)
        self.db.guardar_temperatura('02/01/2023', 28.7)
        self.db.guardar_temperatura('03/01/2023', 22.3)

        # Redirigir la salida estándar para capturar la salida
        import sys
        from io import StringIO
        stdout = sys.stdout
        sys.stdout = StringIO()

        self.db.mostrar_temperaturas('01/01/2023', '03/01/2023')

        # Restaurar la salida estándar
        output = sys.stdout.getvalue()
        sys.stdout = stdout

        expected_output = "01/01/2023: 25.5 °C\n02/01/2023: 28.7 °C\n03/01/2023: 22.3 °C\n"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
