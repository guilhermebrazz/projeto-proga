import tkinter as tk
from tkinter import colorchooser
from figuras import * 

class Paint:


    def __init__(self, root):

        self.ini_x = None
        self.ini_y = None
        self.fim_x = None
        self.fim_y = None
        self.forma = None
        self.cor = None
        self.cor_borda = "#000000"
        self.cor_preenchimento = "#ffffff"
        #Menu de formas
        self.barra = tk.Frame(root)
        self.barra.pack()
        self.btn_retangulo = tk.Button(self.barra, text="Retângulo", command = self.retangulo)
        self.btn_retangulo.pack(side="left")

        self.btn_oval = tk.Button(self.barra, text="Oval", command= self.oval)
        self.btn_oval.pack(side="left")
        self.btn_circulo = tk.Button(self.barra, text="Círculo", command = self.circulo)
        self.btn_circulo.pack(side="left")
        self.btn_c1 = tk.Button(self.barra, text="Azul", command = self.azul)
        self.btn_c1.pack(side="left")
        self.btn_c2 = tk.Button(self.barra, text="Vermelho", command = self.vermelho)
        self.btn_c2.pack(side="left")
        self.btn_c3 = tk.Button(self.barra, text="Verde", command = self.verde)
        self.btn_c3.pack(side="left")

        tk.Label(self.barra, text=" Borda: ").pack(side="left")
        self.botao_cor_borda = tk.Button(
            self.barra, text="   ", bg=self.cor_borda, relief=tk.RIDGE, width=3,
            command=self.escolher_cor_borda
        )
        self.botao_cor_borda.pack(side="left", padx=5)

        tk.Label(self.barra, text=" Preenchimento: ").pack(side="left")
        self.botao_cor_preenchimento = tk.Button(
            self.barra, text="   ", bg=self.cor_preenchimento, relief=tk.RIDGE, width=3,
            command=self.escolher_cor_preenchimento
        )
        self.botao_cor_preenchimento.pack(side="left", padx=5)

        #Configurações do canvas (parte que desenha)
        self.canvas = tk.Canvas(root, bg="white", width=600, height=600)
        self.canvas.pack()
        
                    #Quando clicar no mouse -> chame a funcao inicio
        self.canvas.bind("<ButtonPress-1>", self.inicio)
        self.canvas.bind("<B1-Motion>", self.fim)

    #captura a forma escolhida quando é clicada no menu
    def retangulo(self):
        self.forma = "retangulo"
    def oval(self):
        self.forma = "oval"
    def circulo(self):
        self.forma = "circulo"
    def azul(self):
        self.cor = "blue"
    def vermelho(self):
        self.cor = "red"
    def verde(self):
        self.cor = "green"

    def escolher_cor_borda(self):
        resultado = colorchooser.askcolor(color=self.cor_borda, title="Escolha a cor da borda")
        cor_escolhida = resultado[1]
        if cor_escolhida is not None:
            self.cor_borda = cor_escolhida
            self.botao_cor_borda.config(bg=self.cor_borda)

    def escolher_cor_preenchimento(self):
        resultado = colorchooser.askcolor(color=self.cor_preenchimento, title="Escolha a cor de preenchimento")
        cor_escolhida = resultado[1]
        if cor_escolhida is not None:
            self.cor_preenchimento = cor_escolhida
            self.botao_cor_preenchimento.config(bg=self.cor_preenchimento)
    
    def inicio(self, event):

        #captura as coordenadas de x e de y no momento em que a funcao é chamada
        self.ini_x = event.x
        self.ini_y = event.y
    
    def fim(self, event):

        #captura todas as coordenadas de x e de y enquanto o mouse se move e só mostra a atual
        self.fim_x = event.x
        self.fim_y = event.y
        self.canvas.delete("all")

        #mostra a figura
        if self.forma == "oval":
            
            figura_atual = Oval(self.ini_x,self.ini_y,self.fim_x,self.fim_y, self.cor_borda, self.cor_preenchimento)
        
        elif self.forma == "retangulo":

            figura_atual = Retangulo(self.ini_x,self.ini_y,self.fim_x,self.fim_y, self.cor_borda, self.cor_preenchimento)
        elif self.forma == "circulo":

            figura_atual = Circulo(self.ini_x,self.ini_y,self.fim_x,self.fim_y, self.cor_borda, self.cor_preenchimento)
        if figura_atual is not None:
            figura_atual.desenhar(self.canvas)
        
        
        
            
        
            
            


            

#Configurações da interface
root = tk.Tk()
root.title('Projeto Paint')

obj = Paint(root)


root.mainloop()