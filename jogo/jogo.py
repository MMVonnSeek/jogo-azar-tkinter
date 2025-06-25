import tkinter as tk
from tkinter import messagebox
from random import choice
from PIL import Image, ImageTk

# Lista com caminhos das imagens (substitua pelos seus arquivos)
imagens = ["img1.png", "img2.png", "img3.png"]

class JogoSorte(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jogo do Sorte")
        self.geometry("300x200")
        self.config(bg="#f0f0f0")

        self.labels = []
        self.fotos = []

        for i in range(3):
            foto = ImageTk.PhotoImage(Image.open(imagens[i]).resize((80, 80)))
            self.fotos.append(foto)
            label = tk.Label(self, image=foto)
            label.grid(row=0, column=i, padx=10, pady=20)
            self.labels.append(label)

        self.btn_jogar = tk.Button(self, text="Jogar", command=self.jogar)
        self.btn_jogar.grid(row=1, column=1, pady=20)

    def jogar(self):
        escolhas = [choice(imagens) for _ in range(3)]
        for i, escolha in enumerate(escolhas):
            img = ImageTk.PhotoImage(Image.open(escolha).resize((80, 80)))
            self.labels[i].config(image=img)
            self.labels[i].image = img  # evitar garbage collection

        if escolhas[0] == escolhas[1] == escolhas[2]:
            messagebox.showinfo("Resultado", "Parabéns! Você ganhou!")
        else:
            messagebox.showinfo("Resultado", "Tente novamente!")

if __name__ == "__main__":
    app = JogoSorte()
    app.mainloop()
