class Figura:
    def __init__(self, x1,y1,x2,y2,cor_borda,cor_preenchimento):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
class Retangulo(Figura):
    def __init__(self, x1, y1, x2, y2, cor_borda, cor_preenchimento):
        super().__init__(x1,y1,x2,y2,cor_borda,cor_preenchimento)
    def desenhar(self,canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill = self.cor_preenchimento , outline= self.cor_borda)
class Oval(Figura):
    def __init__(self, x1, y1, x2, y2, cor_borda, cor_preenchimento):
        super().__init__(x1,y1,x2,y2,cor_borda,cor_preenchimento)
    def desenhar(self,canvas):
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill = self.cor_preenchimento , outline= self.cor_borda)
class Circulo(Figura):
    def __init__(self, x1, y1, x2, y2, cor_borda, cor_preenchimento):
        super().__init__(x1,y1,x2,y2,cor_borda,cor_preenchimento)
        self.raio = ( (self.x1 - self.x2) **2 + (self.y1 - self.y2) **2 ) ** 0.5
    def desenhar(self,canvas):
        canvas.create_oval(self.x1 - self.raio, self.y1 - self.raio, self.x1 + self.raio, self.y1 + self.raio, fill = self.cor_preenchimento, outline= self.cor_borda )