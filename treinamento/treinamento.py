import random

# Parâmetros:
taxaAprendizagem = 0.01
maxEpocas = 10000
precisao = 0.00001

# Entradas
with open('./entradas.txt', 'r') as file:
    arqEntradas = file.readlines()

numeroEntradas = len(arqEntradas[0].split(','))

# Saídas
with open('./saidas.txt', 'r') as file:
    arqSaidas = file.readlines()

# Funções
def preencherW():
    resultado = []
    for i in range(numeroEntradas + 1):
        resultado.append(random.uniform(0.001, 0.9))
    return resultado

def somatorioXW(i):
    u = w[0] * -1
    for j in range(numeroEntradas):
        u = u + w[j + 1] * float(arqEntradas[i].split(',')[j])
    return u

def EQM(w):
    p = len(arqEntradas)
    eqm = 0
    for i in range(p):
        # u <- wT . xK ou somatório dos x.w
        u = somatorioXW(i)
        eqm = eqm + ((float(arqSaidas[i]) - u) ** 2)
    eqm = eqm / p
    return eqm

# Fluxo
w = preencherW()
epocas = 0
eqmAnterior = 0
eqmatual = 1
print(f"Pesos iniciais: {w}")
while abs(eqmatual - eqmAnterior) > precisao and epocas < maxEpocas:
    eqmAnterior = EQM(w)
    for i in range(len(arqEntradas)):
        u = somatorioXW(i)
        # Limiar de ativação
        w[0] = w[0] + (taxaAprendizagem * (float(arqSaidas[i]) - u) * -1)
        # Pesos sinápticos
        for j in range(numeroEntradas):
            w[j + 1] = w[j + 1] + taxaAprendizagem * (float(arqSaidas[i]) - u) * float(arqEntradas[i].split(',')[j])
    epocas = epocas + 1
    print(f"Fim da época {epocas}.")
    eqmatual = EQM(w)
    print(f"Erro quadrático médio atual: {eqmatual}")

print(f"Pesos finais: {w}")
with open('./pesos.txt', 'w') as file:
    for i in range(len(w)):
        file.write(str(w[i]) + '\n')

if(epocas == maxEpocas):
    print("A rede não convergiu.")
else:
    print(f"A rede convergiu em {epocas} épocas.")
            



        