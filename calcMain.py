from fractions import Fraction

class CalculadoraMatrizes:
    def __init__(self):
        self.valores_matriz1 = None
        self.valores_matriz2 = None

    def iniciar(self):
        while True:
            operacao = input("Escolha a operação: soma, subtracao, multiplicacao, divisao, determinante\nOperação: ").strip().lower()
            if operacao in ["soma", "subtracao", "multiplicacao", "divisao"]:
                self.operacoes_com_duas_matrizes(operacao)
            elif operacao == "determinante":
                self.calcular_determinante()
            else:
                print("Operação inválida. Tente novamente.")
    
    def operacoes_com_duas_matrizes(self, operacao):
        linhas1 = int(input("Número de linhas da matriz 1: "))
        colunas1 = int(input("Número de colunas da matriz 1: "))
        self.valores_matriz1 = self.definir_valores_matriz(linhas1, colunas1, 1)
        
        linhas2 = int(input("Número de linhas da matriz 2: "))
        colunas2 = int(input("Número de colunas da matriz 2: "))
        self.valores_matriz2 = self.definir_valores_matriz(linhas2, colunas2, 2)

        if operacao == "multiplicacao" and colunas1 != linhas2:
            print("Erro: O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz para multiplicação.")
            return
        elif operacao == "divisao" and (linhas1 != linhas2 or colunas1 != colunas2):
            print("Erro: As matrizes devem ter o mesmo tamanho para divisão.")
            return

        if operacao == "soma":
            resultado = self.somar_matrizes()
        elif operacao == "subtracao":
            resultado = self.subtrair_matrizes()
        elif operacao == "multiplicacao":
            resultado = self.multiplicar_matrizes()
        elif operacao == "divisao":
            resultado = self.dividir_matrizes()
        
        self.exibir_matriz(resultado)

    def definir_valores_matriz(self, linhas, colunas, matriz_num):
        valores_matriz = [[None for _ in range(colunas)] for _ in range(linhas)]
        print(f"Insira os valores da Matriz {matriz_num} ({linhas}x{colunas}):")
        for i in range(linhas):
            linha = input(f"Linha {i+1}: ").split()
            valores_matriz[i] = [Fraction(valor) for valor in linha]
        return valores_matriz

    def somar_matrizes(self):
        linhas = len(self.valores_matriz1)
        colunas = len(self.valores_matriz1[0])
        resultado = [[self.valores_matriz1[i][j] + self.valores_matriz2[i][j] for j in range(colunas)] for i in range(linhas)]
        return resultado

    def subtrair_matrizes(self):
        linhas = len(self.valores_matriz1)
        colunas = len(self.valores_matriz1[0])
        resultado = [[self.valores_matriz1[i][j] - self.valores_matriz2[i][j] for j in range(colunas)] for i in range(linhas)]
        return resultado

    def multiplicar_matrizes(self):
        linhas = len(self.valores_matriz1)
        colunas = len(self.valores_matriz2[0])
        resultado = [[sum(self.valores_matriz1[i][k] * self.valores_matriz2[k][j] for k in range(len(self.valores_matriz2))) for j in range(colunas)] for i in range(linhas)]
        return resultado

    def dividir_matrizes(self):
        linhas = len(self.valores_matriz1)
        colunas = len(self.valores_matriz1[0])
        resultado = [[self.valores_matriz1[i][j] / self.valores_matriz2[i][j] if self.valores_matriz2[i][j] != 0 else None for j in range(colunas)] for i in range(linhas)]
        return resultado

    def calcular_determinante(self):
        linhas = int(input("Número de linhas da matriz: "))
        colunas = int(input("Número de colunas da matriz: "))

        if linhas != colunas or linhas not in [1, 2, 3]:
            print("Erro: O cálculo do determinante só é suportado para matrizes 1x1, 2x2 e 3x3.")
            return

        valores_matriz = self.definir_valores_matriz(linhas, colunas, '')

        if linhas == 1:
            determinante = valores_matriz[0][0]
        elif linhas == 2:
            determinante = valores_matriz[0][0] * valores_matriz[1][1] - valores_matriz[0][1] * valores_matriz[1][0]
        elif linhas == 3:
            determinante = (valores_matriz[0][0] * valores_matriz[1][1] * valores_matriz[2][2] +
                            valores_matriz[0][1] * valores_matriz[1][2] * valores_matriz[2][0] +
                            valores_matriz[0][2] * valores_matriz[1][0] * valores_matriz[2][1] -
                            valores_matriz[0][2] * valores_matriz[1][1] * valores_matriz[2][0] -
                            valores_matriz[0][0] * valores_matriz[1][2] * valores_matriz[2][1] -
                            valores_matriz[0][1] * valores_matriz[1][0] * valores_matriz[2][2])
        else:
            determinante = None

        print(f"Determinante: {determinante}")

    def exibir_matriz(self, matriz):
        print("Resultado:")
        for linha in matriz:
            print("[" + " ".join(str(valor) for valor in linha) + "]")

# Instancia a aplicação
app = CalculadoraMatrizes()
app.iniciar()