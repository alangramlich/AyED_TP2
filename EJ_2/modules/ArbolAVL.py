# -*- coding: utf-8 -*-
"""
Created on Sat May 13 15:47:29 2023

@author: alang
"""
from modules.Fecha import *

class NodoArbol:
    """
    Clase que representa un nodo de un árbol binario.
    """
    def __init__(self,clave,valor,izquierdo=None,derecho=None,
                                        padre=None):
        """
        Constructor de la clase NodoArbol.
        Inicializa los atributos del nodo.

        Args:
            clave: La clave del nodo.
            valor: El valor asociado al nodo.
            izquierdo: Referencia al hijo izquierdo del nodo.
            derecho: Referencia al hijo derecho del nodo.
            padre: Referencia al nodo padre del nodo actual.

        """
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.factorEquilibrio = 0
 
    def tieneHijoIzquierdo(self):
        """
        Verifica si el nodo tiene un hijo izquierdo.

        Returns:
            bool: True si el nodo tiene un hijo izquierdo, False en caso contrario.

        """
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        """
        Verifica si el nodo tiene un hijo derecho.

        Returns:
            bool: True si el nodo tiene un hijo derecho, False en caso contrario.

        """
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        """
        Verifica si el nodo es hijo izquierdo de su padre.

        Returns:
            bool: True si el nodo es hijo izquierdo, False en caso contrario.

        """
        return self.padre and self.padre.hijoIzquierdo == self
 
    def esHijoDerecho(self):
        """
        Verifica si el nodo es hijo derecho de su padre.

        Returns:
            bool: True si el nodo es hijo derecho, False en caso contrario.

        """
        return self.padre and self.padre.hijoDerecho == self
 
    def esRaiz(self):
        """
        Verifica si el nodo es la raíz del árbol.

        Returns:
            bool: True si el nodo es la raíz, False en caso contrario.

        """
        return not self.padre
 
    def esHoja(self):
        """
        Verifica si el nodo es una hoja (no tiene hijos).

        Returns:
            bool: True si el nodo es una hoja, False en caso contrario.

        """
        return not (self.hijoDerecho or self.hijoIzquierdo)
 
    def tieneAlgunHijo(self):
        """
        Verifica si el nodo tiene al menos un hijo.

        Returns:
            bool: True si el nodo tiene al menos un hijo, False en caso contrario.

        """
        return self.hijoDerecho or self.hijoIzquierdo
 
    def tieneAmbosHijos(self):
        """
        Verifica si el nodo tiene ambos hijos.

        Returns:
            bool: True si el nodo tiene ambos hijos, False en caso contrario.

        """
        return self.hijoDerecho and self.hijoIzquierdo
 
    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        """
        Reemplaza los datos de un nodo con nuevos valores.

        Args:
            clave: La nueva clave del nodo.
            valor: El nuevo valor asociado al nodo.
            hizq: La nueva referencia al hijo izquierdo del nodo.
            hder: La nueva referencia al hijo derecho del nodo.

        Returns:
            None

        """
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

class ArbolAVL:
    """
    Clase que representa un árbol AVL.
    """
    def __init__(self):
        """
        Constructor de la clase ArbolAVL.
        Inicializa los atributos del árbol.

        """
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        """
        Devuelve el tamaño del árbol.

        Returns:
            int: El tamaño del árbol.

        """
        return self.tamano

    def __len__(self):
        """
        Devuelve el tamaño del árbol.

        Returns:
            int: El tamaño del árbol.

        """
        return self.tamano

    def __iter__(self):
        """
        Devuelve un iterador sobre los nodos del árbol.

        Returns:
            object: Iterador sobre los nodos del árbol.

        """
        return self.raiz.__iter__()
    
    def agregar(self,clave,valor):
        """
        Agrega un nuevo nodo al árbol.

        Args:
            clave: La clave del nodo.
            valor: El valor asociado al nodo.

        Returns:
            None

        """
        if self.raiz:
            self._agregar(clave,valor,self.raiz)
        else:
            self.raiz = NodoArbol(clave,valor)
        self.tamano = self.tamano + 1
    
    def _agregar(self,clave,valor,nodoActual):
        """
        Método privado para agregar un nodo al árbol.
        Solo lo usa la clase sobre si misma. El usuario no debe acceder a ella.

        Args:
            clave: La clave del nodo.
            valor: El valor asociado al nodo.
            nodoActual: El nodo actual en el proceso de búsqueda.

        Returns:
            None

        """
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                    self._agregar(clave,valor,nodoActual.hijoIzquierdo)
            else:
                    nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)
                    self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
        else:
            if nodoActual.tieneHijoDerecho():
                    self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                    nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual)
                    self.actualizarEquilibrio(nodoActual.hijoDerecho)

    def actualizarEquilibrio(self,nodo):
        """
        Actualiza los factores de equilibrio del árbol.

        Args:
            nodo: El nodo a partir del cual se actualizan los factores de equilibrio.

        Returns:
            None

        """
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.esHijoIzquierdo():
                nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                nodo.padre.factorEquilibrio -= 1

            if nodo.padre.factorEquilibrio != 0:
                self.actualizarEquilibrio(nodo.padre)
                
    def reequilibrar(self,nodo):
        """
        Realiza las rotaciones necesarias para reequilibrar el árbol.

        Args:
            nodo: El nodo a partir del cual se realiza el reequilibrio.

        Returns:
            None

        """
        if nodo.factorEquilibrio < 0:
            if nodo.hijoDerecho.factorEquilibrio > 0:
                self.rotarDerecha(nodo.hijoDerecho)
                self.rotarIzquierda(nodo)
            else:
                self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
            if nodo.hijoIzquierdo.factorEquilibrio < 0:
                self.rotarIzquierda(nodo.hijoIzquierdo)
                self.rotarDerecha(nodo)
            else:
                self.rotarDerecha(nodo)
                
                
                
    def rotarIzquierda(self,rotRaiz):
        """
        Realiza una rotación izquierda en el árbol.

        Args:
            rotRaiz: El nodo sobre el cual se realiza la rotación izquierda.

        Returns:
            None

        """
        nuevaRaiz = rotRaiz.hijoDerecho
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
        if nuevaRaiz.hijoIzquierdo != None:
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                    rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoIzquierdo = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)
                    
    def rotarDerecha(self, rotRaiz):
        """
        Realiza una rotación derecha en el árbol.

        Args:
            rotRaiz: El nodo sobre el cual se realiza la rotación derecha.

        Returns:
            None

        """
        nuevaRaiz = rotRaiz.hijoIzquierdo
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho is not None:
            nuevaRaiz.hijoDerecho.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoDerecho():
                rotRaiz.padre.hijoDerecho = nuevaRaiz
            else:
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
        nuevaRaiz.hijoDerecho = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio - 1 - max(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio - 1 + min(rotRaiz.factorEquilibrio, 0)
        
        
    def buscar_por_clave(self, clave):
        """
    Busca un nodo en el árbol por su clave.

    Args:
        clave: La clave del nodo a buscar.

    Returns:
        El nodo encontrado si existe, None en caso contrario.
        """
        nodo_actual=self.raiz
        while(1):
            if nodo_actual is None:
                return None
            elif nodo_actual.clave == clave:
                return nodo_actual
            elif nodo_actual.clave>clave:
                nodo_actual=nodo_actual.hijoIzquierdo
            elif nodo_actual.clave<clave:
                nodo_actual=nodo_actual.hijoDerecho

            
    def buscar_rango(self, clave1, clave2):
        """
        Busca y devuelve una lista de nodos cuyas claves se encuentran dentro del rango especificado.

        Args:
            clave1: El límite inferior del rango.
            clave2: El límite superior del rango.

        Returns:
            Una lista de nodos cuyas claves se encuentran dentro del rango especificado.
        """
        lista_nodos_en_rango = []
        lista_nodos_a_visitar = []
        #lista_nodos_visitados = [] NO LA NECESITO
        nodo_actual=self.raiz
        while(1):
            #chequeo el nodo actual
            if nodo_actual.clave>=clave1 and nodo_actual.clave<=clave2:
                lista_nodos_en_rango.append(nodo_actual)
                #lista_nodos_visitados.append(nodo_actual) NO LA NECESITO
                if nodo_actual.hijoDerecho is not None:
                    lista_nodos_a_visitar.append(nodo_actual.hijoDerecho)
                if nodo_actual.hijoIzquierdo is not None:
                    lista_nodos_a_visitar.append(nodo_actual.hijoIzquierdo)
            elif nodo_actual.clave>clave2: #MAYOR QUE LA MAYOR
                #en este caso, tengo que analizar el nodo por izquierda (el menor)
                if nodo_actual.hijoIzquierdo is not None:
                    lista_nodos_a_visitar.append(nodo_actual.hijoIzquierdo)
            elif nodo_actual.clave<clave1: #MENOR QUE LA MENOR
                #en este caso, analizo el hijo por derecha
                if nodo_actual.hijoDerecho is not None:
                    lista_nodos_a_visitar.append(nodo_actual.hijoDerecho)
            
            if len(lista_nodos_a_visitar) == 0:
                return lista_nodos_en_rango
            
            elif len(lista_nodos_a_visitar) > 0:
                nodo_actual=lista_nodos_a_visitar[0]
                lista_nodos_a_visitar.pop(0)
                
    def eliminar(self, clave):
        """
        Elimina un nodo del árbol por su clave.

        Args:
            clave: La clave del nodo a eliminar.
        """
        if self.raiz is None:
            return
        nodo = self.buscar_por_clave(clave)
        if nodo is None:
            return
        self._eliminar_nodo(nodo)
        self.tamano -= 1

    def _eliminar_nodo(self, nodo):
        """
        Elimina un nodo del árbol.

        Si el nodo es una hoja, se elimina directamente. Si el nodo tiene dos hijos,
        se busca el sucesor más pequeño del subárbol derecho, se copian sus datos al nodo
        a eliminar, y luego se elimina el sucesor. Si el nodo tiene solo un hijo, se reemplaza
        el nodo por su hijo y se actualiza el equilibrio.

        Args:
            nodo: El nodo a eliminar.
        """
        if nodo.esHoja():
            if nodo.esRaiz():
                self.raiz = None
            elif nodo.esHijoIzquierdo():
                nodo.padre.hijoIzquierdo = None
                self.actualizarEquilibrio(nodo.padre)
            else:
                nodo.padre.hijoDerecho = None
                self.actualizarEquilibrio(nodo.padre)
            del nodo
        elif nodo.tieneAmbosHijos():
            sucesor = self.obtener_sucesor(nodo)
            nodo.clave = sucesor.clave
            nodo.cargaUtil = sucesor.cargaUtil
            self._eliminar_nodo(sucesor)
        else:
            hijo = nodo.hijoIzquierdo or nodo.hijoDerecho
            if nodo.esRaiz():
                self.raiz = hijo
                hijo.padre = None
            elif nodo.esHijoIzquierdo():
                nodo.padre.hijoIzquierdo = hijo
                hijo.padre = nodo.padre
                self.actualizarEquilibrio(nodo.padre)
            else:
                nodo.padre.hijoDerecho = hijo
                hijo.padre = nodo.padre
                self.actualizarEquilibrio(nodo.padre)
            del nodo


    def obtener_sucesor(self, nodo):
        """
        Obtiene el sucesor más pequeño del subárbol derecho del nodo dado.

        El sucesor más pequeño es el nodo con la clave siguiente más pequeña en orden.
        Se recorre el subárbol derecho hasta encontrar el nodo más izquierdo.

        Args:
            nodo: El nodo del cual se desea encontrar el sucesor.

        Returns:
            El nodo sucesor más pequeño.
        """
        sucesor = nodo.hijoDerecho
        while sucesor.hijoIzquierdo:
            sucesor = sucesor.hijoIzquierdo
        return sucesor