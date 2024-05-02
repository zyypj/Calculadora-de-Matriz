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

def multiplicar_matrizes(matriz1, matriz2):
    # Verifica se o número de colunas da primeira matriz é igual ao número de linhas da segunda matriz
    if len(matriz1[0]) != len(matriz2):
        print('Não é possível multiplicar as matrizes. O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.')
        return None

    # Inicializa a matriz resultado com zeros
    resultado = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]

    # Multiplica as matrizes
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

# Solicita ao usuário o número de linhas e colunas para a primeira matriz
linhas1 = int(input('Digite o número de linhas da primeira matriz: '))
colunas1 = int(input('Digite o número de colunas da primeira matriz: '))

# Cria a primeira matriz
print('Digite os valores da primeira matriz:')
matriz1 = criar_matriz(linhas1, colunas1)

# Solicita ao usuário o número de linhas e colunas para a segunda matriz
linhas2 = int(input('Digite o número de linhas da segunda matriz: '))
colunas2 = int(input('Digite o número de colunas da segunda matriz: '))

# Cria a segunda matriz
print('Digite os valores da segunda matriz:')
matriz2 = criar_matriz(linhas2, colunas2)

# Solicita ao usuário a operação desejada
operacao = input('Digite a operação desejada (soma, subtração ou multiplicação): ')

# Executa a operação escolhida e imprime o resultado
if operacao.lower() == 'soma' or operacao == '+':
    resultado = somar_matrizes([matriz1, matriz2])
elif operacao.lower() == 'subtração' or operacao == '-':
    resultado = subtrair_matrizes([matriz1, matriz2])
elif operacao.lower() == 'multiplicação' or operacao.lower() == 'multiplicacao' or operacao == '*':
    resultado = multiplicar_matrizes(matriz1, matriz2)
else:
    print('Operação inválida!')
    resultado = None

# Se houver um resultado válido, imprime a matriz resultado
if resultado:
    print('Resultado:')
    for linha in resultado:
        print(linha)