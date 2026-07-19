from .figuras import Figura

class Rabisco(Figura):
    def __init__(self, pontos, cor_borda, cor_preenchimento):
        self.pontos = pontos
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    def desenhar(self, canvas):
        if len(self.pontos) >= 2:
            canvas.create_line(self.pontos, fill=self.cor_borda, width=2, smooth=True)