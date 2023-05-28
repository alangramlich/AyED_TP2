# -*- coding: utf-8 -*-
"""
Created on Sun May 28 10:48:03 2023

@author: alang
"""

from modules.Funciones import *

"""
    El peso maximo que se pueda transportar desde Buenos Aires hasta cualquier 
    otra ciudad de destino.
"""
#Se inicializa el grafo que nos interesa
grafo_peso=Grafo()
cargar_grafo_pesos("rutas.txt", grafo_peso)
#Se corre el algoritmo de Dijkstra modificado. Ahora, el atributo 
#"distancia" de cada vertice en el grafo queda cargado con la maxima carga 
#que puede ser transportada desde Ciudad de Buenos Aires. Y el atributo 
#"predecesor" contiene el vertice desde el que hay que viajar para poder
#reconstruir dicho camino.
dijkstra_cuello(grafo_peso, grafo_peso.obtenerVertice("CiudadBs.As."))
#Se aplica el algoritmo de Warshall para averiguar que vertices
#son alcanzables desde CiudadBs.As. 
vertices = warshall_lista(grafo_peso, "CiudadBs.As.")
#Se comunica el resultado, detallando la ruta para llegar a cada vertice
#y el peso maximo que puede ser transportado
for vertice in vertices:
    if vertice != "CiudadBs.As.":
        print(f"El camino para llegar desde CiudadBs.As. hasta {vertice} es: ")
        print(mostrarRuta(grafo_peso.obtenerVertice("CiudadBs.As."), \
                          grafo_peso.obtenerVertice(vertice), grafo_peso))
        print(f"Y su peso maximo es: {grafo_peso.obtenerVertice(vertice).obtenerDistancia()}")

        
"""
    El precio minimo para transportar un mobiliario de peso determinado
    hasta otra ciudad de destino.
"""
#Se inicializa el grafo que nos interesa. Para eso, se utiliza la funcion 
#cargar_archivo_peso_minimo, que recibe como parametro el peso minimo
#que tiene que tener una arista para ser considerada valida.
#Las aristas que no cumplen esta condicion, no son cargadas.
grafo_costo = Grafo()
peso_minimo = 90 #Puede modificarse esta variable con el peso del mobiliario
                 #a transportar.
cargar_archivo_peso_minimo("rutas.txt", grafo_costo, peso_minimo)
#Se corre el algoritmo de Dijkstra sobre este grafo. Luego de esto, 
#cada vertice del grafo tiene guardado en la variable "distancia"
#el costo de la ruta mas barata para llegar a el, y se puede reconstruir 
#esta ruta siguiendo los ancestros del mismo.
dijkstra(grafo_costo, grafo_costo.obtenerVertice("CiudadBs.As."))
#Se aplica el algoritmo de Warshall para averiguar que vertices
#son alcanzables desde CiudadBs.As. 
vertices = warshall_lista(grafo_costo, "CiudadBs.As.")
for vertice in vertices:
    if vertice != "CiudadBs.As.":
        print(f"El camino mas barato para llegar desde CiudadBs.As. hasta {vertice} es: ")
        print(mostrarRuta(grafo_costo.obtenerVertice("CiudadBs.As."), \
                          grafo_costo.obtenerVertice(vertice), grafo_costo))
        print(f"Y su costo es: {grafo_costo.obtenerVertice(vertice).obtenerDistancia()}")

