from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        # Inicializa uma lista vazia para a fila
        self.queue = list()

    def __len__(self):
        # Retorna o comprimento da lista
        return len(self.queue)

    def enqueue(self, value):
        # Adiciona um elemento ao final da lista
        self.queue.append(value)

    def dequeue(self):
        # Remove e retorna o primeiro elemento da lista, se existir
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def search(self, index):
        # Busca o elemento na posição especificada
        if 0 <= index <= len(self.queue) - 1:
            return self.queue[index]
        
        # Raise uma exceção caso a posição seja inválida ou inexistente
        raise IndexError("Índice Inválido ou Inexistente")
