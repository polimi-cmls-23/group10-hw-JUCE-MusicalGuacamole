import numpy as np
from scipy import signal
import matplotlib.pylab as plt
import sounddevice as sd

Fs = 8000
f = 100
sample = 80
x = np.arange(sample)
sine = 4*np.sin(2 * np.pi * f *4* x / Fs)
square = signal.square(2 * np.pi * f * x / Fs)

target_signal = square
diff = square - sine
update = diff

morphed = np.array([])
morphed_chunk = sine
morphing_speed = 0.003 # how fast morphing is
while True:
    morphed_chunk = morphed_chunk + morphing_speed*update
    morphed = np.concatenate((morphed, morphed_chunk))
    update = target_signal - morphed_chunk
    if np.mean(update**2) < 0.000001:
            break
sd.play(morphed, Fs)

plt.plot( morphed[-1000:-1])
plt.xlabel('sample(n)')
plt.ylabel('signal value')
plt.title('Target signal (Square wave at 100 Hz)')
plt.show()

plt.plot( morphed[0:1000])
plt.xlabel('sample(n)')
plt.ylabel('signal value')
plt.title('First signal (Square wave at 400 Hz)')
plt.show()

plt.plot( morphed[int(len(morphed)/2):int(len(morphed)/2)+1000])
plt.xlabel('sample(n)')
plt.ylabel('signal value')
plt.title('Half morphed signal')
plt.show()
