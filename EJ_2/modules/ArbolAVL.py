# -*- coding: utf-8 -*-
"""
Created on Sat May 13 15:47:29 2023

@author: alang
"""
from modules.Fecha import *

class NodoArbol:
    def __init__(self,clave,valor,izquierdo=None,derecho=None,
                                        padre=None):
         self.clave = clave
         self.cargaUtil = valor
         self.hijoIzquierdo = izquierdo
         self.hijoDerecho = derecho
         self.padre = padre
         self.factorEquilibrio = 0
 
    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self
 
    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self
 
    def esRaiz(self):
        return not self.padre
 
    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)
 
    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo
 
    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo
 
    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

class ArbolAVL:
    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano

    def __iter__(self):
        return self.raiz.__iter__()
    
    def agregar(self,clave,valor):
        if self.raiz:
            self._agregar(clave,valor,self.raiz)
        else:
            self.raiz = NodoArbol(clave,valor)
        self.tamano = self.tamano + 1
    
    def _agregar(self,clave,valor,nodoActual):
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
        if self.raiz is None:
            return
        nodo = self.buscar_por_clave(clave)
        if nodo is None:
            return
        self._eliminar_nodo(nodo)
        self.tamano -= 1

    def _eliminar_nodo(self, nodo):
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
        sucesor = nodo.hijoDerecho
        while sucesor.hijoIzquierdo:
            sucesor = sucesor.hijoIzquierdo
        return sucesor