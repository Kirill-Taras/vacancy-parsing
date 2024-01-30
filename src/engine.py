import json
from abc import ABC, abstractmethod

from src.jobs import Vacancy


class Sever(ABC):

    def __init__(self, path):
        self.path = path

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

    def add_vacancies(self, vacancies: list[Vacancy]) -> None:
        vacancies_json = [vacancy.to_dict() for vacancy in vacancies]
        with open(self.path, encoding="utf-8") as file:
            old_vacancies = json.load(file)
        old_vacancies.extend(vacancies_json)
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(old_vacancies, file)

    def get_vacancies(self, queries=None) -> list[dict]:
        with open(self.path, encoding="utf-8") as file:
            all_vacancies = json.load(file)
            vacancy_list = list()
        for vacancy in all_vacancies:
            if all(vacancy.get(field) == query for field, query in queries.items()):
                vacancy_list.append(vacancy)
        return vacancy_list

    def delete_vacancies(self, queries=None):
        with open(self.path, encoding="utf-8") as file:
            all_vacancies = json.load(file)
            update_vacancies = list()
        for vacancy in all_vacancies:
            if all(vacancy.get(field) != query for field, query in queries.items()):
                update_vacancies.append(vacancy)
        return update_vacancies
