
#a partir da estrutura do filtro podemos chegar na seguinte equação de diferenças
#y(n) = kx(n) + 1,8x(n-1) - 0,9x(n-2) + 2y(n-1) + 0,5y(n-2) 
#para calcular a resposta impulsional vamos aplicar esse filtro ao impulso unitário [1,0,....,0]
#para que a resposta em frequencia seja igual a 1 podemos resolver a seguinte equação
#k + 1,8 - 0,9 + 2 + 0,5 = 1
#k + 3,4 = 1
#k = 1 - 3,4
#k = -2,4

yCoefici = [2, 0.5];
shifIndY = [1, 2];
xCoefici = [-2.4,1.8,-0.9];
shifIndX = [0,1,2];
xSignal = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


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

#A resposta ao impulso é dado pelo resultado abaixo 
print(applyFilter(yCoefici, xCoefici, shifIndY, shifIndX, xSignal, len(xSignal)));