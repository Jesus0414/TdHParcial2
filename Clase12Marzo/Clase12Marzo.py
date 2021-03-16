import wave
import numpy as np
import matplotlib.pyplot as plt

Claxon = wave.open('Claxon.wav', 'r')
Aves = wave.open('Aves.wav', 'r')
#Sorprise = wave.open('Sorprise.wav', 'r')

framesClaxon = Claxon.readframes(-1)
framesAves = Aves.readframes(-1)
#framesSorprise = Sorprise.readframes(-1)

#mostrar el resultado frames
print(framesClaxon[:10])
print(framesAves[:10])
#print(framesSorprise[:10])

#Convierte el audio good morning de byte a enteros
ondaconvertidaClaxon = np.frombuffer(framesClaxon, dtype='int16')
ondaconvertidaAves = np.frombuffer(framesAves, dtype='int16')
#ondaconvertidaSorprise = np.frombuffer(framesSorprise, dtype='int16')

#Muestra los primeros 10 int
print(ondaconvertidaClaxon[:10])
print(ondaconvertidaAves[:10])
#print(ondaconvertidaSorprise[:10])

framerate_Claxon = Claxon.getframerate()
framerate_Aves = Aves.getframerate()
#framerate_Sorprise = Sorprise.getframerate()

print(framerate_Claxon)
print(framerate_Aves)
#print(framerate_Sorprise)

time_Claxon = np.linspace(start=0, stop=len(ondaconvertidaClaxon)/framerate_Claxon, num=len(ondaconvertidaClaxon))
time_Aves = np.linspace(start=0, stop=len(ondaconvertidaAves)/framerate_Aves, num=len(ondaconvertidaAves))
#time_Sorprise = np.linspace(start=0, stop=len(ondaconvertidaSorprise)/framerate_Sorprise, num=len(ondaconvertidaSorprise))

print(time_Claxon[:10])
print(time_Aves[:10])
#print(time_Sorprise[:10])

plt.title('Claxon vs Aves vs Sorprise')

plt.xlabel('Tiempo(segundos)')
plt.ylabel('Amplitud')


plt.plot(time_Aves, ondaconvertidaAves, label ='Aves')
plt.plot(time_Claxon, ondaconvertidaClaxon, label ='Claxon', alpha=0.5)
#plt.plot(time_Sorprise, ondaconvertidaSorprise, label ='Sorprise', alpha=1.0)

plt.legend()
plt.show()