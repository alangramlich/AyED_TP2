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
    def setUp(self):
        self.db = Temperaturas_DB()

    def test_guardar_temperatura(self):
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
        self.db.guardar_temperatura('01/01/2023', 25.5)
        self.db.borrar_temperatura('01/01/2023')
        temperatura = self.db.devolver_temperatura('01/01/2023')
        self.assertIsNone(temperatura)

    def test_mostrar_temperaturas(self):
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
