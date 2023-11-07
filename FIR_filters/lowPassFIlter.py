import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def ideal_lowPass_filter(Wc, M):
    h = [];
    for n in range(-M, M):
        result = Wc/np.pi * np.sinc(Wc * (n)/np.pi)
        h.append(result)
    return h

h = ideal_lowPass_filter(np.pi/4, 20);


def takeFreqz(h, N):
    w, Hh = signal.freqz(h, 1, whole=True, worN=N)
    return w, Hh

w, Hh = takeFreqz(h, 512);

fig,axs = plt.subplots(3,1)
fig.set_size_inches((8,8))
plt.subplots_adjust(hspace=0.3)

M=20
wc = np.pi/4
n = np.arange(-M,M)
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
