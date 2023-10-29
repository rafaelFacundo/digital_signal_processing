
yCoefici = [0.75, -0.125];
shifIndY = [1, 2];
xCoefici = [1,2,1];
shifIndX = [0,1,2];
xSignal = [0,1,2,3,4,54,56,5,32,10,7]



def applyFilter(Y_coeficients, X_coeficients, shiftIndicesInY, shiftIndicesInX, X_signal, numberOfSamples):
    result = [];
    actualResult = 0
    for n in range(numberOfSamples):
        actualResult = 0
        for x in range(len(X_coeficients)):
            coeficient = X_coeficients[x];
            shift = shiftIndicesInX[x];
            if shift <= n:
                indiceToTakeIn_Xsignal = n - shift;
                valueOfTheSignal = X_signal[indiceToTakeIn_Xsignal];
                actualResult += coeficient * valueOfTheSignal;
            else:
                break
        for y in range(len(Y_coeficients)):
            coeficient = Y_coeficients[y];
            shift = shiftIndicesInY[y];
            if shift <= n and len(result) > 0:
                indiceToTakeIn_Ysignal = n - shift;
                valueOfTheSignal = result[indiceToTakeIn_Ysignal];
                actualResult += coeficient * valueOfTheSignal
            else:
                break;
        result.append(actualResult)
    return result

print(applyFilter(yCoefici, xCoefici, shifIndY, shifIndX, xSignal, len(xSignal)));