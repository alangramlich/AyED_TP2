# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:28:31 2023

@author: alang
"""
from modules.Vertice import Vertice
import numpy as np 


class Grafo:
    """
    Esta clase representa un grafo.
    """
    def __init__(self):
        """
        Inicializa un objeto Grafo.

        El grafo se representa utilizando un diccionario donde las claves son las etiquetas de los vértices y los valores son
        los objetos vértice correspondientes.

        """
        self._listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave):
        """
        Agrega un nuevo vértice al grafo.

        Args:
            clave: La etiqueta o identificador del vértice.

        Returns:
            Vertice: El objeto vértice recién creado.

        """
        nuevoVertice=None
        if clave not in self.obtenerVertices():
            self.numVertices = self.numVertices + 1
            nuevoVertice = Vertice(clave)
            self._listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n):
        """
        Obtiene el vértice correspondiente a una clave específica.

        Args:
            n: La clave del vértice a buscar.

        Returns:
            Vertice: El objeto vértice correspondiente a la clave, o None si no se encuentra.

        """
        if n in self._listaVertices:
            return self._listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        """
        Verifica si un vértice está presente en el grafo.

        Args:
            n: La clave del vértice a verificar.

        Returns:
            bool: True si el vértice está presente, False en caso contrario.

        """
        return n in self.listaVertices

    def agregarArista(self,de,a,costo=0):
        """
        Agrega una arista entre dos vértices al grafo.

        Si los vértices especificados no existen en el grafo, se crean nuevos vértices con las claves proporcionadas.

        Args:
            de: La clave del vértice de origen.
            a: La clave del vértice de destino.
            costo: El costo o peso asociado a la arista. Por defecto es 0.

        """
        if de not in self._listaVertices:
            nv = self.agregarVertice(de)
        if a not in self._listaVertices:
            nv = self.agregarVertice(a)
        self._listaVertices[de].agregarVecino(self._listaVertices[a], int(costo))

    def obtenerVertices(self):
        """
        Obtiene una lista con las claves de todos los vértices en el grafo.

        Returns:
            list: Una lista con las claves de los vértices.

        """
        return self._listaVertices.keys()

    def __iter__(self):
        """
        Devuelve un iterador que permite recorrer los vértices del grafo.

        Returns:
            iter: Un iterador de los objetos vértice del grafo.

        """
        return iter(self._listaVertices.values())
    
    
    
    def decrementarClave(self, valor, nuevaClave):
        """
        Decrementa la clave de un valor específico en el montículo binario.

        Busca el valor en el montículo y actualiza su clave con el valor proporcionado.
        Luego, realiza las operaciones necesarias para mantener la propiedad del montículo.

        Args:
            valor: El valor para el cual se desea decrementar la clave.
            nuevaClave: La nueva clave a asignar al valor.

        """
        for i, (clave, v) in enumerate(self.listaMonticulo[1:], start=1):
            if v == valor:
                self.listaMonticulo[i] = (nuevaClave, v)
                self.infiltArriba(i)
                return
