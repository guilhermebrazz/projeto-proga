
from abc import ABC, abstractmethod

from modelo import Oval, Retangulo, Circulo, Linha, Poligono, Rabisco


class EstadoForma(ABC):

    def ao_selecionar(self, controller):
        pass

    @abstractmethod
    def inicio(self, controller, event):
        
        raise NotImplementedError

    @abstractmethod
    def mover(self, controller, event):
        
        raise NotImplementedError

    @abstractmethod
    def finalizar(self, controller, event):
        
        raise NotImplementedError

    def duplo_clique(self, controller, event):
       
        pass


class EstadoArrastar(EstadoForma):

    def inicio(self, controller, event):
        controller.ini_x = event.x
        controller.ini_y = event.y

    def mover(self, controller, event):
        controller.fim_x = event.x
        controller.fim_y = event.y
        figura_atual = self.criar_figura(controller)
        if figura_atual is not None:
            controller.redesenhar_tudo()
            figura_atual.desenhar(controller.view.canvas)

    def finalizar(self, controller, event):
        controller.fim_x = event.x
        controller.fim_y = event.y
        figura_atual = self.criar_figura(controller)
        if figura_atual is not None:
            controller.desenho.adicionar_figura(figura_atual)
            controller.redesenhar_tudo()

    @abstractmethod
    def criar_figura(self, controller):
        
        raise NotImplementedError


class EstadoRetangulo(EstadoArrastar):
    def criar_figura(self, controller):
        return Retangulo(controller.ini_x, controller.ini_y,
                          controller.fim_x, controller.fim_y,
                          controller.cor_borda, controller.cor_preenchimento)


class EstadoOval(EstadoArrastar):
    def criar_figura(self, controller):
        return Oval(controller.ini_x, controller.ini_y,
                     controller.fim_x, controller.fim_y,
                     controller.cor_borda, controller.cor_preenchimento)


class EstadoCirculo(EstadoArrastar):
    def criar_figura(self, controller):
        return Circulo(controller.ini_x, controller.ini_y,
                        controller.fim_x, controller.fim_y,
                        controller.cor_borda, controller.cor_preenchimento)


class EstadoLinha(EstadoArrastar):
    def criar_figura(self, controller):
        return Linha(controller.ini_x, controller.ini_y,
                      controller.fim_x, controller.fim_y,
                      controller.cor_borda, controller.cor_preenchimento)


class EstadoPoligono(EstadoForma):

    def ao_selecionar(self, controller):
        controller.pontos = []

    def inicio(self, controller, event):
        controller.pontos.append((event.x, event.y))
        controller.redesenhar_tudo()
        controller.view.desenhar_preview_poligono(controller.pontos, controller.cor_borda)

    def mover(self, controller, event):
        pass

    def finalizar(self, controller, event):
        pass

    def duplo_clique(self, controller, event):
        if len(controller.pontos) >= 3:
            figura_atual = Poligono(controller.pontos, controller.cor_borda, controller.cor_preenchimento)
            controller.desenho.adicionar_figura(figura_atual)
            controller.pontos = []
            controller.redesenhar_tudo()


class EstadoRabisco(EstadoForma):

    def inicio(self, controller, event):
        controller.pontos = [(event.x, event.y)]

    def mover(self, controller, event):
        controller.pontos.append((event.x, event.y))
        controller.redesenhar_tudo()
        Rabisco(controller.pontos, controller.cor_borda, controller.cor_preenchimento).desenhar(controller.view.canvas)

    def finalizar(self, controller, event):
        if len(controller.pontos) >= 2:
            figura_atual = Rabisco(controller.pontos, controller.cor_borda, controller.cor_preenchimento)
            controller.desenho.adicionar_figura(figura_atual)
        controller.pontos = []
        controller.redesenhar_tudo()
