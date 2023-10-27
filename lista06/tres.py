#primeiro vamos importa a biblioteca numpy para conseguirmos trabalhar 
import numpy as np
import matplotlib.pyplot as plt

# agora vamos definir o nosso período fundamental, que no caso dessa questão é 40 
Periodo_fundamental1 = 40
Periodo_fundamental2 = 80


# precisamos também criar o vetor de amostras, que no caso vai de 0 a N-1
n1 = np.arange(Periodo_fundamental1);
n2 = np.arange(Periodo_fundamental2);


# agora precisamos definir o nosso sinal como está na questão 
# vamos utilizar a função where() do numpy
# onde basicamente estamos definindo o nosso sinal em um certo intervalo especpifico
x1 = np.where((n1 >= 0) & (n1 <= 19), 5 * np.sin(0.1 * np.pi * n1), 0);
x2 = np.where((n2 >= 0) & (n2 <= 39), 5 * np.sin(0.1 * np.pi * n2), 0);

# agora vamos calulcar a DFS usando a fft da biblioteca numpy 
X1 = np.fft.fft(x1);
X2 = np.fft.fft(x2);

# a DFS resultante agora está em X 

# a parte imaginária de X conterá os coeficientes da fase
# podemos encontrar as magnitudes com a função abs() da biblioteca numpy
magnitudes1 = np.abs(X1)
magnitudes2 = np.abs(X2)


#printando as magnitudes 
#print("Magnitudes de da DFS: ");
#print(magnitudes)

# podemos também obter os angulos 
# utilizando a função angle()
fases1 = np.angle(X1);
fases2 = np.angle(X2);


#print("Printando a fase: ")
#print(fases)

#agora vamos plotar 

#primeiro precisamos do vetor de frequências da DFS
frequencias1 = np.fft.fftfreq(Periodo_fundamental1) * np.pi;
frequencias2 = np.fft.fftfreq(Periodo_fundamental2) * np.pi;

#agora vamos plotar 


plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.stem(frequencias1, magnitudes1, markerfmt='ro', linefmt='r-', basefmt=" ", label='Magnitude X1 (N=40)')
plt.title('Magnitude da DFS para X1 (N=40)')
plt.xlabel('Frequência')
plt.ylabel('Magnitude')
plt.grid(True)


plt.subplot(1,2,2)
plt.stem(frequencias2, magnitudes2, markerfmt='bo', linefmt='b-', basefmt=" ", label='Magnitude X2 (N=80)')
plt.title('Magnitude da DFS para X2 (N=80)')
plt.xlabel('Frquencia')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show();

