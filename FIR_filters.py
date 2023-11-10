import numpy as np
import matplotlib.pyplot as plt
from scipy import signal, special
import math

#definitions of the ideal filters

def Hn_idealLowPassFilter(n, Wc):
    if n == 0:
        return Wc/np.pi;
    return (1/(np.pi * n)) * np.sin(Wc * n);

def Hn_idealHighPassFilter(n, Wc):
    if n == 0:
        return 1 - Wc/np.pi
    return (-1/(np.pi*n)) * np.sin(Wc*n);

def Hn_idealBandPassFilter(n, Wc1, Wc2):
    if n == 0:
        return (Wc2 - Wc1)/np.pi;
    return (1/(np.pi *n)) * (np.sin(Wc2*n) - np.sin(Wc1*n));

def Hn_idealBandRejectFilter(n, Wc1, Wc2):
    if n == 0:
        return 1 - (Wc2 - Wc1)/np.pi;
    return (1/(np.pi *n)) * (np.sin(Wc1*n) - np.sin(Wc2*n));

#definitions of the windows


def Wn_rectangularWindow(n, M):
    if abs(n) <= math.floor(M/2):
        return 1;
    return 0;

def Wn_HammingWindow(n, M):
    if abs(n) <= math.floor(M/2):
        return 0.54 + (1 - 0.54) * np.cos((2*np.pi*n)/M);
    return 0;

def Wn_HanningWindow(n, M):
    if abs(n) <= math.floor(M/2):
        return 0.5 + (1 - 0.5) * np.cos((2*np.pi*n)/M);
    return 0;

def Wn_blackManWindow(n, M):
    if abs(n) <= math.floor(M/2):
        return 0.42 + 0.5*np.cos((2*np.pi*n)/M) + 0.08*np.cos((4*np.pi*n)/M);
    return 0;

def Wn_KaiserWindow(n, M, beta):
    if abs(n) <= math.floor(M/2):
        besselFunctionArgument = beta * np.sqrt(1 - math.pow((2 * n)/M, 2))
        return special.j0(besselFunctionArgument)/special.j0(beta);
    return 0;

def takeWindow(windowName):
    if windowName == "retangular":
        return Wn_rectangularWindow;
    elif windowName == "hamming":
        return Wn_HammingWindow;
    elif windowName == "hanning":
        return Wn_HanningWindow;
    elif windowName == "blackman":
        return Wn_blackManWindow;
    elif windowName == "kaiser":
        return Wn_KaiserWindow;
    else:
        return None;

def takeFilter(filterName):
    print(filterName)
    if filterName == "passa-baixa":
        return Hn_idealLowPassFilter;
    elif filterName == "passa-alta":
        return Hn_idealHighPassFilter;
    elif filterName == "rejeita-faixa":
        return Hn_idealBandRejectFilter;
    elif filterName == "passa-faixa":
        return Hn_idealBandPassFilter;
    else:
        return None;


def takeFilterAndWindow(initalN, finalN, M, filterName, window, Wc1, Wc2=None, beta=None):
    filterFunction = takeFilter(filterName);
    windowFunction = takeWindow(window);
    Hn_Idealfilter = [];
    Wn_window = [];
    Hn_FinalFilter = [];
    for n in range(initalN, finalN):
        #taking filter value in position n
        if filterName == "passa-faixa" or filterName == "rejeita-faixa":
            Hn_result = filterFunction(n, Wc1, Wc2);
        else:
            Hn_result = filterFunction(n, Wc1);
        #taking window value in position n 
        if window == "kaiser":
            Wn_result = windowFunction(n, M, beta);
        else:
            Wn_result = windowFunction(n, M)
        #saving the h(n) value of the ideal filter 
        Hn_Idealfilter.append(Hn_result)
        #savig the w(n) value of the window
        Wn_window.append(Wn_result)
        #saving the final value of the filter
        Hn_FinalFilter.append(Hn_result * Wn_result);
    return (Hn_FinalFilter, Hn_Idealfilter, Wn_window);


N_initial = -20;
N_final = 20;
filter_name = "passa-baixa"
M = 5
window = "retangular"
Wc1 = np.pi/4

(Hn_FinalFilter, Hn_Idealfilter, Wn_window) = takeFilterAndWindow(N_initial, N_final, M, filter_name, window, Wc1);

ara = np.arange(N_initial, N_final);


plt.stem(ara, Hn_FinalFilter, use_line_collection=True);
plt.grid()
plt.show()

plt.stem(ara, Hn_Idealfilter, use_line_collection=True);
plt.grid()
plt.show()

plt.stem(ara, Wn_window, use_line_collection=True);
plt.grid()
plt.show()