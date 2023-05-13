import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(file, inst: Queue):
    arr = []

    get_file = txt_importer(file)

    for length in range(len(inst)):
        if not inst.search(length)["nome_do_arquivo"]:
            return None
        arr.append(inst.search(length)["nome_do_arquivo"])

    if file not in arr:
        new_info = {
            "nome_do_arquivo": file,
            "qtd_linhas": len(get_file),
            "linhas_do_arquivo": get_file,
        }
        inst.enqueue(new_info)
        sys.stdout.write(str(new_info))


def file_metadata(inst: Queue, pos):
    try:
        f_result = inst.search(pos)
        sys.stdout.write(str(f_result))
    except IndexError:
        sys.stderr.write("Posição inválida")


def remove(inst: Queue):
    try:
        if len(inst) > 0 or inst:
            get_file = inst.dequeue()
            f_path = get_file["nome_do_arquivo"]
            sys.stdout.write(f"Arquivo {f_path} removido com sucesso\n")
        sys.stdout.write("Não há elementos\n")
    except TypeError:
        print(TypeError)
