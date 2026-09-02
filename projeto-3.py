from tkinter import *
from tkinter import messagebox

def cadastrar():
    nome = entrada_nome.get()
    cpf = entrada_cpf.get()
    telefone = entrada_telefone.get()
    quarto = entrada_quarto.get()
    entrada = entrada_data_entrada.get()
    saida = entrada_data_saida.get()

    if nome == "" or cpf == "" or telefone == "" or quarto == "" or entrada == "" or saida == "":
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos!"
        )

    else:

        arquivo = open(
            "reservas.txt",
            "a",
            encoding="utf-8"
        )

        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"CPF: {cpf}\n")
        arquivo.write(f"Telefone: {telefone}\n")
        arquivo.write(f"Tipo de quarto: {quarto}\n")
        arquivo.write(f"Data de entrada: {entrada}\n")
        arquivo.write(f"Data de saída: {saida}\n")
        arquivo.write("-----------------------------\n")

        arquivo.close()

        messagebox.showinfo(
            "Sucesso",
            "Reserva cadastrada com sucesso!"
        )

        limpar()


def consultar():

    try:

        arquivo = open(
            "reservas.txt",
            "r",
            encoding="utf-8"
        )

        dados = arquivo.read()

        arquivo.close()

        caixa_texto.delete("1.0", END)

        caixa_texto.insert(END, dados)

    except FileNotFoundError:

        messagebox.showwarning(
            "Atenção",
            "Ainda não existem reservas cadastradas!"
        )

def limpar():

    entrada_nome.delete(0, END)
    entrada_cpf.delete(0, END)
    entrada_telefone.delete(0, END)
    entrada_quarto.delete(0, END)
    entrada_data_entrada.delete(0, END)
    entrada_data_saida.delete(0, END)

def sair():

    janela.destroy()

#interface-------------------------------------------------------------------------

janela = Tk()

janela.title("Sistema de Reserva de Hotel")
janela.geometry("1000x650")


#título
titulo = Label(
    janela,
    text="Sistema de Reserva de Hotel",
    font=("Arial", 18, "bold")
)

titulo.pack(pady=15)


#nome
Label(
    janela,
    text="Nome do hóspede:"
).pack()

entrada_nome = Entry(
    janela,
    width=40
)

entrada_nome.pack(pady=5)


#cpf
Label(
    janela,
    text="CPF:"
).pack()

entrada_cpf = Entry(
    janela,
    width=40
)

entrada_cpf.pack(pady=5)


#telefone
Label(
    janela,
    text="Telefone:"
).pack()

entrada_telefone = Entry(
    janela,
    width=40
)

entrada_telefone.pack(pady=5)


#tipo de quarto
Label(
    janela,
    text="Tipo de quarto:"
).pack()

entrada_quarto = Entry(
    janela,
    width=40
)

entrada_quarto.pack(pady=5)


#data de entrada
Label(
    janela,
    text="Data de entrada:"
).pack()

entrada_data_entrada = Entry(
    janela,
    width=40
)

entrada_data_entrada.pack(pady=5)


#data de saída
Label(
    janela,
    text="Data de saída:"
).pack()

entrada_data_saida = Entry(
    janela,
    width=40
)

entrada_data_saida.pack(pady=5)

botao_cadastrar = Button(
    janela,
    text="Cadastrar Reserva",
    command=cadastrar,
    bg="green",
    fg="white"
)

botao_cadastrar.pack(pady=10)

botao_consultar = Button(
    janela,
    text="Consultar Reservas",
    command=consultar,
    bg="blue",
    fg="white"
)

botao_consultar.pack(pady=5)

botao_limpar = Button(
    janela,
    text="Limpar Campos",
    command=limpar,
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
    command=sair,
    bg="yellow"
)

botao_sair.pack(pady=5)

janela.mainloop()