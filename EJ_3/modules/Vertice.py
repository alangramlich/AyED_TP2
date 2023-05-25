# -*- coding: utf-8 -*-
"""
Created on Tue May 23 17:38:40 2023

@author: alang
"""
import numpy as np 
class Vertice:
    def __init__(self,clave):
        self._id = clave
        self._conectadoA = {}
        self._distancia=99999999999
        self._predecesor=0
        self._max_cuello=0
        self.estado="no visitado"
    def agregarVecino(self,vecino,ponderacion=0):
        self._conectadoA[vecino] = ponderacion
    def __str__(self):
        return str(self._id) + ' conectadoA: ' + str([x._id for x in self._conectadoA])
    @property
    def conexiones(self):
        return self._conectadoA.keys()
    @property
    def Id(self):
        return self._id
    @property
    def distancia(self):
        return self._distancia
    def ponderacion(self,vecino):
        return self._conectadoA[vecino]
    def setDistancia(self, valor):
        self._distancia=valor
    @property
    def predecesor(self, predecesor):
        return self._predecesor
    @property
    def predecesor(self, predecesor):
        self._predecesor=predecesor
    def asignarDistancia(self, dist):
        self._distancia=dist
    def obtenerDistancia(self):
        return self._distancia
    def obtenerConexiones(self):
        return self._conectadoA.keys()
    def obtenerPonderacion(self, vecino):
        return self._conectadoA[vecino]
    def asignarPredecesor(self, predecesor):
        self._predecesor=predecesor
        