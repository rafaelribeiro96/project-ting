import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instancia_fila: Queue):
    # Importando o arquivo utilizando a função "txt_importer"
    lista_linhas = txt_importer(path_file)

    # Criando uma lista para os nomes dos arquivos
    lista_arqui = []

    for i in range(len(instancia_fila)):
        if not instancia_fila.search(i)["nome_do_arquivo"]:
            return None
        lista_arqui.append(instancia_fila.search(i)["nome_do_arquivo"])

    # Adicionando as informações do arquivo à fila caso ele não exista
    if path_file not in lista_arqui:
        novo_arquivo = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lista_linhas),
            "linhas_do_arquivo": lista_linhas,
        }
        instancia_fila.enqueue(novo_arquivo)
        sys.stdout.write(str(novo_arquivo))


def remove(instancia_fila: Queue):
    try:
        if len(instancia_fila) > 0 or instancia_fila:
            # Removendo o primeiro elemento da fila
            arquivo_removido = instancia_fila.dequeue()
            path_file = arquivo_removido["nome_do_arquivo"]
            sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")
        # Retornando uma mensagem caso a fila esteja vazia
        sys.stdout.write("Não há elementos\n")
    except TypeError:
        print(TypeError)


def file_metadata(instancia_fila: Queue, posicao):
    try:
        # Buscando as informações do arquivo na posição indicada
        resultado_busca = instancia_fila.search(posicao)
        sys.stdout.write(str(resultado_busca))
    except IndexError:
        sys.stderr.write("Posição inválida")
