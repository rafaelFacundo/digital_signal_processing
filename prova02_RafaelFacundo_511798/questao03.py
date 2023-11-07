import math

def circularShift(signalToShift, numberOfShift):
    signal = signalToShift + signalToShift + signalToShift;
    newInitialIndice = len(signalToShift);
    newInitialIndice += numberOfShift;
    newSignal = signal[newInitialIndice:newInitialIndice+len(signalToShift)]
    return newSignal;

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

def summationOfTwoSignals(signalOne, SignalTwo):
    result = 0;
    for x in range(len(signalOne)):
        result += signalOne[x] * SignalTwo[x];
    return result;

def circularConvolution(signalOne, signalTwo):
    result = []
    signalTwoInverted = invert_a_signal(signalTwo, 1, len(signalTwo)-1);
    for x in range(len(signalTwo)):
        sumResult = summationOfTwoSignals(signalOne, signalTwoInverted);
        result.append(sumResult);
        signalTwoInverted = circularShift(signalTwoInverted, -1);
    return result;


def callCircularConvolution(signalOne, signalTwo):
    lenghtDifference = len(signalOne) - len(signalTwo)
    if lenghtDifference > 0:
        arrayOfZeros = [0] * lenghtDifference;
        signalTwo = signalTwo + arrayOfZeros;
    elif lenghtDifference < 0:
        arrayOfZeros = [0] * lenghtDifference;
        signalOne = signalOne + arrayOfZeros;
    return circularConvolution(signalOne, signalTwo);

#LETRA A - X1 = [1,1,1,1]; X2 = [1, sqrt(2)/2, 0, -sqrt(2)/2, -1, -sqrt(2)/2]
print("= RESPOSTA LETRA A: ") # [0.2928932188134524, 1.7071067811865475, 1.7071067811865475, 1.0, -0.9999999999999999, -2.414213562373095, -2.414213562373095, -1.7071067811865475]
print(circularConvolution([1,1,1,1,0,0,0,0],[1, math.sqrt(2)/2, 0, -1 * math.sqrt(2)/2, -1, -1 * math.sqrt(2)/2, 0,0] ))

#LETRA B - 
lis = [0] * 16;
x1 = []
for n in range(0,16):
    x1.append(math.cos( (2 * math.pi * n )/ 32))
x1 = x1 + lis

x2 = []
for n in range(0,16):
    x2.append(math.sin( (2 * math.pi * n )/ 32))
x2 = x2 + lis
print("= RESPOSTA LETRA B: ")
print(circularConvolution(x1,x2))


#LETRA C - X1 = [1,-1,1,-1]; X2 = [1,0,-1,0]; N = 5
print("= RESPOSTA LETRA C: ") # [2, -1, 0, 0, -1]
print(circularConvolution([1,-1,1,-1,0], [1,0,-1,0,0]))

print("+++++")



