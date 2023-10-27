import numpy as np
import matplotlib.pyplot as plt

# Comprimento da sequência
N = 256  # Escolha um número grande para obter uma aparência suave no gráfico

# Vetor de amostras de n
n = np.arange(-N//2, N//2)

# Defina a sequência 𝑥(𝑛) de acordo com a descrição
x = 2 * np.exp(-0.9 * np.abs(n))

# Calcule a DFT da sequência x usando a função fft do NumPy
X = np.fft.fft(x)

# Crie um vetor de frequências correspondentes à DTFT
frequencias = np.fft.fftfreq(N)

# Plote a DTFT da sequência x
plt.figure(figsize=(8, 6))
plt.plot(frequencias, np.abs(X))
plt.title('DTFT da Sequência x(𝑛)')
plt.xlabel('Frequência')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()
