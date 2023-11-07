import numpy as np
import matplotlib.pyplot as plt

#RESPOSTA LETRA A
# def H(w):
#     return (2 * np.exp(1j * w)) / (np.exp(1j * w) - 0.9)

#RESPOSTA LETRA C
# def H(w):
#     return (1/(1-0.5*np.exp(-1j*w))) + (1/(1-0.4*np.exp(-1j*w)))

omega = np.linspace(-np.pi, np.pi, 1000)


H_omega = H(omega)


magnitude = np.abs(H_omega)
phase = np.angle(H_omega)


plt.figure(1)
plt.plot(omega, magnitude)
plt.title("Resposta em Magnitude")
plt.xlabel("Frequência [radianos]")
plt.ylabel("Magnitude")


plt.figure(2)
plt.plot(omega, phase)
plt.title("Resposta de Fase")
plt.xlabel("Frequência [radianos]")
plt.ylabel("Fase [radianos]")

plt.show()