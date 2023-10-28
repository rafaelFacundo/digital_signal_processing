
yCoefici = [0.75, -0.125];
shifIndY = [1   , 2];
xCoefici = [1,2,1];
shifIndX = [0,1,2];
xSignal = [0,1,2,3,4,54,56,5,32,10,7]



def applyFilter(Y_coeficients, X_coeficients, shiftIndicesInY, shiftIndicesInX, X_signal, numberOfSamples):
    result = [];
    actualResult = 0
    for n in range(numberOfSamples):
        print(f"N={n}")
        actualResult = 0
        print("VOU ENTRAR NO FOR DO X")
        for x in range(len(X_coeficients)):
            coeficient = X_coeficients[x];
            shift = shiftIndicesInX[x];
            print("coefici ", coeficient);
            print("shif ", shift);
            if shift <= n:
                print("Shift é menor ")
                indiceToTakeIn_Xsignal = n - shift;
                valueOfTheSignal = X_signal[indiceToTakeIn_Xsignal];
                print("VOU pegar")
                print(f"{coeficient} * X({n}-{shift})({valueOfTheSignal})");
                actualResult += coeficient * valueOfTheSignal;
                print("result ", actualResult)
                print("++++++")
            else:  
                print("parei")
                print("+++++")
                break
        
        print("VOU ENTRAR NO FOR DO y")
        for y in range(len(Y_coeficients)):
            coeficient = Y_coeficients[y];
            shift = shiftIndicesInY[y];
            print("coefici ", coeficient);
            print("shif ", shift);
            if shift <= n and len(result) > 0:
                print("Shift é menor e result é maior q zero ")
                indiceToTakeIn_Ysignal = n - shift;
                valueOfTheSignal = result[indiceToTakeIn_Ysignal];
                print("VOU pegar")
                print(f"{coeficient} * Y({n}-{shift}){valueOfTheSignal}");
                actualResult += coeficient * valueOfTheSignal
                print("result ", actualResult)
                print("=======")
            else:
                print("parei")
                print("=====")
                break;
        result.append(actualResult)
    return result

print(applyFilter(yCoefici, xCoefici, shifIndY, shifIndX, xSignal, len(xSignal)));