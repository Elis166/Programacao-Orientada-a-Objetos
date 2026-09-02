import tkinter as tk
from codigo import criar_interface


janela = tk.Tk()

janela.title("Ferramenta de Cadastro de Clientes")
janela.geometry("500x500")

criar_interface(janela)

janela.mainloop()