
yCoefici = [1 , 0.75, -0.125];
shifIndY = [0 , 1   , 2];
xCoefici = [1,2,1];
shifIndX = [0,1,2];
xSignal = [0,1,2,3,4,54,56,5,32,10,7]



def applyFilter(Y_coeficients, X_coeficients, shiftIndicesInY, shiftIndicesInX, X_signal, numberOfSamples):
    result = [];
    actualResult = 0
    for n in range(numberOfSamples):
        actualResult = 0
        for x in range(len(X_coeficients)):
            print("for x")
            shift = shiftIndicesInX[x];
            print("n ", n);
            print("shif", shift)
            if n - shift >= 0:
                print("entrei no if")
                print(X_coeficients[x], X_signal[(n-shift)])
                
                actualResult += X_coeficients[x] * X_signal[(n-shift)]
                print("Reusl", actualResult);
                print("=============")
            else:
                break
        for y in range(len(result)):
            
            shiftY = shiftIndicesInY[y];
            if n-shiftY >= 0 and n-shiftY > len(result):
                print("entrei no if de Y +++")
                print(Y_coeficients[y])
                print("=============", (n-shiftY), len(result))
                actualResult += Y_coeficients[y] * result[(n-shiftY)]
            else:
                break
        result.append(actualResult)
    return result

print(applyFilter(yCoefici, xCoefici, shifIndY, shifIndX, xSignal, len(xSignal)));