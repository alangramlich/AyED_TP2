# -*- coding: utf-8 -*-
"""
Created on Mon May  8 10:40:23 2023

@author: alang
"""

class MonticuloBinario:
    def __init__(self, minimo_absoluto=0):
        self.listaMonticulo = []
        self.listaMonticulo.append(minimo_absoluto)
        self.tamanoActual = 0
        
    def infiltArriba(self,i):
        while i // 2 > 0:
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2
            
    def insertar(self,k):
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)
        
    def infiltAbajo(self,i):
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm

    def hijoMin(self,i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
            
    def eliminarMin(self):
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado
    
    def construirMonticulo(self,unaLista):
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
        