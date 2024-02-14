import tkinter as tk
from tkinter import messagebox
import random

class JogoForcaGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Forca")
        
        self.palavra = self.escolher_palavra()
        self.palavra_oculta = ['_'] * len(self.palavra)
        self.tentativas_maximas = 6
        self.tentativas = 0
        self.letras_erradas = []

        self.criar_interface()

    def escolher_palavra(self):
        palavras = ["python", "programacao", "computador", "desenvolvimento", "inteligencia"]
        return random.choice(palavras)

    def criar_interface(self):
        self.label_forca = tk.Label(self.master, text="")
        self.label_forca.pack()

        self.label_palavra = tk.Label(self.master, text="Palavra: " + " ".join(self.palavra_oculta))
        self.label_palavra.pack()

        self.label_letras_erradas = tk.Label(self.master, text="Letras erradas: ")
        self.label_letras_erradas.pack()

        self.entry_palpite = tk.Entry(self.master)
        self.entry_palpite.pack()

        self.botao_palpite = tk.Button(self.master, text="Palpite", command=self.verificar_palpite)
        self.botao_palpite.pack()

        self.botao_sair = tk.Button(self.master, text="Sair", command=self.master.destroy)
        self.botao_sair.pack()

        # Configurando o botão ENTER como atalho para o palpite
        self.master.bind('<Return>', lambda event=None: self.verificar_palpite())

        self.atualizar_interface()

    def exibir_forca(self):
        forca = [
            """
             ------
             |    |
             |
             |
             |
             |
            ---
            """
            ,
            """
             ------
             |    |
             |    O
             |
             |
             |
            ---
            """
            ,
            """
             ------
             |    |
             |    O
             |    |
             |
             |
            ---
            """
            ,
            """
             ------
             |    |
             |    O
             |   /|
             |
             |
            ---
            """
            ,
            """
             ------
             |    |
             |    O
             |   /|\\
             |
             |
            ---
            """
            ,
            """
             ------
             |    |
             |    O
             |   /|\\
             |   /
             |
            ---
            """
            ,
            """
             ------
             |    |
             |    O
             |   /|\\
             |   / \\
             |
            ---
            """
        ]
        return forca[self.tentativas]

    def verificar_palpite(self):
        palpite = self.entry_palpite.get().lower()

        if palpite.isalpha() and len(palpite) == 1:
            if palpite in self.palavra:
                for i in range(len(self.palavra)):
                    if self.palavra[i] == palpite:
                        self.palavra_oculta[i] = palpite
            else:
                self.letras_erradas.append(palpite)
                self.tentativas += 1

            if "_" not in self.palavra_oculta:
                messagebox.showinfo("Parabéns!", "Você acertou a palavra: " + self.palavra)
                self.reiniciar_jogo()

            if self.tentativas == self.tentativas_maximas:
                messagebox.showinfo("Fim de jogo", "Você perdeu! A palavra era: " + self.palavra)
                self.reiniciar_jogo()
        else:
            messagebox.showwarning("Entrada inválida", "Por favor, digite uma única letra.")

        self.entry_palpite.delete(0, tk.END)  # Limpar a entrada
        self.atualizar_interface()

    def atualizar_interface(self):
        self.label_forca["text"] = self.exibir_forca()
        self.label_palavra["text"] = "Palavra: " + " ".join(self.palavra_oculta)
        self.label_letras_erradas["text"] = "Letras erradas: " + " ".join(self.letras_erradas)

    def reiniciar_jogo(self):
        self.palavra = self.escolher_palavra()
        self.palavra_oculta = ['_'] * len(self.palavra)
        self.tentativas = 0
        self.letras_erradas = []
        self.atualizar_interface()

if __name__ == "__main__":
    root = tk.Tk()
    jogo_forca = JogoForcaGUI(root)
    root.mainloop()
