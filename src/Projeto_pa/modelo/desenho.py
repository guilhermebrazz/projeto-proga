import json
from .circulo import Circulo
from .retangulo import Retangulo
from .oval import Oval
from .linha import Linha
from .poligono import Poligono
from .rabiscos import Rabisco


class Desenho:
    def __init__(self):
        self.figuras = []

    def adicionar_figura(self, figura):
        self.figuras.append(figura)

    def remover_figura(self, figura):
        self.figuras.remove(figura)

    def limpar(self):
        self.figuras.clear()

    def desenhar(self, canvas):
        for figura in self.figuras:
            figura.desenhar(canvas)

    def salvar(self, caminho):
        dados = [self._figura_para_dict(figura) for figura in self.figuras]
        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=2)

    def carregar(self, caminho):
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        self.figuras = [self._dict_para_figura(item) for item in dados]

    def _figura_para_dict(self, figura):
        tipo = type(figura).__name__
        if tipo in ("Poligono", "Rabisco"):
            return {
                "tipo": tipo,
                "pontos": figura.pontos,
                "cor_borda": figura.cor_borda,
                "cor_preenchimento": figura.cor_preenchimento,
            }
        return {
            "tipo": tipo,
            "x1": figura.x1,
            "y1": figura.y1,
            "x2": figura.x2,
            "y2": figura.y2,
            "cor_borda": figura.cor_borda,
            "cor_preenchimento": figura.cor_preenchimento,
        }

    def _dict_para_figura(self, dados):
        tipo = dados["tipo"]
        classes = {"Oval": Oval, "Retangulo": Retangulo, "Circulo": Circulo, "Linha": Linha}

        if tipo in classes:
            classe = classes[tipo]
            return classe(dados["x1"], dados["y1"], dados["x2"], dados["y2"],
                           dados["cor_borda"], dados["cor_preenchimento"])
        elif tipo == "Poligono":
            pontos = [tuple(p) for p in dados["pontos"]]
            return Poligono(pontos, dados["cor_borda"], dados["cor_preenchimento"])
        elif tipo == "Rabisco":
            pontos = [tuple(p) for p in dados["pontos"]]
            return Rabisco(pontos, dados["cor_borda"], dados["cor_preenchimento"])
        return None