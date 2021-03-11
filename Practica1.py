import wave
import numpy as np

#Cargar  archivo wav en la variable 
GM = wave.open('good-morningMan.wav', 'r')

frames = GM.readframes(-1)

#mostrar el resultado frames
#print(frames[:10])

#Convierte el audio good morning de byte a enteros
ondaconvertida = np.frombuffer(frames, dtype='int16')

#Muestra los primeros 10 int
print(ondaconvertida[:10])