# -*- coding: utf-8 -*-
"""
Created on Wed May 24 19:20:50 2023

@author: alang
"""

class MonticuloBinarioMax():
    def __init__(self):
        self.listaMonticulo = [(999999,0)]
        self.tamanoActual = 0
        
    def estaVacia(self):
        return self.tamanoActual == 0
    
    def insertar(self, k):
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)
        
    def infiltArriba(self, i):
        while i // 2 > 0:
            if self.listaMonticulo[i][0] > self.listaMonticulo[i // 2][0]:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2
    
    def infiltAbajo(self, i):
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMax(i)
            if self.listaMonticulo[i][0] < self.listaMonticulo[hm][0]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm
    
    def eliminarMax(self):
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado
    
    def hijoMax(self, p):
        if p * 2 + 1 > self.tamanoActual:
            return p * 2
        
        else:
            if self.listaMonticulo[p * 2][0] > self.listaMonticulo[p * 2 + 1][0]:
                return p * 2
            else:
                return p * 2 + 1
    
    def incrementarClave(self, valor, nuevaClave):
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

    
    def construirMonticulo(self, unaTupla): 
        self.tamanoActual = len(unaTupla)
        self.listaMonticulo = [(999999, 999999)]
        for dato in unaTupla:
            self.listaMonticulo.append(dato)
        i = len(unaTupla) // 2
        while i > 0:
            self.infiltAbajo(i)
            i = i - 1
    
    
    def __contains__(self, vertice):
        for par in self.listaMonticulo:
            if par[1] == vertice:
                return True 
        return False
    
    def devolverMaximo(self):
        return self.listaMonticulo[1][1]
    
    
    def __iter__(self):
        return iter(self.listaMonticulo)

