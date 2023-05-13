from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.__queue = []

    def __len__(self):
        return len(self.__queue)

    def enqueue(self, value):
        self.__queue.append(value)

    def dequeue(self):
        self.__queue.pop(0)

    def search(self, index):
        if not (0 >= index <= len(self.__queue)):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.__queue[index]
