import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from fractions import Fraction

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

        self.operacao_var = tk.StringVar(self)
        self.operacao_var.set("soma")  # Valor padrão

        # Criação dos widgets da interface
        self.criar_widgets()

    def criar_widgets(self):
        # Escolher o tamanho da matriz 1
        ttk.Label(self, text="Tamanho da Matriz 1").pack()
        self.entr_linhas1 = ttk.Entry(self, width=5)
        self.entr_linhas1.pack()
        self.entr_colunas1 = ttk.Entry(self, width=5)
        self.entr_colunas1.pack()
        ttk.Button(self, text="Confirmar", command=self.definir_tamanho_matriz1).pack()

    def definir_tamanho_matriz1(self):
        # Define o tamanho da matriz 1 com base nos valores inseridos pelo usuário
        self.linhas_matriz1 = int(self.entr_linhas1.get())
        self.colunas_matriz1 = int(self.entr_colunas1.get())
        self.valores_matriz1 = [[None for _ in range(self.colunas_matriz1)] for _ in range(self.linhas_matriz1)]

        # Interface para inserir os valores da matriz 1
        self.limpar_widgets()
        ttk.Label(self, text="Insira os valores da Matriz 1").pack()
        self.criar_campos_matriz(self.valores_matriz1)

        ttk.Button(self, text="Próximo", command=self.definir_tamanho_matriz2).pack()

    def definir_tamanho_matriz2(self):
        # Escolher o tamanho da matriz 2
        ttk.Label(self, text="Tamanho da Matriz 2").pack()
        self.entr_linhas2 = ttk.Entry(self, width=5)
        self.entr_linhas2.pack()
        self.entr_colunas2 = ttk.Entry(self, width=5)
        self.entr_colunas2.pack()
        ttk.Button(self, text="Confirmar", command=self.definir_valores_matriz2).pack()

    def definir_valores_matriz2(self):
        # Define o tamanho da matriz 2 com base nos valores inseridos pelo usuário
        self.linhas_matriz2 = int(self.entr_linhas2.get())
        self.colunas_matriz2 = int(self.entr_colunas2.get())
        self.valores_matriz2 = [[None for _ in range(self.colunas_matriz2)] for _ in range(self.linhas_matriz2)]

        # Interface para inserir os valores da matriz 2
        self.limpar_widgets()
        ttk.Label(self, text="Insira os valores da Matriz 2").pack()
        self.criar_campos_matriz(self.valores_matriz2)

        ttk.Button(self, text="Próximo", command=self.escolher_operacao).pack()

    def criar_campos_matriz(self, valores_matriz):
        # Cria campos de entrada para os valores da matriz
        for i in range(len(valores_matriz)):
            frame_linha = ttk.Frame(self)
            frame_linha.pack()
            for j in range(len(valores_matriz[0])):
                entry = ttk.Entry(frame_linha, width=8)  # Increased width to accommodate fractions
                entry.pack(side=tk.LEFT)
                valores_matriz[i][j] = entry

    def escolher_operacao(self):
        # Escolher a operação a ser realizada
        self.limpar_widgets()
        ttk.Label(self, text="Escolha a operação:").pack()
        operacoes = ["soma", "subtração", "multiplicação"]
        ttk.OptionMenu(self, self.operacao_var, self.operacao_var.get(), *operacoes).pack()

        ttk.Button(self, text="Calcular", command=self.calcular).pack()

    def calcular(self):
        # Verifica se as matrizes têm tamanhos compatíveis para a operação escolhida
        if self.operacao_var.get() == "multiplicação":
            if self.colunas_matriz1 != self.linhas_matriz2:
                messagebox.showerror("Erro", "O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz para realizar a multiplicação.")
                return
        else:
            if self.linhas_matriz1 != self.linhas_matriz2 or self.colunas_matriz1 != self.colunas_matriz2:
                messagebox.showerror("Erro", "As matrizes devem ter o mesmo tamanho para realizar esta operação.")
                return

        # Realiza a operação selecionada e exibe o resultado
        if self.operacao_var.get() == "soma":
            resultado = self.somar_matrizes()
        elif self.operacao_var.get() == "subtração":
            resultado = self.subtrair_matrizes()
        elif self.operacao_var.get() == "multiplicação":
            resultado = self.multiplicar_matrizes()
        else:
            resultado = None

        if resultado:
            self.limpar_widgets()
            ttk.Label(self, text="Resultado:").pack()
            for linha in resultado:
                ttk.Label(self, text="[" + "  ".join(str(f) for f in linha) + "]").pack(pady=5, padx=10, anchor="center")
            
            ttk.Label(self, text=f"Ordem da Matriz Resultante: {len(resultado)}x{len(resultado[0])}").pack(pady=5, padx=10, anchor="center")
            
            ttk.Button(self, text="Calcular Novamente", command=self.reiniciar_calculadora).pack()

    def somar_matrizes(self):
        # Realiza a soma das matrizes
        resultado = [[Fraction(0) for _ in range(self.colunas_matriz1)] for _ in range(self.linhas_matriz1)]
        for i in range(self.linhas_matriz1):
            for j in range(self.colunas_matriz1):
                valor1 = Fraction(self.valores_matriz1[i][j].get())
                valor2 = Fraction(self.valores_matriz2[i][j].get())
                resultado[i][j] = valor1 + valor2
        return resultado

    def subtrair_matrizes(self):
        # Realiza a subtração das matrizes
        resultado = [[Fraction(0) for _ in range(self.colunas_matriz1)] for _ in range(self.linhas_matriz1)]
        for i in range(self.linhas_matriz1):
            for j in range(self.colunas_matriz1):
                valor1 = Fraction(self.valores_matriz1[i][j].get())
                valor2 = Fraction(self.valores_matriz2[i][j].get())
                resultado[i][j] = valor1 - valor2
        return resultado

    def multiplicar_matrizes(self):
        # Realiza a multiplicação das matrizes
        resultado = [[Fraction(0) for _ in range(self.colunas_matriz2)] for _ in range(self.linhas_matriz1)]
        for i in range(self.linhas_matriz1):
            for j in range(self.colunas_matriz2):
                for k in range(self.colunas_matriz1):
                    valor1 = Fraction(self.valores_matriz1[i][k].get())
                    valor2 = Fraction(self.valores_matriz2[k][j].get())
                    resultado[i][j] += valor1 * valor2
        return resultado

    def limpar_widgets(self):
        # Limpa os widgets da interface
        for widget in self.winfo_children():
            widget.pack_forget()

    def reiniciar_calculadora(self):
        # Reinicia a calculadora, recriando os widgets iniciais
        self.linhas_matriz1 = None
        self.colunas_matriz1 = None
        self.valores_matriz1 = None

        self.linhas_matriz2 = None
        self.colunas_matriz2 = None
        self.valores_matriz2 = None

        self.operacao_var.set("soma")

        self.limpar_widgets()
        self.criar_widgets()

# Instancia a aplicação
app = CalculadoraMatrizes()
app.mainloop()