def criar_matriz(linhas, colunas):
    # Cria uma matriz vazia
    matriz = []
    # Para cada linha na matriz
    for l in range(linhas):
        linha = []
        # Para cada coluna na linha
        for c in range(colunas):
            # Pede ao usuário um valor para a posição [l, c] e adiciona à linha
            valor = float(input(f'Digite o valor para a posição [{l}, {c}]: '))
            linha.append(valor)
        # Adiciona a linha à matriz
        matriz.append(linha)
    # Retorna a matriz preenchida
    return matriz

def somar_matrizes(matrizes):
    # Inicializa uma matriz vazia para armazenar o resultado da soma
    resultado = [[0 for _ in range(len(matrizes[0][0]))] for _ in range(len(matrizes[0]))]

    # Para cada matriz
    for matriz in matrizes:
        # Para cada linha na matriz
        for l in range(len(matriz)):
            # Para cada coluna na linha
            for c in range(len(matriz[0])):
                # Soma os valores das matrizes e adiciona ao resultado
                resultado[l][c] += matriz[l][c]
    # Retorna a matriz resultado
    return resultado

def subtrair_matrizes(matrizes):
    # Inicializa uma matriz vazia para armazenar o resultado da subtração
    resultado = [[0 for _ in range(len(matrizes[0][0]))] for _ in range(len(matrizes[0]))]
    # Para cada matriz
    for matriz in matrizes:
        # Para cada linha na matriz
        for l in range(len(matriz)):
            # Para cada coluna na linha
            for c in range(len(matriz[0])):
                # Subtrai os valores das matrizes e adiciona ao resultado
                resultado[l][c] -= matriz[l][c]
    # Retorna a matriz resultado
    return resultado

# Solicita ao usuário o número de matrizes
num_matrizes = int(input('Digite o número de matrizes que deseja somar/subtrair: '))
# Solicita ao usuário o número de linhas e colunas para as matrizes
linhas = int(input('Digite o número de linhas das matrizes: '))
colunas = int(input('Digite o número de colunas das matrizes: '))

# Inicializa uma lista vazia para armazenar as matrizes
matrizes = []
# Para cada matriz
for _ in range(num_matrizes):
    print(f'Digite os valores da matriz {_ + 1}:')
    matriz = criar_matriz(linhas, colunas)
    matrizes.append(matriz)

# Solicita ao usuário a operação desejada
operacao = input('Digite a operação desejada (soma/subtração): ')

# Executa a operação de soma ou subtração e imprime o resultado
if operacao.lower() == 'soma' or operacao == '+':
    resultado = somar_matrizes(matrizes)
elif operacao.lower() == 'subtração' or operacao == '-':
    resultado = subtrair_matrizes(matrizes)
else:
    print('Operação inválida!')
    resultado = None

# Se houver um resultado válido, imprime a matriz resultado
if resultado:
    print('Resultado:')
    for linha in resultado:
        print(linha)