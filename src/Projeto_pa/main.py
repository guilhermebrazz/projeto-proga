import tkinter as tk
from tkinter import colorchooser
from figuras import *

class Paint:

    def __init__(self, root):

        self.ini_x = None
        self.ini_y = None
        self.fim_x = None
        self.fim_y = None
        self.forma = None
        self.cor_borda = "#000000"
        self.cor_preenchimento = "#ffffff"
        self.figuras = []
        self.pontos = []  # pontos do polígono sendo desenhado

        # Menu de formas
        self.barra = tk.Frame(root)
        self.barra.pack()
        self.btn_retangulo = tk.Button(self.barra, text="Retângulo", command=self.retangulo)
        self.btn_retangulo.pack(side="left")

        self.btn_oval = tk.Button(self.barra, text="Oval", command=self.oval)
        self.btn_oval.pack(side="left")

        self.btn_circulo = tk.Button(self.barra, text="Círculo", command=self.circulo)
        self.btn_circulo.pack(side="left")

        self.btn_poligono = tk.Button(self.barra, text="Polígono", command=self.poligono)
        self.btn_poligono.pack(side="left")

        tk.Label(self.barra, text=" Borda: ").pack(side="left")
        self.botao_cor_borda = tk.Button(
            self.barra, text="   ", bg=self.cor_borda, relief=tk.RIDGE, width=3,
            command=self.escolher_cor_borda
        )
        self.botao_cor_borda.pack(side="left", padx=5)

        tk.Label(self.barra, text=" Preenchimento: ").pack(side="left")
        self.botao_cor_preenchimento = tk.Button(
            self.barra, text="   ", bg=self.cor_preenchimento, relief=tk.RIDGE, width=3,
            command=self.escolher_cor_preenchimento
        )
        self.botao_cor_preenchimento.pack(side="left", padx=5)

        # Configurações do canvas (parte que desenha)
        self.canvas = tk.Canvas(root, bg="white", width=600, height=600)
        self.canvas.pack()

        self.canvas.bind("<ButtonPress-1>", self.inicio)
        self.canvas.bind("<B1-Motion>", self.fim)
        self.canvas.bind("<ButtonRelease-1>", self.finalizar_figura)
        self.canvas.bind("<Double-Button-1>", self.finalizar_poligono)

    # captura a forma escolhida quando é clicada no menu
    def retangulo(self):
        self.forma = "retangulo"

    def oval(self):
        self.forma = "oval"

    def circulo(self):
        self.forma = "circulo"

    def poligono(self):
        self.forma = "poligono"
        self.pontos = []

    def escolher_cor_borda(self):
        resultado = colorchooser.askcolor(color=self.cor_borda, title="Escolha a cor da borda")
        cor_escolhida = resultado[1]
        if cor_escolhida is not None:
            self.cor_borda = cor_escolhida
            self.botao_cor_borda.config(bg=self.cor_borda)

    def escolher_cor_preenchimento(self):
        resultado = colorchooser.askcolor(color=self.cor_preenchimento, title="Escolha a cor de preenchimento")
        cor_escolhida = resultado[1]
        if cor_escolhida is not None:
            self.cor_preenchimento = cor_escolhida
            self.botao_cor_preenchimento.config(bg=self.cor_preenchimento)

    def inicio(self, event):
        if self.forma == "poligono":
            self.pontos.append((event.x, event.y))
            self.redesenhar_tudo()
            self.desenhar_preview_poligono()
            return

        self.ini_x = event.x
        self.ini_y = event.y

    def criar_figura(self):
        if self.forma == "oval":
            return Oval(self.ini_x, self.ini_y, self.fim_x, self.fim_y,
                        self.cor_borda, self.cor_preenchimento)
        elif self.forma == "retangulo":
            return Retangulo(self.ini_x, self.ini_y, self.fim_x, self.fim_y,
                              self.cor_borda, self.cor_preenchimento)
        elif self.forma == "circulo":
            return Circulo(self.ini_x, self.ini_y, self.fim_x, self.fim_y,
                            self.cor_borda, self.cor_preenchimento)
        return None

    def redesenhar_tudo(self):
        self.canvas.delete("all")
        for figura in self.figuras:
            figura.desenhar(self.canvas)

    def desenhar_preview_poligono(self):
        for (x, y) in self.pontos:
            self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill=self.cor_borda)
        if len(self.pontos) >= 2:
            self.canvas.create_line(self.pontos, fill=self.cor_borda)

    def fim(self, event):
        if self.forma == "poligono":
            return

        self.fim_x = event.x
        self.fim_y = event.y

        figura_atual = self.criar_figura()

        if figura_atual is not None:
            self.redesenhar_tudo()
            figura_atual.desenhar(self.canvas)

    def finalizar_figura(self, event):
        if self.forma == "poligono":
            return

        self.fim_x = event.x
        self.fim_y = event.y

        figura_atual = self.criar_figura()
        if figura_atual is not None:
            self.figuras.append(figura_atual)
            self.redesenhar_tudo()

    def finalizar_poligono(self, event):
        if self.forma == "poligono" and len(self.pontos) >= 3:
            figura_atual = Poligono(self.pontos, self.cor_borda, self.cor_preenchimento)
            self.figuras.append(figura_atual)
            self.pontos = []
            self.redesenhar_tudo()


# Configurações da interface
root = tk.Tk()
root.title('Projeto Paint')

obj = Paint(root)

root.mainloop()