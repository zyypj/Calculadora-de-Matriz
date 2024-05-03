import tkinter as tk
from tkinter import messagebox

class CalculadoraMatrizes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Matrizes")
        self.geometry("400x400")

        # Variáveis para armazenar informações sobre as matrizes e operação
        self.linhas_matriz1 = None
        self.colunas_matriz1 = None
        self.valores_matriz1 = None

        self.linhas_matriz2 = None
        self.colunas_matriz2 = None
        self.valores_matriz2 = None

        self.operacao = None

        # Criação dos widgets da interface
        self.criar_widgets()

    def criar_widgets(self):
        # Escolher o tamanho da matriz 1
        tk.Label(self, text="Tamanho da Matriz 1").pack()
        self.entr_linhas1 = tk.Entry(self, width=5)
        self.entr_linhas1.pack()
        self.entr_colunas1 = tk.Entry(self, width=5)
        self.entr_colunas1.pack()
        tk.Button(self, text="Confirmar", command=self.definir_tamanho_matriz1).pack()

    def definir_tamanho_matriz1(self):
        # Define o tamanho da matriz 1 com base nos valores inseridos pelo usuário
        self.linhas_matriz1 = int(self.entr_linhas1.get())
        self.colunas_matriz1 = int(self.entr_colunas1.get())
        self.valores_matriz1 = [[None for _ in range(self.colunas_matriz1)] for _ in range(self.linhas_matriz1)]

        # Interface para inserir os valores da matriz 1
        self.limpar_widgets()
        tk.Label(self, text="Insira os valores da Matriz 1").pack()
        self.criar_campos_matriz(self.valores_matriz1)

        tk.Button(self, text="Próximo", command=self.definir_tamanho_matriz2).pack()

    def definir_tamanho_matriz2(self):
        # Escolher o tamanho da matriz 2
        tk.Label(self, text="Tamanho da Matriz 2").pack()
        self.entr_linhas2 = tk.Entry(self, width=5)
        self.entr_linhas2.pack()
        self.entr_colunas2 = tk.Entry(self, width=5)
        self.entr_colunas2.pack()
        tk.Button(self, text="Confirmar", command=self.definir_valores_matriz2).pack()

    def definir_valores_matriz2(self):
        # Define o tamanho da matriz 2 com base nos valores inseridos pelo usuário
        self.linhas_matriz2 = int(self.entr_linhas2.get())
        self.colunas_matriz2 = int(self.entr_colunas2.get())
        self.valores_matriz2 = [[None for _ in range(self.colunas_matriz2)] for _ in range(self.linhas_matriz2)]

        # Interface para inserir os valores da matriz 2
        self.limpar_widgets()
        tk.Label(self, text="Insira os valores da Matriz 2").pack()
        self.criar_campos_matriz(self.valores_matriz2)

        tk.Button(self, text="Próximo", command=self.escolher_operacao).pack()

    def criar_campos_matriz(self, valores_matriz):
        # Cria campos de entrada para os valores da matriz
        for i in range(len(valores_matriz)):
            frame_linha = tk.Frame(self)
            frame_linha.pack()
            for j in range(len(valores_matriz[0])):
                entry = tk.Entry(frame_linha, width=5)
                entry.pack(side=tk.LEFT)
                valores_matriz[i][j] = entry

    def escolher_operacao(self):
        # Escolher a operação a ser realizada
        self.limpar_widgets()
        tk.Label(self, text="Escolha a operação:").pack()
        self.operacao = tk.StringVar(self)
        self.operacao.set("soma")  # Valor padrão
        operacoes = ["soma", "subtração", "multiplicação"]
        tk.OptionMenu(self, self.operacao, *operacoes).pack()

        tk.Button(self, text="Calcular", command=self.calcular).pack()

    def calcular(self):
        # Verifica se as matrizes têm tamanhos compatíveis para a operação escolhida
        if self.linhas_matriz1 != self.linhas_matriz2 or self.colunas_matriz1 != self.colunas_matriz2:
            tk.messagebox.showerror("Erro", "As matrizes devem ter o mesmo tamanho para realizar esta operação.")
            return

        # Realiza a operação selecionada e exibe o resultado
        if self.operacao.get() == "soma":
            resultado = self.somar_matrizes()
        elif self.operacao.get() == "subtração":
            resultado = self.subtrair_matrizes()
        elif self.operacao.get() == "multiplicação":
            resultado = self.multiplicar_matrizes()
        else:
            resultado = None

        if resultado:
            self.limpar_widgets()
            tk.Label(self, text="Resultado:").pack()
            for linha in resultado:
                tk.Label(self, text=linha).pack()

    def somar_matrizes(self):
        # Realiza a soma das matrizes
        resultado = [[0 for _ in range(self.colunas_matriz1)] for _ in range(self.linhas_matriz1)]
        for i in range(self.linhas_matriz1):
            for j in range(self.colunas_matriz1):
                valor1 = float(self.valores_matriz1[i][j].get())
                valor2 = float(self.valores_matriz2[i][j].get())
                resultado[i][j] = valor1 + valor2
        return resultado

    def subtrair_matrizes(self):
        # Realiza a subtração das matrizes
        resultado = [[0 for _ in range(self.colunas_matriz1)] for _ in range(self.linhas_matriz1)]
        for i in range(self.linhas_matriz1):
            for j in range(self.colunas_matriz1):
                valor1 = float(self.valores_matriz1[i][j].get())
                valor2 = float(self.valores_matriz2[i][j].get())
                resultado[i][j] = valor1 - valor2
        return resultado

    def multiplicar_matrizes(self):
        # Realiza a multiplicação das matrizes
        resultado = [[0 for _ in range(self.colunas_matriz2)] for _ in range(self.linhas_matriz1)]
        for i in range(self.linhas_matriz1):
            for j in range(self.colunas_matriz2):
                for k in range(self.colunas_matriz1):
                    valor1 = float(self.valores_matriz1[i][k].get())
                    valor2 = float(self.valores_matriz2[k][j].get())
                    resultado[i][j] += valor1 * valor2
        return resultado

    def limpar_widgets(self):
        # Limpa os widgets da interface
        for widget in self.winfo_children():
            widget.pack_forget()

# Instancia a aplicação
app = CalculadoraMatrizes()
app.mainloop()