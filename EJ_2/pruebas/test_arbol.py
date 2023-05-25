# -*- coding: utf-8 -*-


from modules.ArbolAVL import *
import unittest
import random


def in_orden_recursivo(nodo):
    nodos = []
    if nodo:
        nodos.extend(in_orden_recursivo(nodo.hijoIzquierdo))
        nodos.append(nodo)
        nodos.extend(in_orden_recursivo(nodo.hijoDerecho))
    return nodos



class Test_arbol_AVL(unittest.TestCase):
    """Test de la clase ArbolAVL. 
    En este test se busca probar que tan bien mantiene la estructura el arbol, 
    testeando los metodos de agregar y eliminar. Para las comparaciones, se 
    utiliza un metodo que recorre el arbol en in-orden. No se testea que 
    el arbol este equilibrado.
    """
    
    def setUp(self):
        self.arbol1=ArbolAVL()
        self.arbol2=ArbolAVL()
        self.arbol3=ArbolAVL()
    
    def test_agregar(self):
        """
        En este test, se agregan los numeros del 0 al 99 y se recorre el arbol 
        in-orden, debiendo resultar en una lista con las claves ordenadas 
        de menor a mayor.
        La lista 4 contiene letras agregadas en el orden especifico que 
        garantiza todas las rotaciones posibles.
        """
        self.arbol1=ArbolAVL()
        self.arbol2=ArbolAVL()
        self.arbol3=ArbolAVL()
        self.arbol4=ArbolAVL()
        lista=list(range(0,100))
        
        for elemento in lista:
            self.arbol1.agregar(elemento, 1.0) #No importa que valor le pase
            
        random.shuffle(lista)
        for elemento in lista:
            self.arbol2.agregar(elemento, 1.0)
            
        random.shuffle(lista)
        for elemento in lista:
            self.arbol3.agregar(elemento, 1.0)
            
        lista4=['M','N','O','L','K','Q','P','H','I','A']
        for letra in lista4:
            self.arbol4.agregar(letra, 1)
            
        recorrido_arbol1=in_orden_recursivo(self.arbol1.raiz)
        recorrido_arbol2=in_orden_recursivo(self.arbol2.raiz)
        recorrido_arbol3=in_orden_recursivo(self.arbol3.raiz)
        recorrido_arbol4=in_orden_recursivo(self.arbol4.raiz)
        
        lista_claves1=[nodo.clave for nodo in recorrido_arbol1]
        lista_claves2=[nodo.clave for nodo in recorrido_arbol2]
        lista_claves3=[nodo.clave for nodo in recorrido_arbol3]
        lista_claves4=[nodo.clave for nodo in recorrido_arbol4]
        lista4.sort()
        lista=list(range(0,100))
        self.assertEqual(lista, lista_claves1)
        self.assertEqual(lista, lista_claves2)
        self.assertEqual(lista, lista_claves3)
        self.assertEqual(lista4, lista_claves4)
    
    def test_eliminar(self):
        """
        En este test, se agregan los numeros del 0 al 99 menos algunos
        eliminados aleatoriamente, y se verifica que, al recorrerse in-orden, 
        el arbol mantiene sus propiedades.
        """
        
        self.arbol1=ArbolAVL()
        self.arbol2=ArbolAVL()
        self.arbol3=ArbolAVL()
        
        lista1=list(range(0,100))
        lista2=list(range(0,100))
        lista3=list(range(0,100))
        
        for elemento in lista1:
            self.arbol1.agregar(elemento, 1.0) 
            
        random.shuffle(lista2)
        for elemento in lista2:
            self.arbol2.agregar(elemento, 1.0)
            
        random.shuffle(lista3)
        for elemento in lista3:
            self.arbol3.agregar(elemento, 1.0)

        #elimino los primeros diez elementos de cada lista
        
        for i in range(10):
            self.arbol1.eliminar(lista1[0])
            lista1.pop(0)
            self.arbol2.eliminar(lista2[0])
            lista2.pop(0)
            self.arbol3.eliminar(lista3[0])
            lista3.pop(0)
        lista1.sort()
        lista2.sort()
        lista3.sort()
        
        recorrido_arbol1=in_orden_recursivo(self.arbol1.raiz)
        recorrido_arbol2=in_orden_recursivo(self.arbol2.raiz)
        recorrido_arbol3=in_orden_recursivo(self.arbol3.raiz)
        
        lista_claves1=[nodo.clave for nodo in recorrido_arbol1]
        lista_claves2=[nodo.clave for nodo in recorrido_arbol2]
        lista_claves3=[nodo.clave for nodo in recorrido_arbol3]
        
        self.assertEqual(lista1, lista_claves1)
        self.assertEqual(lista2, lista_claves2)
        self.assertEqual(lista3, lista_claves3)
if __name__ == "__main__":
    unittest.main()
    
    
    
    
    #ARMAR CUATRO ARBOLES EN EL QUE SEPA QUE ROTACIONES DEBEN HACERSE, 
    #TESTEAR LAS CUATRO POSIBILIDADES
    #AYUDARSE CON EL SOFTWARE INTERACTIVO DE LA CATEDRA (el de teoria)