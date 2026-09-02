from tkinter import messagebox, END
import banco

def cadastrar(entrada_nome, entrada_cpf, entrada_telefone, entrada_quarto, entrada_data_entrada, entrada_data_saida):
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
        banco.salvar_reserva(nome, cpf, telefone, quarto, entrada, saida)

        messagebox.showinfo(
            "Sucesso",
            "Reserva cadastrada com sucesso!"
        )

        limpar(entrada_nome, entrada_cpf, entrada_telefone, entrada_quarto, entrada_data_entrada, entrada_data_saida)


def consultar(caixa_texto):

    try:
        dados = banco.ler_reservas()

        caixa_texto.delete("1.0", END)

        caixa_texto.insert(END, dados)

    except FileNotFoundError:

        messagebox.showwarning(
            "Atenção",
            "Ainda não existem reservas cadastradas!"
        )

def limpar(entrada_nome, entrada_cpf, entrada_telefone, entrada_quarto, entrada_data_entrada, entrada_data_saida):

    entrada_nome.delete(0, END)
    entrada_cpf.delete(0, END)
    entrada_telefone.delete(0, END)
    entrada_quarto.delete(0, END)
    entrada_data_entrada.delete(0, END)
    entrada_data_saida.delete(0, END)

def sair(janela):

    janela.destroy()