from circularShift import circularShift
from circularInversion import circularInversion


def summationOfTwoSignals(signalOne, SignalTwo):
    result = 0;
    for x in range(len(signalOne)):
        result += signalOne[x] * SignalTwo[x];
    return result;

def circularConvolution(signalOne, signalTwo):
    result = []
    signalTwoInverted = circularInversion.invert_a_signal(signalTwo, 1, len(signalTwo)-1);
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


print(callCircularConvolution([1,2,3,4,5,6,7], [7,8,9,7]))