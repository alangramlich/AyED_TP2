# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:38:17 2023

@author: alang
"""
from modules.MonticuloBinarioMax import *
from modules.Grafo import *
from modules.MonticuloBinario import *
def leer_archivo_grafo(nombre_archivo, grafo_peso, grafo_costo):
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            inicio, destino, peso, costo = linea.strip().split(',')
            grafo_peso.agregarArista(inicio, destino, peso)
            grafo_costo.agregarArista(inicio, destino, costo)
            
def cargar_grafo_pesos(nombre_archivo, grafo_peso):
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            inicio, destino, peso, costo = linea.strip().split(',')
            grafo_peso.agregarArista(inicio, destino, peso)    
            
def cargar_archivo_peso_minimo(nombre_archivo, grafo_costo, peso_minimo):
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            inicio, destino, peso, costo = linea.strip().split(',')
            if int(peso)>=int(peso_minimo):
                #print(f"Cargado: {inicio},{destino},{costo}")
                grafo_costo.agregarArista(inicio, destino, costo)
            
def mostrarRuta(vertice_inicio, vertice_fin, grafo):
    ruta=""
    recorrido=[]
    vertice_actual=vertice_fin
    recorrido.append(vertice_actual)
    while vertice_actual is not vertice_inicio:
        recorrido.insert(0,vertice_actual._predecesor)
        vertice_actual=vertice_actual._predecesor
    for vertice in recorrido:
        ruta+= str(vertice.Id)+"->"
    ruta=ruta[:-2]
    return ruta

def dijkstra(unGrafo,inicio):
    cp = MonticuloBinario()
    inicio.asignarDistancia(0)
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in unGrafo])
    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()[1]
        for verticeSiguiente in verticeActual.obtenerConexiones():
            nuevaDistancia = verticeActual.obtenerDistancia() \
                    + verticeActual.obtenerPonderacion(verticeSiguiente)
            if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarDistancia( nuevaDistancia )
                verticeSiguiente.asignarPredecesor(verticeActual)
                cp.decrementarClave(verticeSiguiente,nuevaDistancia)
                

def dijkstra_cuello(unGrafo, inicio):
    cp = MonticuloBinarioMax()
    
    for v in unGrafo:
        v.asignarDistancia(0)
    inicio.asignarDistancia(float(1))  
    cp.construirMonticulo([(v.obtenerDistancia(), v) for v in unGrafo])
    
    while not cp.estaVacia():
        verticeActual = cp.eliminarMax()[1] 
        #print(f"El vertice actual es: {verticeActual}")
        
        for verticeSiguiente in verticeActual.obtenerConexiones():
            ponderacion = verticeActual.obtenerPonderacion(verticeSiguiente)
            #print(f"El vertice siguiente es: {verticeSiguiente}")
            if verticeSiguiente.estado == "no visitado":
                verticeSiguiente.asignarPredecesor(verticeActual)
                verticeSiguiente.estado="visitado"
                if verticeActual==inicio:
                    
                    verticeSiguiente._distancia=ponderacion
                    cp.incrementarClave(verticeSiguiente, ponderacion)
                else:
                    verticeSiguiente.asignarPredecesor(verticeActual)
                    verticeSiguiente._distancia=min(verticeActual._distancia, ponderacion)
                    cp.incrementarClave(verticeSiguiente, verticeSiguiente._distancia)
            elif (verticeSiguiente.estado== "visitado" and verticeActual._distancia>verticeSiguiente._distancia and verticeSiguiente._distancia<ponderacion):
                verticeSiguiente.asignarPredecesor(verticeActual)
                verticeSiguiente._distancia=min(verticeActual._distancia, ponderacion)
                    

def warshall(graph, start, end):
    node_map = {}
    index = 0
    for node in graph.obtenerVertices():
        node_map[node] = index
        index += 1

    n = len(graph.obtenerVertices())
    dist = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]

    for node in graph.obtenerVertices():
        for neighbor in graph.obtenerVertice(node).conexiones:
            i = node_map[node]
            j = node_map[neighbor.Id]
            dist[i][j] = 1  # Puedes ajustar el peso de la conexión si es necesario

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist[node_map[start]][node_map[end]] != float('inf')
    
def warshall_lista(graph, start):
    node_map = {}
    index = 0
    for node in graph.obtenerVertices():
        node_map[node] = index
        index += 1

    n = len(graph.obtenerVertices())
    dist = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]

    for node in graph.obtenerVertices():
        for neighbor in graph.obtenerVertice(node).conexiones:
            i = node_map[node]
            j = node_map[neighbor.Id]
            dist[i][j] = 1  # Puedes ajustar el peso de la conexión si es necesario

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    reachable_nodes = []
    start_index = node_map[start]
    for i, distance in enumerate(dist[start_index]):
        if distance != float('inf'):
            reachable_nodes.append(list(node_map.keys())[list(node_map.values()).index(i)])

    return reachable_nodes
