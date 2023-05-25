# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:28:31 2023

@author: alang
"""
from modules.Vertice import Vertice
import numpy as np 


class Grafo:
    def __init__(self):
        self._listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self._listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n):
        if n in self._listaVertices:
            return self._listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices

    def agregarArista(self,de,a,costo=0):
        if de not in self._listaVertices:
            nv = self.agregarVertice(de)
        if a not in self._listaVertices:
            nv = self.agregarVertice(a)
        self._listaVertices[de].agregarVecino(self._listaVertices[a], int(costo))

    def obtenerVertices(self):
        return self._listaVertices.keys()

    def __iter__(self):
        return iter(self._listaVertices.values())
