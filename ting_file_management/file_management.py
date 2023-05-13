import sys


def txt_importer(path: str):
    try:
        if not path.endswith(".txt"):
            raise TypeError
        with open(path) as file:
            arr = [f_line.rstrip("\n") for f_line in file]
            return arr

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path} não encontrado\n")
    except TypeError:
        sys.stderr.write("Formato inválido")
