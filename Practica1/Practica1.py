import wave
import numpy as np
import matplotlib.pyplot as plt

#Cargar  archivo wav en la variable 
GM = wave.open('good-morningMan.wav', 'r')
GA = wave.open('good-afternoon.wav', 'r')

framesGM = GM.readframes(-1)
framesGA = GA.readframes(-1)

#mostrar el resultado frames
#print(frames[:10])

#Convierte el audio good morning de byte a enteros
ondaconvertidaGM = np.frombuffer(framesGM, dtype='int16')
ondaconvertidaGA = np.frombuffer(framesGA, dtype='int16')

#Muestra los primeros 10 int
#print(ondaconvertida[:10])

framerate_gm = GM.getframerate()
framerate_ga = GA.getframerate()

#print(framerate_gm)
#print(framerate_ga)

time_gm = np.linspace(start=0, stop=len(ondaconvertidaGM)/framerate_gm, num=len(ondaconvertidaGM))
time_ga = np.linspace(start=0, stop=len(ondaconvertidaGA)/framerate_ga, num=len(ondaconvertidaGA))

#print(time_gm[:10])
#print(time_ga[:10])

#generacion de la grafica
plt.title('Good morning vs Good afternoon')

#etiquetas de los ejes
plt.xlabel('Tiempo(segundos)')
plt.ylabel('Amplitud')

#agregar informacion de las ondas para graficar
plt.plot(time_ga, ondaconvertidaGA, label ='Good afternoon')
plt.plot(time_gm, ondaconvertidaGM, label ='Good morning', alpha=0.5)

plt.legend()
plt.show()