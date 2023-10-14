import numpy as np
import matplotlib.pyplot as plt


A = 3  
f = 100  


fs1 = 200  
fs2 = 75   


t = np.linspace(0,10,100)  


x_t = A * np.cos(2 * np.pi * f * t)


n1 = np.arange(0, len(t))
x1_n = A * np.cos(2 * np.pi * f * n1 / fs1)


n2 = np.arange(0, len(t))
x2_n = A * np.cos(2 * np.pi * f * n2 / fs2)


plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, x_t, label='Sinal Analógico')

plt.legend()

plt.subplot(3, 1, 2)
plt.stem(n1, x1_n, markerfmt='ro', basefmt=' ', linefmt='-r', label='Amostragem fs=200 Hz')
plt.legend()

plt.subplot(3, 1, 3)
plt.stem(n2, x2_n, markerfmt='bo', basefmt=' ', linefmt='-b', label='Amostragem fs=75 Hz')
plt.legend()

plt.tight_layout()
plt.show()
