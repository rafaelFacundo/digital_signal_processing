import numpy as np
import matplotlib.pyplot as plt


n = np.arange(-5, 6)
x = 2 * np.exp(-0.9 * np.abs(n))
N = 100
X = np.fft.fft(x, N)
X_mag = np.abs(X)
plt.stem(np.arange(N), X_mag, use_line_collection=True)
plt.title('Magnitude da DFT de x(n)')
plt.xlabel('k')
plt.ylabel('|X(k)|')
plt.grid()
plt.show()