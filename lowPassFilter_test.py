from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal



#OMEGA_c = PI/4


wc = np.pi/4; # aqui é a banda de 
M = 20 #aqui é o tamanho do filtro
N = 512 #aqui nós temos o tamanho da DFT
n = np.arange(-M, M) 
h = wc/np.pi * np.sinc(wc*(n)/np.pi) #aqui estamos definindo a função h(n) do filtro passa baixa ideal

w, Hh = signal.freqz(h, 1, whole=True, worN=N) # pegando o dominio da frequencia
#wx = np.fft.fftfreq(len(w)) #dando um shift para o centro para poder plotar




fig, axs = plt.subplots(3,1);

fig.set_size_inches((8,8))
plt.subplots_adjust(hspace=0.3)

ax=axs[0]
ax.stem(n+M,h,basefmt='b-')
ax.set_xlabel("n",fontsize=16)
ax.set_ylabel("amplitude",fontsize=16)

ax=axs[1]
ax.plot(w-np.pi,abs(np.fft.fftshift(Hh)))
ax.axis(xmax=np.pi/2,xmin=-np.pi/2)
ax.vlines([-wc,wc],0,1.2,color='g',lw=2.,linestyle='--',)
ax.hlines(1,-np.pi,np.pi,color='g',lw=2.,linestyle='--',)
ax.set_xlabel(r"",fontsize=22)
ax.set_ylabel(r"",fontsize=22)
ax.grid()


ax=axs[2]
ax.plot(w-np.pi,20*np.log10(abs(np.fft.fftshift(Hh))))
ax.axis(ymin=-40,xmax=np.pi/2,xmin=-np.pi/2)
ax.vlines([-wc,wc],10,-40,color='g',lw=2.,linestyle='--',)
ax.hlines(0,-np.pi,np.pi,color='g',lw=2.,linestyle='--',)
ax.grid()
ax.set_xlabel(r"",fontsize=22)
ax.set_ylabel(r"",fontsize=18)

plt.show()