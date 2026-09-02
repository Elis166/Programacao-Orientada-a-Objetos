from tkinter import *
import funcoes

#interface-------------------------------------------------------------------------

janela = Tk()

janela.title("Sistema de Reserva de Hotel")
janela.geometry("1000x650")
janela.config(bg="#B86830")


#título
titulo = Label(
    janela,
    text="Sistema de Reserva de Hotel",
    font=("Arial", 22, "bold"),
    bg="#C97A42",
    padx=20,
    pady=10,
    relief="solid",
    bd=2
)

titulo.pack(pady=15)


#nome
Label(
    janela,
    text="Nome do hóspede:",
    bg="#C97A42",
    fg="lightyellow"
).pack()

entrada_nome = Entry(
    janela,
    width=40
)

entrada_nome.pack(pady=5)


#cpf
Label(
    janela,
    text="CPF:",
    bg="#C97A42",
    fg="lightyellow"
).pack()

entrada_cpf = Entry(
    janela,
    width=40
)

entrada_cpf.pack(pady=5)


#telefone
Label(
    janela,
    text="Telefone:",
    bg="#C97A42",
    fg="lightyellow"
).pack()

entrada_telefone = Entry(
    janela,
    width=40
)

entrada_telefone.pack(pady=5)


#tipo de quarto
Label(
    janela,
    text="Tipo de quarto:",
    bg="#C97A42",
    fg="lightyellow"
).pack()

entrada_quarto = Entry(
    janela,
    width=40
)

entrada_quarto.pack(pady=5)


#data de entrada
Label(
    janela,
    text="Data de entrada:",
    bg="#C97A42",
    fg="lightyellow"
).pack()

entrada_data_entrada = Entry(
    janela,
    width=40
)

entrada_data_entrada.pack(pady=5)


#data de saída
Label(
    janela,
    text="Data de saída:",
    bg="#C97A42",
    fg="lightyellow"
).pack()

entrada_data_saida = Entry(
    janela,
    width=40
)

entrada_data_saida.pack(pady=5)

botao_cadastrar = Button(
    janela,
    text="Cadastrar Reserva",
    command=lambda: funcoes.cadastrar(entrada_nome, entrada_cpf, entrada_telefone, entrada_quarto, entrada_data_entrada, entrada_data_saida),
    bg="green",
    fg="white"
)

botao_cadastrar.pack(pady=10)

botao_consultar = Button(
    janela,
    text="Consultar Reservas",
    command=lambda: funcoes.consultar(caixa_texto),
    bg="blue",
    fg="white"
)

botao_consultar.pack(pady=5)

botao_limpar = Button(
    janela,
    text="Limpar Campos",
    command=lambda: funcoes.limpar(entrada_nome, entrada_cpf, entrada_telefone, entrada_quarto, entrada_data_entrada, entrada_data_saida),
    bg="red",
    fg="white"
)

botao_limpar.pack(pady=5)

caixa_texto = Text(
    janela,
    width=60,
    height=12,
    bg="grey"
)

caixa_texto.pack(pady=15)

botao_sair = Button(
    janela,
    text="Sair",
    command=lambda: funcoes.sair(janela),
    bg="yellow"
)

botao_sair.pack(pady=5)

janela.mainloop()