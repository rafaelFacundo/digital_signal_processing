            
def calcularConvolu(sinal1, sinal2):
        tamanhoListaSinal1 = len(sinal1)
        tamanhoListaSinal2 = len(sinal2)
        resultado = [0] * (tamanhoListaSinal1 + tamanhoListaSinal2 - 1)
    
        for n in range(tamanhoListaSinal1 + tamanhoListaSinal2 - 1):
            soma = 0
            for k in range(max(0, n - tamanhoListaSinal1 + 1), min(n, tamanhoListaSinal2 - 1) + 1):
                soma += sinal1[n - k] * sinal2[k]
            resultado[n] = soma
        
        return resultado

x1n = [1,1]
result1 = calcularConvolu(x1n,x1n)
result2 = calcularConvolu(result1, x1n)
result3 = calcularConvolu(result2, x1n)
print(result3)

#A resposta é [1, 4, 6, 4, 1]