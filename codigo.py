import tkinter as tk
from tkinter import messagebox


def cadastrar_cliente(nome, sobrenome, email, telefone):

    if nome == "" or sobrenome == "" or email == "" or telefone == "":
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos!"
        )
        return

    arquivo = open("clientes.txt", "a", encoding="utf-8")

    arquivo.write(
        nome + ";" +
        sobrenome + ";" +
        email + ";" +
        telefone + "\n"
    )

    arquivo.close()

    messagebox.showinfo(
        "Sucesso",
        "Cliente cadastrado com sucesso!"
    )


def consultar_clientes(janela):

    try:
        arquivo = open("clientes.txt", "r", encoding="utf-8")
        clientes = arquivo.readlines()
        arquivo.close()

    except FileNotFoundError:
        messagebox.showinfo(
            "Consulta",
            "Nenhum cliente cadastrado."
        )
        return

    if len(clientes) == 0:
        messagebox.showinfo(
            "Consulta",
            "Nenhum cliente cadastrado."
        )
        return

    tela = tk.Toplevel(janela)

    tela.title("Clientes cadastrados")
    tela.geometry("600x400")

    titulo = tk.Label(
        tela,
        text="Clientes Cadastrados",
        font=("Arial", 18, "bold")
    )

    titulo.pack(pady=10)

    lista = tk.Listbox(
        tela,
        width=80,
        height=15
    )

    lista.pack(padx=10, pady=10)

    for cliente in clientes:

        cliente = cliente.strip()

        dados = cliente.split(";")

        texto = (
            "Nome: " + dados[0] + " " + dados[1] +
            " | E-mail: " + dados[2] +
            " | Telefone: " + dados[3]
        )

        lista.insert(tk.END, texto)


def limpar_campos(
    entrada_nome,
    entrada_sobrenome,
    entrada_email,
    entrada_telefone
):

    entrada_nome.delete(0, tk.END)
    entrada_sobrenome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)

    entrada_nome.focus()


def sair(janela):

    resposta = messagebox.askyesno(
        "Sair",
        "Deseja realmente sair do programa?"
    )

    if resposta:
        janela.destroy()


def criar_interface(janela):

    titulo = tk.Label(
        janela,
        text="Cadastro de Clientes",
        font=("Arial", 22, "bold")
    )

    titulo.pack(pady=20)

    tk.Label(
        janela,
        text="Nome:"
    ).pack()

    entrada_nome = tk.Entry(
        janela,
        width=40
    )

    entrada_nome.pack(pady=5)

    tk.Label(
        janela,
        text="Sobrenome:"
    ).pack()

    entrada_sobrenome = tk.Entry(
        janela,
        width=40
    )

    entrada_sobrenome.pack(pady=5)

    tk.Label(
        janela,
        text="E-mail:"
    ).pack()

    entrada_email = tk.Entry(
        janela,
        width=40
    )

    entrada_email.pack(pady=5)

    tk.Label(
        janela,
        text="Telefone:"
    ).pack()

    entrada_telefone = tk.Entry(
        janela,
        width=40
    )

    entrada_telefone.pack(pady=5)

    botao_cadastrar = tk.Button(
        janela,
        text="Cadastrar Cliente",
        width=30,
        command=lambda: cadastrar_cliente(
            entrada_nome.get(),
            entrada_sobrenome.get(),
            entrada_email.get(),
            entrada_telefone.get()
        )
    )

    botao_cadastrar.pack(pady=15)

    botao_consultar = tk.Button(
        janela,
        text="Consultar Clientes",
        width=30,
        command=lambda: consultar_clientes(janela)
    )

    botao_consultar.pack(pady=5)

    botao_limpar = tk.Button(
        janela,
        text="Limpar Campos",
        width=30,
        command=lambda: limpar_campos(
            entrada_nome,
            entrada_sobrenome,
            entrada_email,
            entrada_telefone
        )
    )

    botao_limpar.pack(pady=5)

    botao_sair = tk.Button(
        janela,
        text="Sair",
        width=30,
        command=lambda: sair(janela)
    )

    botao_sair.pack(pady=15)
