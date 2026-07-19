from modelo import Figura, Oval, Retangulo, Circulo, Linha, Poligono, Rabisco
from modelo.desenho import Desenho
from visao.view import View

class Controller:
    def __init__(self, root):
        self.ini_x = None
        self.ini_y = None
        self.fim_x = None
        self.fim_y = None
        self.forma = None
        self.cor_borda = "#000000"
        self.cor_preenchimento = "#ffffff"
        self.pontos = []

        self.desenho = Desenho()
        self.view = View(root, self)

    def retangulo(self):
        self.forma = "retangulo"

    def oval(self):
        self.forma = "oval"

    def circulo(self):
        self.forma = "circulo"

    def linha(self):
        self.forma = "linha"

    def rabisco(self):
        self.forma = "rabisco"

    def poligono(self):
        self.forma = "poligono"
        self.pontos = []

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
        if self.forma == "poligono":
            self.pontos.append((event.x, event.y))
            self.redesenhar_tudo()
            self.view.desenhar_preview_poligono(self.pontos, self.cor_borda)
            return

        if self.forma == "rabisco":
            self.pontos = [(event.x, event.y)]
            return

        self.ini_x = event.x
        self.ini_y = event.y

    def criar_figura(self):
        if self.forma == "oval":
            return Oval(self.ini_x, self.ini_y, self.fim_x, self.fim_y, self.cor_borda, self.cor_preenchimento)
        elif self.forma == "retangulo":
            return Retangulo(self.ini_x, self.ini_y, self.fim_x, self.fim_y, self.cor_borda, self.cor_preenchimento)
        elif self.forma == "circulo":
            return Circulo(self.ini_x, self.ini_y, self.fim_x, self.fim_y, self.cor_borda, self.cor_preenchimento)
        elif self.forma == "linha":
            return Linha(self.ini_x, self.ini_y, self.fim_x, self.fim_y, self.cor_borda, self.cor_preenchimento)
        return None

    def fim(self, event):
        if self.forma == "poligono":
            return

        if self.forma == "rabisco":
            self.pontos.append((event.x, event.y))
            self.redesenhar_tudo()
            Rabisco(self.pontos, self.cor_borda, self.cor_preenchimento).desenhar(self.view.canvas)
            return

        self.fim_x = event.x
        self.fim_y = event.y

        figura_atual = self.criar_figura()
        if figura_atual is not None:
            self.redesenhar_tudo()
            figura_atual.desenhar(self.view.canvas)

    def finalizar_figura(self, event):
        if self.forma == "poligono":
            return

        if self.forma == "rabisco":
            if len(self.pontos) >= 2:
                figura_atual = Rabisco(self.pontos, self.cor_borda, self.cor_preenchimento)
                self.desenho.adicionar_figura(figura_atual)
            self.pontos = []
            self.redesenhar_tudo()
            return

        self.fim_x = event.x
        self.fim_y = event.y

        figura_atual = self.criar_figura()
        if figura_atual is not None:
            self.desenho.adicionar_figura(figura_atual)
            self.redesenhar_tudo()

    def finalizar_poligono(self, event):
        if self.forma == "poligono" and len(self.pontos) >= 3:
            figura_atual = Poligono(self.pontos, self.cor_borda, self.cor_preenchimento)
            self.desenho.adicionar_figura(figura_atual)
            self.pontos = []
            self.redesenhar_tudo()