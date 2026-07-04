import tkinter as tk

class Paint:


    def __init__(self, root):

        self.ini_x = None
        self.ini_y = None
        self.fim_x = None
        self.fim_y = None
        self.forma = None

        #Menu de formas
        self.barra = tk.Frame(root)
        self.barra.pack()
        self.btn_retangulo = tk.Button(self.barra, text="Retângulo", command = self.retangulo)
        self.btn_retangulo.pack(side="left")

        self.btn_oval = tk.Button(self.barra, text="Oval", command= self.oval)
        self.btn_oval.pack(side="left")

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
            
            self.canvas.create_oval(self.ini_x, self.ini_y, self.fim_x, self.fim_y)
        
        elif self.forma == "retangulo":

            self.canvas.create_rectangle(self.ini_x, self.ini_y, self.fim_x, self.fim_y)

#Configurações da interface
root = tk.Tk()
root.title('Projeto Paint')

obj = Paint(root)


root.mainloop()

