import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")

        # Variáveis
        self.tabuleiro = [None] * 9  # Representa as 9 posições do tabuleiro
        self.jogador = "X"  # Começa com o jogador X

        # Criação dos botões do tabuleiro
        self.botoes = []
        for i in range(9):
            botao = tk.Button(self.root, text="", font=("Arial", 20), width=5, height=2, command=lambda i=i: self.jogar(i))
            botao.grid(row=i//3, column=i%3)
            self.botoes.append(botao)

        # Botão de reiniciar o jogo
        self.reiniciar_btn = tk.Button(self.root, text="Reiniciar Jogo", font=("Arial", 15), command=self.reiniciar)
        self.reiniciar_btn.grid(row=3, column=0, columnspan=3)

    def jogar(self, pos):
        if self.tabuleiro[pos] is None:  # Verifica se a posição está vazia
            self.tabuleiro[pos] = self.jogador
            self.botoes[pos].config(text=self.jogador)
            if self.checar_vitoria():
                messagebox.showinfo("Vitória", f"Jogador {self.jogador} venceu!")
                self.reiniciar()
            elif None not in self.tabuleiro:
                messagebox.showinfo("Empate", "O jogo empatou!")
                self.reiniciar()
            else:
                self.jogador = "O" if self.jogador == "X" else "X"  # Alterna o jogador

    def checar_vitoria(self):
        # Checa as linhas, colunas e diagonais
        for i in range(3):
            if self.tabuleiro[i*3] == self.tabuleiro[i*3+1] == self.tabuleiro[i*3+2] != None:
                return True
            if self.tabuleiro[i] == self.tabuleiro[i+3] == self.tabuleiro[i+6] != None:
                return True
        if self.tabuleiro[0] == self.tabuleiro[4] == self.tabuleiro[8] != None:
            return True
        if self.tabuleiro[2] == self.tabuleiro[4] == self.tabuleiro[6] != None:
            return True
        return False

    def reiniciar(self):
        self.tabuleiro = [None] * 9
        for botao in self.botoes:
            botao.config(text="")
        self.jogador = "X"

# Criação da janela principal
root = tk.Tk()
jogo = JogoDaVelha(root)
root.mainloop()
