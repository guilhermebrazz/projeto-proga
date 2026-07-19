from .figuras import Figura

class Circulo(Figura):
    def __init__(self, x1, y1, x2, y2, cor_borda, cor_preenchimento):
        super().__init__(x1, y1, x2, y2, cor_borda, cor_preenchimento)
        self.raio = ((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) ** 0.5

    def desenhar(self, canvas):
        canvas.create_oval(self.x1 - self.raio, self.y1 - self.raio,
                            self.x1 + self.raio, self.y1 + self.raio,
                            fill=self.cor_preenchimento, outline=self.cor_borda)