import matplotlib.pyplot as plt
import math

def calculateSignal_form_A_power_n(a_factor, start, end):
    x_indiceArray = []
    y_indiceArray = []
    resultEachIteration = 0
    for x in range(start, end+1):
        x_indiceArray.append(x);
        resultEachIteration = math.pow(a_factor, x);
        y_indiceArray.append(resultEachIteration)
    return (x_indiceArray, y_indiceArray)

def plotSignal(x_indiceArray, y_indiceArray):
    plt.stem(x_indiceArray, y_indiceArray,markerfmt='ro', basefmt=' ', linefmt='-r')
    plt.tight_layout()
    plt.show()

def invert_a_signal(signalToInvert, start, end):
    signal = signalToInvert
    temporaryNumber = 0
    limit = math.floor(end/2);
    while start <= limit:
        temporaryNumber = signal[start];
        signal[start] = signal[end];
        signal[end] = temporaryNumber;
        start += 1;
        end -= 1;
    return signal
    
# resultOfsignalFormula = calculateSignal_form_A_power_n(0.8, 0,10);
# y_indiceArray_circularInvertion = invert_a_signal(resultOfsignalFormula[1], 1, len(resultOfsignalFormula[1])-1 )
# plotSignal(resultOfsignalFormula[0], y_indiceArray_circularInvertion)


