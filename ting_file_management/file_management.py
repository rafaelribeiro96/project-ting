import sys


def txt_importer(caminho_arquivo: str):
    try:
        # Verificando se a extensão do arquivo é ".txt"
        if not caminho_arquivo.endswith(".txt"):
            raise TypeError

        # Abrindo o arquivo e armazenando cada linha em uma lista
        with open(caminho_arquivo) as arquivo:
            lista_linhas = [l_arq.rstrip("\n") for l_arq in arquivo]
            
            # Retornando a lista de linhas
            return lista_linhas

    # Tratando o erro caso o arquivo não seja encontrado
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {caminho_arquivo} não encontrado\n")
    
    # Tratando o erro caso o formato do arquivo não seja válido
    except TypeError:
        sys.stderr.write("Formato inválido")
