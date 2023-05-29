# -*- coding: utf-8 -*-
"""
Created on Wed May 24 21:44:31 2023

@author: alang
"""
from modules.Funciones import *
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Establecer las dimensiones de la ventana
ventana.geometry("400x200")
def buscar_costo_minimo():
    boton_cuello_botella.grid_forget()
    boton_costo_minimo.grid_forget()
    cuadro_texto1 = tk.Entry(ventana)
    
    def guardar_valores2():
        peso_minimo=cuadro_texto1.get()
        cuadro_texto1.grid_forget()
        boton_guardar.grid_forget()
        grafo_costo=Grafo()
        cargar_archivo_peso_minimo("rutas.txt", grafo_costo, peso_minimo)
        lista_ciudades_conectadas = warshall_lista(grafo_costo, "CiudadBs.As.")
        lista_ciudades=grafo_costo.obtenerVertices()
        
        lista_botones=[]
        def elegir_ciudad_destino(destino):
            dijkstra(grafo_costo, grafo_costo.obtenerVertice("CiudadBs.As."))
            for boton in lista_botones:
                boton.grid_forget()
            linea="El camino para ir desde CiudadBs.As. a "+str(destino)+" es: "+mostrarRuta(grafo_costo.obtenerVertice("CiudadBs.As."),grafo_costo.obtenerVertice(str(destino)), grafo_costo )+"\n"+"Y su coste es: "+str(grafo_costo.obtenerVertice(str(destino))._distancia)
                
            etiqueta=tk.Label(ventana, text=linea)
            etiqueta.grid()
            
            
        contador = 0
        num_columnas = 2
        for ciudad in lista_ciudades:
            fila = contador // num_columnas
            columna = contador % num_columnas
            if ciudad in lista_ciudades_conectadas and ciudad != "CiudadBs.As.":
                button = tk.Button(ventana, text=ciudad,  command=lambda n=ciudad: elegir_ciudad_destino(n))
            else:
                button = tk.Button(ventana, text=ciudad, state="disabled", command=lambda n=ciudad: elegir_ciudad_destino(n))
            button.grid(row=fila, column=columna, padx=5, pady=5)
            lista_botones.append(button)
            contador += 1


            
    boton_guardar = tk.Button(ventana, text="Setear peso", command=guardar_valores2)
    cuadro_texto1.grid()
    boton_guardar.grid()
        
    
# Función que se ejecuta al hacer clic en el botón de cuello de botella
def buscar_cuello_de_botella():
    # Ocultar el botón de cuello de botella
    boton_cuello_botella.grid_forget()
    boton_costo_minimo.grid_forget()
    # Crear los cuadros de texto
    #cuadro_texto1 = tk.Entry(ventana)
    #cuadro_texto2 = tk.Entry(ventana)
    grafo_peso=Grafo()
    grafo_costo=Grafo()
    leer_archivo_grafo("rutas.txt", grafo_peso, grafo_costo)
    lista_de_ciudades=grafo_peso.obtenerVertices()
    def elegir_ciudad_origen(inicio):
        for boton in lista_botones:
            boton.grid_forget()
        ciudades_conectadas=warshall_lista(grafo_peso, inicio)
        lista_ciudades=grafo_peso.obtenerVertices()
        contador = 0
        num_columnas = 2
        def elegir_ciudad_destino2(destino):
            dijkstra_cuello(grafo_peso, grafo_peso.obtenerVertice(inicio))
            for boton in lista_botones:
                boton.grid_forget()
            linea="El camino para ir desde "+str(inicio)+" a "+str(destino)+" es: "+mostrarRuta(grafo_peso.obtenerVertice(str(inicio)),grafo_peso.obtenerVertice(str(destino)), grafo_peso )+"\n"+"Y su cuello de botella es: "+str(grafo_peso.obtenerVertice(str(destino))._distancia)
            
            etiqueta=tk.Label(ventana, text=linea)
            etiqueta.grid()
        for ciudad in lista_ciudades:
            fila = contador // num_columnas
            columna = contador % num_columnas
            if ciudad in ciudades_conectadas and ciudad != "CiudadBs.As.":
                button = tk.Button(ventana, text=ciudad,  command=lambda n=ciudad: elegir_ciudad_destino2(n))
            else:
                button = tk.Button(ventana, text=ciudad, state="disabled", command=lambda n=ciudad: elegir_ciudad_destino2(n))
            button.grid(row=fila, column=columna, padx=5, pady=5)
            lista_botones.append(button)
            contador += 1
    contador = 0
    num_columnas = 2
    lista_botones=[]
    for ciudad in lista_de_ciudades:
        fila = contador // num_columnas
        columna = contador % num_columnas
        button = tk.Button(ventana, text=ciudad,  command=lambda n=ciudad: elegir_ciudad_origen(n))
        button.grid(row=fila, column=columna, padx=5, pady=5)
        lista_botones.append(button)
        contador += 1
        
    
    # Función para guardar los valores ingresados
    def guardar_valores():
        inicio = cuadro_texto1.get()
        destino = cuadro_texto2.get()
        #print("Texto 1:", inicio)
        #print("Texto 2:", destino)
        #print(type(inicio))
        cuadro_texto1.grid_forget()
        cuadro_texto2.grid_forget()
        boton_guardar.grid_forget()
        
        if (warshall(grafo_peso, inicio, destino)):
            etiqueta_existen=tk.Label(ventana, text="¡Los nodos estan conectados!")
            etiqueta_existen.grid()
            dijkstra_cuello(grafo_peso, grafo_peso.obtenerVertice(inicio))
            texto="El camino es: "+mostrarRuta(grafo_peso.obtenerVertice(inicio), grafo_peso.obtenerVertice(destino), grafo_peso)
            etiqueta_camino=tk.Label(ventana, text=texto)
            etiqueta_camino.grid()
            texto="El peso maximo es: "+str(grafo_peso.obtenerVertice(destino)._distancia)
            etiqueta_peso_maximo=tk.Label(ventana, text=texto)
            etiqueta_peso_maximo.grid()
        
        
            


# Crear una etiqueta
etiqueta = tk.Label(ventana, text="¡Bienvenido!")

# Crear el botón de cuello de botella
boton_cuello_botella = tk.Button(ventana, text="Buscar máximo cuello de botella", command=buscar_cuello_de_botella)
boton_costo_minimo = tk.Button(ventana, text="Buscar costo minimo para determinado peso", command=buscar_costo_minimo)
# Ubicar la etiqueta y el botón en la ventana
etiqueta.grid()
boton_cuello_botella.grid()
boton_costo_minimo.grid()

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
