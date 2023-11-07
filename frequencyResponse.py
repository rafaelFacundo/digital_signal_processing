from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def calculateFrequencyResponse(A_coeficients, B_coeficients):
    return signal.freqz(B_coeficients, A_coeficients);

w, h = calculateFrequencyResponse([1,-0.9],[1])

angles = np.unwrap(np.angle(h))

plt.plot(w, angles);
plt.show()