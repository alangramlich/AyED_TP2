

import time
import datetime
import modules.paciente as pac
import random
from modules.MonticuloBinario import MonticuloBinario
n = 20  # cantidad de ciclos de simulación
contador=1
minimo=pac.Paciente(0,0,0,1)
lista=[]
cola_de_espera = MonticuloBinario(minimo)

# Ciclo que gestiona la simulación
for i in range(n):
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente un paciente por segundo
    # La criticidad del paciente es aleatoria
    paciente = pac.Paciente(0,0,contador)
    lista.append(paciente)
    contador+=1
    cola_de_espera.insertar(paciente)
    print('Pacientes que faltan atenderse:', len(cola_de_espera))
    for paciente in cola_de_espera:
        print('\t', paciente)
    
    print()
    print('-*-'*15)

    
    #Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        # se atiende paciente que se encuentra al frente de la cola
        paciente_atendido = cola_de_espera.eliminarMin()
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)
    else:
        # se continúa atendiendo paciente de ciclo anterior
        pass
    
    print()

    #Se muestran los pacientes restantes en la cola de espera
    
    
    time.sleep(1)
    
# for i in lista:
#     print(i)
# print(cola_de_espera)

# for i in range(5):
#     print("ATIENDO UN PACIENTE: ")
#     print(f"Paciente atendido: {cola_de_espera.eliminarMin()}")
#     print("La cola queda: ")
#     print(cola_de_espera)
#     input()