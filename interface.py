import tkinter as tk

janela = tk.Tk()
janela.geometry('1500x500')
janela.title('Compra de ingresso')
botao = tk.Button(
    janela,
    text="Enviar",
    bg="green",
    fg="white"
)
botao.pack()
rotulo = tk.Label(janela, text="Olá, Mundo!")
janela.mainloop()