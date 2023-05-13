import sys


def txt_importer(path: str):
    try:
        # Verifica se o caminho do arquivo possui extensão .txt
        if not path.endswith(".txt"):
            raise TypeError

        # Abre o arquivo e armazena cada linha em uma lista
        with open(path) as file:
            arr = [f_line.rstrip("\n") for f_line in file]
            return arr

    # Tratamento de exceções em 2 casos
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path} não encontrado\n")
    except TypeError:
        sys.stderr.write("Formato inválido")
