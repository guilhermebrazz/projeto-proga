from .figuras import Figura

class Poligono(Figura):
    def __init__(self, pontos, cor_borda, cor_preenchimento):
        self.pontos = pontos
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    def desenhar(self, canvas):
        canvas.create_polygon(self.pontos, fill=self.cor_preenchimento, outline=self.cor_borda)