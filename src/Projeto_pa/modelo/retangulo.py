from .figuras import Figura

class Retangulo(Figura):
    def __init__(self, x1, y1, x2, y2, cor_borda, cor_preenchimento):
        super().__init__(x1, y1, x2, y2, cor_borda, cor_preenchimento)

    def desenhar(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                 fill=self.cor_preenchimento, outline=self.cor_borda)