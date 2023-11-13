from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np



[fs,data]=wavfile.read('trumpEntreOrigin.wav')

ara = np.arange(0,len(data))

plt.plot(data);
plt.grid()
plt.show()