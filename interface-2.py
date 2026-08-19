import tkinter as tk
janela = tk.Tk()
janela.title("Login")
janela.geometry('700x450')

tk.Label(janela,
    text="Usuário:").grid(
    row=0, column=0, sticky="e")

tk.Entry(janela).grid(
    row=0, column=1)

tk.Label(janela,
    text="Senha:").grid(
    row=1, column=0, sticky="e")

tk.Entry(janela,
    show="*").grid(
    row=1, column=1)

tk.Button(janela,
    text="Entrar").grid(
    row=2, column=0,
    columnspan=2)
janela.mainloop()