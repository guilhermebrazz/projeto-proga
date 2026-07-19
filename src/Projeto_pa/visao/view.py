import tkinter as tk
from tkinter import colorchooser


class View:
    def __init__(self, root, controller):
        self.controller = controller

        self.barra = tk.Frame(root)
        self.barra.pack()

        self.btn_retangulo = tk.Button(self.barra, text="Retângulo", command=self.controller.retangulo)
        self.btn_retangulo.pack(side="left")

        self.btn_oval = tk.Button(self.barra, text="Oval", command=self.controller.oval)
        self.btn_oval.pack(side="left")

        self.btn_circulo = tk.Button(self.barra, text="Círculo", command=self.controller.circulo)
        self.btn_circulo.pack(side="left")

        self.btn_poligono = tk.Button(self.barra, text="Polígono", command=self.controller.poligono)
        self.btn_poligono.pack(side="left")

        self.btn_linha = tk.Button(self.barra, text="Linha", command=self.controller.linha)
        self.btn_linha.pack(side="left")

        self.btn_rabisco = tk.Button(self.barra, text="Rabisco", command=self.controller.rabisco)
        self.btn_rabisco.pack(side="left")

        self.btn_salvar = tk.Button(self.barra, text="Salvar", command=self.controller.salvar)
        self.btn_salvar.pack(side="left")

        self.btn_abrir = tk.Button(self.barra, text="Abrir", command=self.controller.abrir)
        self.btn_abrir.pack(side="left")

        tk.Label(self.barra, text=" Borda: ").pack(side="left")
        self.botao_cor_borda = tk.Button(
            self.barra, text="   ", bg="#000000", relief=tk.RIDGE, width=3,
            command=self.controller.escolher_cor_borda
        )
        self.botao_cor_borda.pack(side="left", padx=5)

        tk.Label(self.barra, text=" Preenchimento: ").pack(side="left")
        self.botao_cor_preenchimento = tk.Button(
            self.barra, text="   ", bg="#ffffff", relief=tk.RIDGE, width=3,
            command=self.controller.escolher_cor_preenchimento
        )
        self.botao_cor_preenchimento.pack(side="left", padx=5)

        self.canvas = tk.Canvas(root, bg="white", width=600, height=600)
        self.canvas.pack()

        self.canvas.bind("<ButtonPress-1>", self.controller.inicio)
        self.canvas.bind("<B1-Motion>", self.controller.fim)
        self.canvas.bind("<ButtonRelease-1>", self.controller.finalizar_figura)
        self.canvas.bind("<Double-Button-1>", self.controller.finalizar_poligono)

    def pedir_cor(self, cor_atual, titulo):
        resultado = colorchooser.askcolor(color=cor_atual, title=titulo)
        return resultado[1]

    def atualizar_botao_cor_borda(self, cor):
        self.botao_cor_borda.config(bg=cor)

    def atualizar_botao_cor_preenchimento(self, cor):
        self.botao_cor_preenchimento.config(bg=cor)

    def limpar_canvas(self):
        self.canvas.delete("all")

    def desenhar_preview_poligono(self, pontos, cor_borda):
        for (x, y) in pontos:
            self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill=cor_borda)
        if len(pontos) >= 2:
            self.canvas.create_line(pontos, fill=cor_borda)