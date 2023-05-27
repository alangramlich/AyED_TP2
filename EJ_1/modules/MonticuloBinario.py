# -*- coding: utf-8 -*-
"""
Created on Mon May  8 10:40:23 2023

@author: alang
"""

class MonticuloBinario:
    """
    Clase que representa un Montículo Binario Mínimo.

    Un montículo binario es una estructura de datos basada en un árbol binario completo,
    donde el valor de cada nodo es menor o igual que los valores de sus hijos. El montículo
    binario mínimo se utiliza principalmente para mantener el elemento más pequeño en la raíz.
    """
    def __init__(self, minimo_absoluto=0):
        """
        Constructor de la clase MonticuloBinario.
        Inicializa la lista de elementos, el tamaño actual del montículo y agrega
        un elemento mínimo absoluto especificado.

        Args:
            minimo_absoluto: El valor mínimo absoluto que se agrega al montículo. Siempre
            permanecera en la posicion 0.

        """
        self.listaMonticulo = []
        self.listaMonticulo.append(minimo_absoluto)
        self.tamanoActual = 0
        
    def infiltArriba(self,i):
        """
    Realiza el proceso de "infiltración hacia arriba" en el montículo. Este proceso
    se utiliza para mantener la propiedad de orden del montículo binario mínimo
    después de insertar un elemento en la posición `i`.

    El proceso de infiltración hacia arriba compara el elemento en la posición `i`
    con su padre en la posición `i // 2` y realiza intercambios si es necesario para
    cumplir con la propiedad de orden. El proceso se repite hasta que el elemento
    en la posición `i` sea mayor o igual que su padre, o hasta llegar a la raíz del
    montículo.

    Args:
        i (int): Índice del elemento en el montículo que se debe infiltrar hacia arriba.

    Returns:
        None

    """
        while i // 2 > 0:
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2
            
    def insertar(self,k):
        """
    Inserta un nuevo elemento `k` en el montículo binario mínimo. El elemento se agrega
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
        
    def infiltAbajo(self,i):
        """
    Realiza el proceso de "infiltración hacia abajo" en el montículo. Este proceso
    se utiliza para mantener la propiedad de orden del montículo binario mínimo
    después de eliminar el elemento en la posición `i`.

    El proceso de infiltración hacia abajo compara el elemento en la posición `i`
    con sus hijos (izquierdo y derecho) y realiza intercambios con el hijo más pequeño
    si es necesario para cumplir con la propiedad de orden. El proceso se repite hasta
    que el elemento en la posición `i` sea menor o igual que sus hijos o hasta que no
    tenga hijos.

    Args:
        i (int): Índice del elemento en el montículo que se debe infiltrar hacia abajo.

    Returns:
        None

    """
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm

    def hijoMin(self,i):
        """
    Obtiene el índice del hijo más pequeño de un nodo en el montículo binario mínimo.
    Compara los valores de los hijos izquierdo (`i * 2`) y derecho (`i * 2 + 1`) del nodo
    en la posición `i` y devuelve el índice del hijo con el valor más pequeño.

    Args:
        i (int): Índice del nodo en el montículo.

    Returns:
        int: Índice del hijo más pequeño.

    """
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
            
    def eliminarMin(self):
        """
    Elimina y devuelve el elemento mínimo (raíz) del montículo binario mínimo.

    El elemento mínimo se encuentra en la posición 1 de la lista `listaMonticulo`.
    Se intercambia con el último elemento del montículo (posición `tamanoActual`),
    luego se reduce el tamaño actual del montículo en uno y se elimina el último
    elemento de la lista. Finalmente, se realiza el proceso de "infiltración hacia
    abajo" desde la raíz para restaurar la propiedad de orden del montículo.

    Returns:
        El valor del elemento mínimo que se ha eliminado del montículo.

    """
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado
    
    def construirMonticulo(self,unaLista):
        """
    Construye un montículo binario mínimo a partir de una lista dada.

    El montículo se construye utilizando el algoritmo de "infiltración hacia abajo".
    Se establece el tamaño actual del montículo como la longitud de la lista `unaLista`.
    Luego, se crea una copia de la lista `unaLista` y se asigna a `listaMonticulo` con
    un elemento extra en la posición 0. A continuación, se itera a través de los nodos
    internos del montículo (desde la mitad hacia la raíz) y se realiza la infiltración
    hacia abajo en cada nodo para asegurar la propiedad de orden.

    Args:
        unaLista (list): La lista de elementos a partir de la cual se construirá el montículo.

    Returns:
        None

    """
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1
            
    def __str__(self):
        linea=''
        for i in range(self.tamanoActual):
            linea+=self.listaMonticulo[i+1].get_nombre()+self.listaMonticulo[i+1].get_apellido()+self.listaMonticulo[i+1].get_descripcion_riesgo()+str(self.listaMonticulo[i+1].get_orden())+'\n'
        return linea
    
    def __len__(self):
        return self.tamanoActual
    
    def __iter__(self):
        return iter(self.listaMonticulo[1:])