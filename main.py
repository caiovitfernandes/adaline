# Parâmetros
valorSeNegativo = "False"
valorSePositivo = "True"

# Arquivos
with open('./treinamento/pesos.txt', 'r') as file:
    w = file.readlines()
    w = [float(i) for i in w]

# Funções
def degrau(valor):
    return 1 if valor >= 0 else 0

def somatorioXW(entrada):
    u = 0
    for j in range(len(entrada.split(','))):
        u = u + w[j + 1] * float(entrada.split(',')[j])
    return u

# Fluxo
for i in range(50):
    entrada = input("Digite a entrada: ")
    # Limiar de ativação
    u = w[0] * -1;
    u = u + somatorioXW(entrada)
    print(f"u = {u}")
    y = degrau(u)
    if y == 1:
        print(valorSePositivo)
    else:
        print(valorSeNegativo)