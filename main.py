# Parâmetros
valorSeNegativo = "False"
valorSePositivo = "True"

# Arquivos
with open('./treinamento/pesos.txt', 'r') as file:
    w = file.readlines()
    w = [float(i) for i in w]

# Funções
def sinal(valor):
    return 1 if valor >= 0 else -1

def normalizar(valor):
    return 1 if float(valor) == 1 else -1

def somatorioXW(entrada):
    u = w[0] * - 1
    for j in range(len(entrada.split(','))):
        u = u + w[j + 1] * normalizar(entrada.split(',')[j])
    return u

# Fluxo
for i in range(50):
    entrada = input("Digite a entrada: ")
    u = somatorioXW(entrada)
    y = sinal(u)
    if y == 1:
        print(valorSePositivo)
    else:
        print(valorSeNegativo)