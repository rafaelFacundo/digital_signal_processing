
from circularInversion import circularInversion

resultSignal = circularInversion.calculateSignal_form_A_power_n(0.8,0,10);



# its just negative values for "numberOfShift", for a while
def circularShift(signalToShift, numberOfShift):
    signal = signalToShift + signalToShift + signalToShift;
    newInitialIndice = len(signalToShift);
    newInitialIndice += numberOfShift;
    newSignal = signal[newInitialIndice:newInitialIndice+len(signalToShift)]
    
    print(newSignal);   
    return newSignal;



#signalShifted = circularShift(resultSignal[1], -3);
#circularInversion.plotSignal(resultSignal[0], signalShifted);