import random

# Parâmetros:
taxaAprendizagem = 0.1
maxEpocas = 250000
precisao = 0.000001

# Entradas
with open('./entradas.txt', 'r') as file:
    arqEntradas = file.readlines()

numeroEntradas = len(arqEntradas[0].split(','))

# Saídas
with open('./saidas.txt', 'r') as file:
    arqSaidas = file.readlines()

# Funções
def sinal(valor):
    return 1 if valor >= 0 else -1

def preencherW():
    resultado = []
    for i in range(numeroEntradas):
        resultado.append(random.uniform(0, 1))
    return resultado

def somatorioXW(i, w):
    u = 0
    valores = arqEntradas[i].split(',')
    for j in range(numeroEntradas):
        u = u + (w[j] * float(valores[j]))
    return u

def EQM(w):
    p = len(arqEntradas)
    eqm = 0
    for i in range(p):
        # u <- wT . xK ou somatório dos x.w
        u = somatorioXW(i, w)
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
        u = somatorioXW(i, w)
        # Pesos sinápticos
        for j in range(numeroEntradas):
            entrada = float(arqEntradas[i].split(',')[j])
            w[j] = w[j] + (taxaAprendizagem * (float(arqSaidas[i]) - u) * entrada)
    epocas = epocas + 1
    eqmatual = EQM(w)

print(f"Pesos finais: {w}")
with open('./pesos.txt', 'w') as file:
    for i in range(len(w)):
        file.write(str(w[i]) + '\n')

if(epocas == maxEpocas):
    print("A rede não convergiu.")
else:
    print(f"A rede convergiu em {epocas} épocas.")
        