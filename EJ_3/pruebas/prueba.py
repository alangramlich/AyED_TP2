# -*- coding: utf-8 -*-

from modules.Funciones import *
 

grafo_peso=Grafo()
grafo_costo=Grafo()
leer_archivo_grafo("rutas2.txt", grafo_peso, grafo_costo)
dijkstra_cuello(grafo_costo, grafo_costo.obtenerVertice("4"))
#print (mostrarRuta(grafo_costo.obtenerVertice("4"), grafo_costo.obtenerVertice("3"), grafo_costo))
# print(grafo_costo.obtenerVertice("4"))
#dijkstra(grafo_costo, grafo_costo.obtenerVertice("4"))
# buscarMaximoPeso(grafo_costo, grafo_costo.obtenerVertice("4"))
#print(grafo_peso.obtenerVertice("CiudadBs.As."))
#lista=grafo_peso.obtenerVertices()
#print(grafo_costo.obtenerVertice("Rosario")._predecesor)
# print (mostrarRuta(grafo_costo.obtenerVertice("4"), grafo_costo.obtenerVertice("3"), grafo_costo))

print(mostrarRuta(grafo_costo.obtenerVertice("4"), grafo_costo.obtenerVertice("3"), grafo_costo))



#start="4"

#print(warshall_lista(grafo_costo, start))
# print(warshall(grafo_peso, "4", "3"))
# dijkstra_cuello(grafo_peso, grafo_peso.obtenerVertice("4"))
# print(mostrarRuta(grafo_costo.obtenerVertice("4"), grafo_costo.obtenerVertice("3"), grafo_peso))