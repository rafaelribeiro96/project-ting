import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(file, inst: Queue):
    # Inicializa uma lista vazia
    arr = []

    # Chama a função txt_importer para obter as informações do arquivo
    get_file = txt_importer(file)

    # Itera sobre os elementos da fila
    for length in range(len(inst)):
        if not inst.search(length)["nome_do_arquivo"]:
            return None
        arr.append(inst.search(length)["nome_do_arquivo"])

    # Verifica se o arquivo já está na lista
    if file not in arr:
        new_info = {
            "nome_do_arquivo": file,
            "qtd_linhas": len(get_file),
            "linhas_do_arquivo": get_file,
        }
        inst.enqueue(new_info)
        sys.stdout.write(str(new_info))


def remove(inst: Queue):
    # Tenta remover um elemento da fila
    try:
        if len(inst) > 0 or inst:
            get_file = inst.dequeue()
            f_path = get_file["nome_do_arquivo"]
            sys.stdout.write(f"Arquivo {f_path} removido com sucesso\n")

        # Caso contrário, exibe uma mensagem informando que a fila está vazia
        sys.stdout.write("Não há elementos\n")

    # Tratamento de exceção caso ocorra um erro ao remover o elemento da fila
    except TypeError:
        print(TypeError)


def file_metadata(inst: Queue, pos):
    # Tenta buscar as informações do arquivo na posição especificada
    try:
        get_result = inst.search(pos)
        sys.stdout.write(str(get_result))

    # Tratamento de exceção caso a posição seja inválida
    except IndexError:
        sys.stderr.write("Posição inválida")
