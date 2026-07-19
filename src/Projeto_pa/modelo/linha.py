from .figuras import Figura

class Linha(Figura):
    def __init__(self, x1, y1, x2, y2, cor_borda, cor_preenchimento):
        super().__init__(x1, y1, x2, y2, cor_borda, cor_preenchimento)

    def desenhar(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.cor_borda, width=2)