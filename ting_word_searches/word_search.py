from ting_file_management.queue import Queue


def search_by_word(word: str, inst: Queue):
    lower = word.lower()
    arr = []
    dict_mock = {
        "palavra": word,
    }
    for i in range(len(inst)):
        get_file = inst.search(i)
        dict_mock["arquivo"] = get_file["nome_do_arquivo"]
        info_arr = []
        for i, f_line in enumerate(get_file["linhas_do_arquivo"]):
            if lower in f_line.lower():
                info_arr.append({"linha": i + 1, "conteudo": f_line})
        if len(info_arr) >= 1:
            dict_mock["ocorrencias"] = info_arr
            arr.append(dict_mock)
        return arr


def exists_word(word: str, inst: Queue):
    arr = []
    dict_mock = {
        "palavra": word,
    }
    lower = word.lower()

    for length in range(len(inst)):
        get_file = inst.search(length)
        dict_mock["arquivo"] = get_file["nome_do_arquivo"]
        info_arr = []
        for index, f_line in enumerate(get_file["linhas_do_arquivo"]):
            if lower in f_line.lower():
                info_arr.append({"linha": index + 1})
        if len(info_arr) >= 1:
            dict_mock["ocorrencias"] = info_arr
            arr.append(dict_mock)
        return arr
