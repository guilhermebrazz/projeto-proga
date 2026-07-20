from tkinter import filedialog

from modelo.desenho import Desenho
from visao.view import View
from .estados import (
    EstadoRetangulo,
    EstadoOval,
    EstadoCirculo,
    EstadoLinha,
    EstadoPoligono,
    EstadoRabisco,
)


class Controller:
    def __init__(self, root):
        self.ini_x = None
        self.ini_y = None
        self.fim_x = None
        self.fim_y = None
        self.estado = None
        self.cor_borda = "#000000"
        self.cor_preenchimento = "#ffffff"
        self.pontos = []

        self.desenho = Desenho()
        self.view = View(root, self)

    def _definir_estado(self, estado):
        self.estado = estado
        self.estado.ao_selecionar(self)

    def retangulo(self):
        self._definir_estado(EstadoRetangulo())

    def oval(self):
        self._definir_estado(EstadoOval())

    def circulo(self):
        self._definir_estado(EstadoCirculo())

    def linha(self):
        self._definir_estado(EstadoLinha())

    def rabisco(self):
        self._definir_estado(EstadoRabisco())

    def poligono(self):
        self._definir_estado(EstadoPoligono())

    def escolher_cor_borda(self):
        cor_escolhida = self.view.pedir_cor(self.cor_borda, "Escolha a cor da borda")
        if cor_escolhida is not None:
            self.cor_borda = cor_escolhida
            self.view.atualizar_botao_cor_borda(self.cor_borda)

    def escolher_cor_preenchimento(self):
        cor_escolhida = self.view.pedir_cor(self.cor_preenchimento, "Escolha a cor de preenchimento")
        if cor_escolhida is not None:
            self.cor_preenchimento = cor_escolhida
            self.view.atualizar_botao_cor_preenchimento(self.cor_preenchimento)

    def redesenhar_tudo(self):
        self.view.limpar_canvas()
        self.desenho.desenhar(self.view.canvas)

    def inicio(self, event):
        if self.estado is not None:
            self.estado.inicio(self, event)

    def fim(self, event):
        if self.estado is not None:
            self.estado.mover(self, event)

    def finalizar_figura(self, event):
        if self.estado is not None:
            self.estado.finalizar(self, event)

    def finalizar_poligono(self, event):
        if self.estado is not None:
            self.estado.duplo_clique(self, event)


    def salvar(self):
        caminho = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("Arquivo JSON", "*.json")]
        )
        if caminho:
            self.desenho.salvar(caminho)

    def abrir(self):
        caminho = filedialog.askopenfilename(
            filetypes=[("Arquivo JSON", "*.json")]
        )
        if caminho:
            self.desenho.carregar(caminho)
            self.redesenhar_tudo()