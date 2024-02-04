import json
from abc import ABC, abstractmethod

from src.jobs import Vacancy


class Sever(ABC):

    def __init__(self, path):
        self.path = path
        self.write_file_json([])

    @abstractmethod
    def read_file_json(self):
        """Метод открытия файла для чтения"""
        pass

    @abstractmethod
    def write_file_json(self, write_file):
        """Метод открытия файла для записи"""
        pass

    @abstractmethod
    def add_vacancies(self, vacancies: list[dict]) -> None:
        """Метод добавления вакансий в файл"""
        pass

    @abstractmethod
    def get_vacancies(self, query=None) -> list[dict]:
        """Метод чтения вакансий из файла"""
        pass

    @abstractmethod
    def delete_vacancies(self):
        """Метод удаления вакансий из файла"""
        pass


class JsonSever(Sever):

    def read_file_json(self):
        """Метод открытия файла для чтения"""
        with open(self.path, encoding="utf-8") as file:
            return json.load(file)

    def write_file_json(self, write_file):
        """Метод открытия файла для записи"""
        with open(self.path, "w", encoding="utf-8") as file:
            return json.dump(write_file, file, ensure_ascii=False, indent=4)

    def add_vacancies(self, vacancies: list[Vacancy]) -> None:
        vacancies_json = [vacancy.to_dict() for vacancy in vacancies]
        old_vacancies = self.read_file_json()
        old_vacancies.extend(vacancies_json)
        self.write_file_json(old_vacancies)
        
    def get_vacancies(self, queries=None) -> list[dict]:
        all_vacancies = self.read_file_json()
        vacancy_list = list()
        for vacancy in all_vacancies:
            if all(vacancy.get(field) == query for field, query in queries.items()):
                vacancy_list.append(vacancy)
        return vacancy_list

    def delete_vacancies(self, queries=None):
        all_vacancies = self.read_file_json()
        update_vacancies = list()
        for vacancy in all_vacancies:
            if all(vacancy.get(field) != query for field, query in queries.items()):
                update_vacancies.append(vacancy)
        self.write_file_json(update_vacancies)
