#importando modulo speech_recognition

import speech_recognition as sr

#definir el reconocedor
r = sr.Recognizer()

audio_file = sr.AudioFile('good-afternoon.wav')

#speech recognition
with audio_file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
    result = r.recognize_google(audio, language="en-US")

#exportar los resultados
with open('result.txt', mode='w') as file:
    file.write("Texto detectado:")
    file.write("\n")
    file.write(result)
    print("Listo!")