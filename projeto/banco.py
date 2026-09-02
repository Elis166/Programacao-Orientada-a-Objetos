def salvar_reserva(nome, cpf, telefone, quarto, entrada, saida):
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

def ler_reservas():
    arquivo = open(
        "reservas.txt",
        "r",
        encoding="utf-8"
    )

    dados = arquivo.read()

    arquivo.close()
    return dados