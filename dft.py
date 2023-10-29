import numpy as np
import matplotlib.pyplot as plt

N = 100

x = np.linspace(-2,2,N);
y = np.zeros(N);
y[abs(x) < 1] = x[abs(x) < 1]

c = np.zeros(N, complex)
n = np.arange(N)
for k in range(N):
    c[k] = np.sum(y*np.exp(-2j*np.pi*k*n/N))

plt.figure(figsize=(12,4))

plt.subplot(1,2,1)
plt.plot(np.imag(c), label="imag")
plt.plot(np.real(c), label="real")
plt.legend()

plt.subplot(1,2,2)
plt.plot(abs(c), "r", label="mag")
plt.legend()

plt.show()