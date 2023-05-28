# -*- coding: utf-8 -*-
"""
Created on Wed May 24 14:27:32 2023

@author: alang
"""

from modules.Vertice import Vertice 


class MonticuloBinario():
    """
    Clase que representa un Montículo Binario Mínimo.
    Esta clase es una modificacion de la clase del ejercicio 1. Esta adaptada para
    trabajar con vertices.
    """

    def __init__(self):
        """
        Constructor de la clase MonticuloBinario.
        Inicializa la lista de elementos, el tamaño actual del montículo y agrega
        un elemento mínimo absoluto especificado.

        Args:
            minimo_absoluto: El valor mínimo absoluto que se agrega al montículo. Siempre
            permanecera en la posicion 0.

        """
        self.listaMonticulo = (0,0)
        self.tamanoActual = 0
        
    def estaVacia(self):
        return self.tamanoActual == 0
    
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
            i: Índice del elemento en el montículo que se debe infiltrar hacia arriba.

        Returns:
            None
            
        """
        while i // 2 > 0:
          if self.listaMonticulo[i][0] < self.listaMonticulo[i // 2][0]:
              
             tmp = self.listaMonticulo[i // 2]
             self.listaMonticulo[i // 2] = self.listaMonticulo[i]
             self.listaMonticulo[i] = tmp
          i = i // 2
    
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
            i: Índice del elemento en el montículo que se debe infiltrar hacia abajo.

        Returns:
            None

        """
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i][0] > self.listaMonticulo[hm][0]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm
    
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
    
    def hijoMin(self,p):
        """
        Obtiene el índice del hijo más pequeño de un nodo en el montículo binario mínimo.
        Compara los valores de los hijos izquierdo (`i * 2`) y derecho (`i * 2 + 1`) del nodo
        en la posición `i` y devuelve el índice del hijo con el valor más pequeño.

        Args:
            i: Índice del nodo en el montículo.

        Returns:
            Índice del hijo más pequeño.

        """
        if p * 2 + 1 > self.tamanoActual:
            return p * 2
        
        else:
            if self.listaMonticulo[p*2][0] < self.listaMonticulo[p*2+1][0]:
                return p * 2
            else:
                return p * 2 + 1
    
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
        # hecho = False
        # i=1
        # clave=0
        # while not hecho and i<=self.tamanoActual:
        #     if self.listaMonticulo[i][1]== valor:
        #         hecho =True 
        #         clave=i
        #     else:
        #         i=i+1
        # if clave >0:
        #     self.listaMonticulo[clave]=(nuevaClave, self.listaMonticulo[clave][1])
        #     self.infiltArriba(clave)

    
    def construirMonticulo(self,unaLista): 
        """
        Construye un montículo binario a partir de una lista de valores.

        Crea un nuevo montículo binario utilizando los valores proporcionados en la lista.
        La lista debe contener pares de valores, donde el primer elemento del par representa la clave
        y el segundo elemento representa el valor del elemento en el montículo.

        Args:
            unaLista: Una lista de pares de valores (clave, valor) para construir el montículo.

        """
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [(0,0)]
        for dato in unaLista:
            self.listaMonticulo.append(dato)
        i = len(unaLista) // 2
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
    
