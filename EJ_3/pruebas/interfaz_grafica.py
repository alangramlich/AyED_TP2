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
    boton_cuello_botella.pack_forget()
    boton_costo_minimo.pack_forget()
    cuadro_texto1 = tk.Entry(ventana)
    
    def guardar_valores2():
        peso_minimo=cuadro_texto1.get()
        cuadro_texto1.pack_forget()
        grafo_costo=Grafo()
        cargar_archivo_peso_minimo("rutas.txt", grafo_costo, peso_minimo)
        lista_ciudades_conectadas = warshall_lista(grafo_costo, "CiudadBs.As.")
        lista_ciudades=grafo_costo.obtenerVertices()
        lista_botones=[]
        def elegir_ciudad_destino(destino):
            dijkstra(grafo_costo, grafo_costo.obtenerVertice("CiudadBs.As."))
            for boton in lista_botones:
                boton.pack_forget()
            linea="El camino para ir desde CiudadBs.As. a "+str(destino)+" es: "+mostrarRuta(grafo_costo.obtenerVertice("CiudadBs.As."),grafo_costo.obtenerVertice(str(destino)), grafo_costo )+"\n"+"Y su coste es: "+str(grafo_costo.obtenerVertice(str(destino))._distancia)
                
            etiqueta=tk.Label(ventana, text=linea)
            etiqueta.pack()
        for ciudad in lista_ciudades:
            if ciudad in lista_ciudades_conectadas:
                button = tk.Button(ventana, text=ciudad,  command=lambda n=ciudad: elegir_ciudad_destino(n))
            else:
                button = tk.Button(ventana, text=ciudad, state="disabled", command=lambda n=ciudad: elegir_ciudad_destino(n))
            button.pack(padx=0, pady=0)
            lista_botones.append(button)

            
    boton_guardar = tk.Button(ventana, text="Setear peso", command=guardar_valores2)
    cuadro_texto1.pack()
    boton_guardar.pack()
        
# def buscar_costo_minimo():
#     boton_cuello_botella.pack_forget()
#     boton_costo_minimo.pack_forget()
#     cuadro_texto1 = tk.Entry(ventana)
#     cuadro_texto2 = tk.Entry(ventana)
#     cuadro_texto3 = tk.Entry(ventana)
#     def guardar_valores2():
#         inicio = cuadro_texto1.get()
#         destino = cuadro_texto2.get()
#         peso_minimo = cuadro_texto3.get()
#         cuadro_texto1.pack_forget()
#         cuadro_texto2.pack_forget()
#         cuadro_texto3.pack_forget()
#         boton_guardar.pack_forget()
#         grafo_costo=Grafo()
#         cargar_archivo_peso_minimo("rutas.txt", grafo_costo, peso_minimo)
#         print(warshall(grafo_costo, inicio, destino))
#         if (warshall(grafo_costo, inicio, destino)):
#             etiqueta_existen=tk.Label(ventana, text="¡Los nodos estan conectados!")
#             etiqueta_existen.pack()
#             dijkstra(grafo_costo, grafo_costo.obtenerVertice(inicio))
#             texto="El camino es: "+mostrarRuta(grafo_costo.obtenerVertice(inicio), grafo_costo.obtenerVertice(destino), grafo_costo)
#             etiqueta_camino=tk.Label(ventana, text=texto)
#             etiqueta_camino.pack()
#             texto="El costo es: "+str(grafo_costo.obtenerVertice(destino)._distancia)
#             etiqueta_peso_maximo=tk.Label(ventana, text=texto)
#             etiqueta_peso_maximo.pack()    
#     boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_valores2)
#     cuadro_texto1.pack()
#     cuadro_texto2.pack()
#     cuadro_texto3.pack()
#     boton_guardar.pack()

    
# Función que se ejecuta al hacer clic en el botón de cuello de botella
def buscar_cuello_de_botella():
    # Ocultar el botón de cuello de botella
    boton_cuello_botella.pack_forget()
    boton_costo_minimo.pack_forget()
    # Crear los cuadros de texto
    cuadro_texto1 = tk.Entry(ventana)
    cuadro_texto2 = tk.Entry(ventana)
    
    # Función para guardar los valores ingresados
    def guardar_valores():
        inicio = cuadro_texto1.get()
        destino = cuadro_texto2.get()
        #print("Texto 1:", inicio)
        #print("Texto 2:", destino)
        #print(type(inicio))
        cuadro_texto1.pack_forget()
        cuadro_texto2.pack_forget()
        boton_guardar.pack_forget()
        grafo_peso=Grafo()
        grafo_costo=Grafo()
        leer_archivo_grafo("rutas.txt", grafo_peso, grafo_costo)
        if (warshall(grafo_peso, inicio, destino)):
            etiqueta_existen=tk.Label(ventana, text="¡Los nodos estan conectados!")
            etiqueta_existen.pack()
            dijkstra_cuello(grafo_peso, grafo_peso.obtenerVertice(inicio))
            texto="El camino es: "+mostrarRuta(grafo_peso.obtenerVertice(inicio), grafo_peso.obtenerVertice(destino), grafo_peso)
            etiqueta_camino=tk.Label(ventana, text=texto)
            etiqueta_camino.pack()
            texto="El peso maximo es: "+str(grafo_peso.obtenerVertice(destino)._distancia)
            etiqueta_peso_maximo=tk.Label(ventana, text=texto)
            etiqueta_peso_maximo.pack()
        
        
            
    # Crear el botón de guardar
    boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_valores)
    
    # Ubicar los cuadros de texto y el botón de guardar en la ventana
    cuadro_texto1.pack()
    cuadro_texto2.pack()
    boton_guardar.pack()

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="¡Bienvenido!")

# Crear el botón de cuello de botella
boton_cuello_botella = tk.Button(ventana, text="Buscar máximo cuello de botella", command=buscar_cuello_de_botella)
boton_costo_minimo = tk.Button(ventana, text="Buscar costo minimo para determinado peso", command=buscar_costo_minimo)
# Ubicar la etiqueta y el botón en la ventana
etiqueta.pack()
boton_cuello_botella.pack()
boton_costo_minimo.pack()

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
