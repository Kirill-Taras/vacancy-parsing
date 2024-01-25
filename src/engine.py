from abc import ABC, abstractmethod


class Sever(ABC):

    def __init__(self, path):
        self.path = path

    @abstractmethod
    def add_vacancies(self, vacancies: list[dict]):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass


class JsonSever(Sever):

    def add_vacancies(self):
        pass

    def get_vacancies(self):
        pass

    def delete_vacancies(self):
        pass





