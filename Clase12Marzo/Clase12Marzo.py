import wave
import numpy as np
import matplotlib.pyplot as plt

Claxon = wave.open('Claxon.wav', 'r')
Aves = wave.open('Aves.wav', 'r')

framesClaxon = Claxon.readframes(-1)
framesAves = Aves.readframes(-1)

#mostrar el resultado frames
print(framesClaxon[:10])
print(framesAves[:10])

#Convierte el audio good morning de byte a enteros
ondaconvertidaClaxon = np.frombuffer(framesClaxon, dtype='int16')
ondaconvertidaAves = np.frombuffer(framesAves, dtype='int16')

#Muestra los primeros 10 int
print(ondaconvertidaClaxon[:10])
print(ondaconvertidaAves[:10])

framerate_Claxon = Claxon.getframerate()
framerate_Aves = Aves.getframerate()

print(framerate_Claxon)
print(framerate_Aves)

time_Claxon = np.linspace(start=0, stop=len(ondaconvertidaClaxon)/framerate_Claxon, num=len(ondaconvertidaClaxon))
time_Aves = np.linspace(start=0, stop=len(ondaconvertidaAves)/framerate_Aves, num=len(ondaconvertidaAves))

print(time_Claxon[:10])
print(time_Aves[:10])

plt.title('Claxon vs Aves')

plt.xlabel('Tiempo(segundos)')
plt.ylabel('Amplitud')

plt.plot(time_Claxon, Claxon, label ='Claxon')
plt.plot(time_Aves, Aves, label ='Aves', alpha=0.5)

plt.legend()
plt.show()