import numpy as np
import matplotlib.pyplot as plt
from scipy import signal, special
import math

def multiplySignals(signalOne, signalTwo):
    lenghtDifference = len(signalOne) - len(signalTwo)
    if lenghtDifference > 0:
        arrayOfZeros = [0] * lenghtDifference;
        signalTwo = signalTwo + arrayOfZeros;
    elif lenghtDifference < 0:
        arrayOfZeros = [0] * lenghtDifference;
        signalOne = signalOne + arrayOfZeros;
    
    result = [];
    for n in range(len(signalOne)):
        result.append(signalOne[n] * signalTwo[n])
    return result;

def ideal_lowPass_filter(Wc, M):
    h = [];
    hPart = []
    h.append(Wc/np.pi)
    for n in range(1, math.floor(M/2)+1):
        hPart.append(1/(np.pi * n) * (np.sin(Wc*n)))
    return list(reversed(hPart)) + h + hPart;

def ideal_highPass_filter(Wc, M):
    h = [];
    hPart = []
    h.append(1 - Wc/np.pi)
    for n in range(1,  math.floor(M/2)+1):
        hPart.append((-1/np.pi * n) * np.sin(Wc * n));
    return list(reversed(hPart)) + h + hPart;

def bandPass_filter(Wc1, Wc2, M):
    h = [];
    hPart = []
    h.append((Wc2 - Wc1)/np.pi)
    for n in range(1,  math.floor(M/2)+1):
        hPart.append(1/(np.pi * n) * (np.sin(Wc2*n) - np.sin(Wc1*n)));
    return list(reversed(hPart)) + h + hPart;
    

def bandReject_filter(Wc1, Wc2, M):
    h = [];
    hPart = []
    h.append(1 - (Wc2 - Wc1)/np.pi)
    for n in range(1,  math.floor(M/2)+1):
        hPart.append(1/(np.pi * n) * (np.sin(Wc1*n)-np.sin(Wc2*n)));
    return list(reversed(hPart)) + h + hPart;
   
   
h = ideal_lowPass_filter(np.pi/4, 13);

#h = ideal_highPass_filter(np.pi/8, 13);
#h = bandPass_filter(np.pi/16, np.pi/2, 13);
#h = bandReject_filter(np.pi/4, np.pi/30, 30);

print("asas", len(h))


def rectangularWindow(M):
    w = []
    limit = 0;
    if M % 2 == 0:
        limit = math.floor(M/2)
        for n in range(-limit, limit):
            w.append(1);
        w = [0]*limit + w + [0]*limit;
    else:
        limit = math.floor((M-1)/2)
        for n in range(-limit, (limit+1)):
            w.append(1)
        w = [0]*limit + w + [0]*(limit+1)
    return w

def hammingWindow(Alfa, M):
    w = []
    limit = 0;
    if M % 2 == 0:
        limit = math.floor(M/2)
        for n in range(-limit, limit):
            w.append(Alfa + (1-Alfa) * np.cos((2 * np.pi * n)/M))
        w = [0]*limit + w + [0]*limit;
    else:
        limit = math.floor((M-1)/2)
        for n in range(-limit, (limit+1)):
            w.append(Alfa + (1-Alfa) * np.cos((2 * np.pi * n)/M))
        w = [0]*limit + w + [0]*(limit+1)        
    return w;

def blackManWindow(M):
    w = []
    limit = 0
    if M % 2 == 0:
        limit = math.floor(M/2)
        for n in range(-limit, limit):
            w.append(0.42 + 0.5*np.cos(2* np.pi * n/M) + 0.08 * np.cos(4 * np.pi/M ))
        w = [0]*limit + w + [0]*limit;
    else:
        limit = math.floor((M-1)/2)
        for n in range(-limit, (limit+1)):
            w.append(0.42 + 0.5*np.cos(2* np.pi * n/M) + 0.08 * np.cos(4 * np.pi /M ))
        w = [0]*limit + w + [0]*(limit+1)        
    return w;

def Io_function(x):
    return special.j0(x);

def kaiserWindow(M, beta):
    w = []
    limit = 0
    besselFunctionArgument = 0
    if M % 2 == 0:
        limit = math.floor(M/2)
        for n in range(-limit, limit):
            besselFunctionArgument = beta * np.sqrt(1 - math.pow((2 * n)/M, 2))
            w.append(special.j0(besselFunctionArgument)/special.j0(beta))
        w = [0]*limit + w + [0]*limit;
    else:
        limit = math.floor((M-1)/2)
        for n in range(-limit, (limit+1)):
            besselFunctionArgument = beta * np.sqrt(1 - math.pow((2 * n)/M, 2))
            w.append(special.j0(besselFunctionArgument)/special.j0(beta))
        w = [0]*limit + w + [0]*(limit+1)        
    return w;

def takeFreqz(h, N):
    w, Hh = signal.freqz(h, 1)
    return w, Hh

rectWindow = blackManWindow(20)

#h = multiplySignals(h, rectWindow);


w, Hh = takeFreqz(h, 512);


fig,axs = plt.subplots(3,1)
fig.set_size_inches((8,8))
plt.subplots_adjust(hspace=0.3)


M=31
wc = np.pi/4
n = np.arange(0,len(h))
ax=axs[0]
print("asdjaks")
ax.stem(n,h,basefmt='b-')

ax.set_xlabel("n",fontsize=16)
ax.set_ylabel("amplitude",fontsize=16)



"""
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
"""

plt.show()
