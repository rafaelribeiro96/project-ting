from ting_file_management.queue import Queue


def search_by_word(word: str, inst: Queue):
    # Converte a palavra para letra minúscula
    lower = word.lower()
    
    # Inicializa uma lista vazia e um dicionário com a palavra de busca
    arr = []
    dict_mock = {
        "palavra": word,
    }
    
    # Itera sobre os elementos da fila
    for i in range(len(inst)):
        get_file = inst.search(i)
        
        # Adiciona o nome do arquivo atual ao dicionário
        dict_mock["arquivo"] = get_file["nome_do_arquivo"]
        info_arr = []
        
        # Procura pela palavra de busca em cada linha do arquivo
        for i, f_line in enumerate(get_file["linhas_do_arquivo"]):
            if lower in f_line.lower():
                info_arr.append({"linha": i + 1, "conteudo": f_line})
        
        # Se alguma ocorrência foi encontrada, adiciona-a ao dicionário e à lista de resultados
        if len(info_arr) >= 1:
            dict_mock["ocorrencias"] = info_arr
            arr.append(dict_mock)
            
        # Retorna a lista de resultados
        return arr


def exists_word(word: str, inst: Queue):
    # Inicializa uma lista vazia e um dicionário com a palavra de busca
    arr = []
    dict_mock = {
        "palavra": word,
    }
    
    # Converte a palavra para letra minúscula
    lower = word.lower()

    # Itera sobre os elementos da fila
    for length in range(len(inst)):
        get_file = inst.search(length)
        dict_mock["arquivo"] = get_file["nome_do_arquivo"]
        info_arr = []
        
        # Procura pela palavra de busca em cada linha do arquivo
        for index, f_line in enumerate(get_file["linhas_do_arquivo"]):
            if lower in f_line.lower():
                info_arr.append({"linha": index + 1})
        
        # Se alguma ocorrência foi encontrada, adiciona-a ao dicionário e à lista de resultados
        if len(info_arr) >= 1:
            dict_mock["ocorrencias"] = info_arr
            arr.append(dict_mock)
            
        # Retorna a lista de resultados
        return arr
