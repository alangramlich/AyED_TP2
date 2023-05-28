# -*- coding: utf-8 -*-
"""
Created on Wed May 24 19:20:50 2023

@author: alang
"""

class MonticuloBinarioMax():
    """
    Clase que representa un monticulo binario máximo. Esto es, un monticulo binario
    que deja su elemento mayor para ser sacado.
    """
    def __init__(self):
        """
        Constructor de la clase MonticuloBinarioMax.
        Inicializa el montículo binario máximo con un elemento máximo absoluto especificado.

        """
        self.listaMonticulo = [(999999,0)]
        self.tamanoActual = 0
        
    def estaVacia(self):
        """
        Verifica si el montículo está vacío.

        Returns:
            bool: True si el montículo está vacío, False en caso contrario.

        """
        return self.tamanoActual == 0
    
    def insertar(self, k):
        """
        Inserta un nuevo elemento `k` en el montículo binario máximo. El elemento se agrega
        al final de la lista `listaMonticulo` y luego se realiza el proceso de "infiltración
        hacia arriba" para mantener la propiedad de orden del montículo.

        Args:
            k: El elemento a insertar en el montículo.

        Returns:
            None

        """
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)
        
    def infiltArriba(self, i):
        """
        Realiza el proceso de "infiltración hacia arriba" en el montículo binario máximo
        a partir de un índice `i`. Este proceso consiste en comparar el elemento en el
        índice `i` con su padre y, si es mayor, intercambiarlos. Luego, se repite el proceso
        con el padre hasta que el elemento se encuentre en la posición correcta.

        Args:
            i: Índice a partir del cual se realiza la infiltración hacia arriba.

        Returns:
            None

        """
        while i // 2 > 0:
            if self.listaMonticulo[i][0] > self.listaMonticulo[i // 2][0]:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2
    
    def infiltAbajo(self, i):
        """
        Realiza el proceso de "infiltración hacia abajo" en el montículo binario máximo
        a partir de un índice `i`. Este proceso consiste en comparar el elemento en el
        índice `i` con sus hijos y, si alguno de ellos es mayor, intercambiarlos. Luego,
        se repite el proceso con el hijo mayor hasta que el elemento se encuentre en la
        posición correcta.

        Args:
            i: Índice a partir del cual se realiza la infiltración hacia abajo.

        Returns:
            None

        """
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMax(i)
            if self.listaMonticulo[i][0] < self.listaMonticulo[hm][0]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm
    
    def eliminarMax(self):
        """
        Elimina y devuelve el elemento máximo del montículo binario máximo. El elemento
        máximo se encuentra en la raíz del montículo. Después de eliminarlo, se reorganiza
        el montículo realizando el proceso de "infiltración hacia abajo" desde la nueva raíz.

        Returns:
            tuple: El elemento máximo eliminado del montículo.

        """
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado
    
    def hijoMax(self, p):
        """
        Devuelve el índice del hijo mayor del elemento en el índice `p` en el montículo binario máximo.
        Si ambos hijos tienen el mismo valor, se devuelve el índice del hijo izquierdo.

        Args:
            p: Índice del elemento padre.

        Returns:
            int: Índice del hijo mayor.

        """
        if p * 2 + 1 > self.tamanoActual:
            return p * 2
        
        else:
            if self.listaMonticulo[p * 2][0] > self.listaMonticulo[p * 2 + 1][0]:
                return p * 2
            else:
                return p * 2 + 1
    
    def incrementarClave(self, valor, nuevaClave):
        """
        Incrementa la clave de un elemento en el montículo binario máximo a partir de su valor.
        Si el elemento se encuentra en el montículo, se actualiza su clave y se realiza el
        proceso de "infiltración hacia arriba" para mantener la propiedad de orden del montículo.

        Args:
            valor: Valor del elemento cuya clave se va a incrementar.
            nuevaClave: Nueva clave del elemento.

        Returns:
            None

        """
        hecho = False
        i = 1
        clave = 0
        while not hecho and i <= self.tamanoActual:
            if self.listaMonticulo[i][1] == valor:
                hecho = True
                clave = i
            else:
                i = i + 1
        if clave > 0:
            self.listaMonticulo[clave] = (nuevaClave, self.listaMonticulo[clave][1])
            self.infiltArriba(clave)

    
    def construirMonticulo(self, unaLista): 
        """
        Construye un montículo binario máximo a partir de una lista de elementos. La lista se
        agrega a `listaMonticulo` y luego se realiza el proceso de "infiltración hacia abajo"
        en cada elemento a partir de la mitad de la longitud de la lista.

        Args:
            unaLista: Lista de elementos a partir de la cual se construirá el montículo.

        Returns:
            None

        """
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [(999999, 999999)]
        for dato in unaLista:
            self.listaMonticulo.append(dato)
        i = len(unaLista) // 2
        while i > 0:
            self.infiltAbajo(i)
            i = i - 1
    
    
    def __contains__(self, vertice):
        """
        Verifica si un vértice dado se encuentra en el montículo binario máximo.

        Args:
            vertice: Vértice a verificar su presencia en el montículo.

        Returns:
            bool: True si el vértice está presente en el montículo, False en caso contrario.

        """
        for par in self.listaMonticulo:
            if par[1] == vertice:
                return True 
        return False
    
    def devolverMaximo(self):
        """
        Devuelve el valor del elemento máximo en el montículo binario máximo.

        Returns:
            int: Valor del elemento máximo.

        """
        return self.listaMonticulo[1][1]
    
    
    def __iter__(self):
        """
        Implementa la iteración sobre los elementos del montículo binario máximo.

        Returns:
            iter: Iterador sobre los elementos del montículo.

        """
        return iter(self.listaMonticulo)

