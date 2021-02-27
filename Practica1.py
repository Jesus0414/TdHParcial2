import wave

GM = wave.open('good-morningMan.wav', 'r')

frames = GM.readframes(-1)

print(frames[:100])