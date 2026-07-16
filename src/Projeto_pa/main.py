import tkinter as tk
from controlador.controlador import Controller

root = tk.Tk()
root.title('Projeto Paint')

controller = Controller(root)

root.mainloop()