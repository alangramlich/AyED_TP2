# -*- coding: utf-8 -*-
"""
Created on Tue May 23 17:38:40 2023

@author: alang
"""
import numpy as np 
class Vertice:
    def __init__(self,clave):
        """
        Constructor de la clase Vertice.

        Args:
            clave: La clave o identificador del vértice.

        """
        self._id = clave
        self._conectadoA = {}
        self._distancia=99999999999
        self._predecesor=0
        self._max_cuello=0
        self.estado="no visitado"
    def agregarVecino(self,vecino,ponderacion=0):
        """
        Agrega un vértice vecino y su ponderación al vértice actual.

        Args:
            vecino: El vértice vecino a agregar.
            ponderacion: La ponderación de la conexión entre el vértice actual y el vecino.

        Returns:
            None

        """
        self._conectadoA[vecino] = ponderacion
    def __str__(self):
        """
        Devuelve una representación en forma de cadena del vértice.

        Returns:
            str: Representación en forma de cadena del vértice.

        """
        return str(self._id) + ' conectadoA: ' + str([x._id for x in self._conectadoA])
    @property
    def conexiones(self):
        """
        Devuelve los vértices vecinos del vértice actual.

        Returns:
            dict_keys: Vértices vecinos del vértice actual.

        """
        return self._conectadoA.keys()
    @property
    def Id(self):
        """
        Devuelve el identificador del vértice.

        Returns:
            Any: Identificador del vértice.

        """
        return self._id
    @property
    def distancia(self):
        """
        Devuelve la distancia del vértice.

        Returns:
            int: Distancia del vértice.

        """
        return self._distancia
    def ponderacion(self,vecino):
        """
        Devuelve la ponderación de la conexión entre el vértice actual y el vértice vecino.
        Esto podria significar, por ejemplo, el costo de desplazarse.
        Args:
            vecino: El vértice vecino.

        Returns:
            int: Ponderación de la conexión.

        """
        return self._conectadoA[vecino]
    def setDistancia(self, valor):
        """
        Establece la distancia del vértice.

        Args:
            valor: Nuevo valor de la distancia.

        Returns:
            None

        """
        self._distancia=valor
    @property
    def predecesor(self, predecesor):
        """
        Devuelve el predecesor del vértice.

        Returns:
            Any: Predecesor del vértice.

        """
        return self._predecesor
    @property
    def predecesor(self, predecesor):
        """
        Establece el predecesor del vértice.

        Args:
            predecesor: Nuevo predecesor del vértice.

        Returns:
            None

        """
        self._predecesor=predecesor
    def asignarDistancia(self, dist):
        """
        Asigna una distancia al vértice.

        Args:
            dist: Distancia a asignar al vértice.

        Returns:
            None

        """
        self._distancia=dist
    def obtenerDistancia(self):
        """
        Devuelve la distancia del vértice.

        Returns:
            int: Distancia del vértice.

        """
        return self._distancia
    def obtenerConexiones(self):
        """
        Devuelve los vértices vecinos del vértice actual.

        Returns:
            dict_keys: Vértices vecinos del vértice actual.

        """
        return self._conectadoA.keys()
    def obtenerPonderacion(self, vecino):
        """
        Devuelve la ponderación de la conexión entre el vértice actual y el vértice vecino.

        Args:
            vecino: El vértice vecino.

        Returns:
            int: Ponderación de la conexión.

        """
        return self._conectadoA[vecino]
    def asignarPredecesor(self, predecesor):
        """
        Asigna un predecesor al vértice.

        Args:
            predecesor: Predecesor a asignar al vértice.

        Returns:
            None

        """
        self._predecesor=predecesor
        