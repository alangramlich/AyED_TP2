# -*- coding: utf-8 -*-

from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 
class Paciente:
    def __init__(self, nombre=0, apellido=0, llegada=0, riesgo=None):
        n = len(nombres)
        self.__orden=llegada
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        if (riesgo is None):
            self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        else:
            self.__riesgo = riesgo
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]

    def get_orden(self):
        return self.__orden
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo
    
    def get_descripcion_riesgo(self):
        return self.__descripcion
    
    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion +'\t ->'
        cad += str(self.__orden)
        return cad
        
    def __eq__(self, other):
        return self.__riesgo==other.__riesgo & self.__orden==other.__orden 
        
    def __lt__(self, other):
        if (self.__riesgo == other.__riesgo):
            return self.__orden<other.__orden
        else:
            return self.__riesgo<other.__riesgo
        
    