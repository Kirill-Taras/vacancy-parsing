import json
from abc import ABC, abstractmethod

from src.jobs import Vacancy


class Sever(ABC):
    """Абстрактный класс для работы с файлами"""

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
        """Метод получени вакансий из файла"""
        pass

    @abstractmethod
    def delete_vacancies(self):
        """Метод удаления вакансий из файла"""
        pass


class JsonSever(Sever):
    """Класс для работы с json файлами."""

    def read_file_json(self):
        """Метод открытия файла для чтения"""
        with open(self.path, encoding="utf-8") as file:
            return json.load(file)

    def write_file_json(self, write_data):
        """Метод открытия файла для записи"""
        with open(self.path, "w", encoding="utf-8") as file:
            return json.dump(write_data, file, ensure_ascii=False, indent=4)

    def add_vacancies(self, vacancies: list[Vacancy]) -> None:
        """"Метод добавления вакансий в файл json"""
        vacancies_json = [vacancy.to_dict() for vacancy in vacancies]
        old_vacancies = self.read_file_json()
        old_vacancies.extend(vacancies_json)
        self.write_file_json(old_vacancies)
        
    def get_vacancies(self, query=None) -> list[dict]:
        """"Метод получения вакансий из файла json"""
        all_vacancies = self.read_file_json()
        vacancy_list = list()
        for vacancy in all_vacancies:
            if query:
                if query in vacancy["description_vacancy"].lower():
                    vacancy_list.append(vacancy)
            else:
                vacancy_list = all_vacancies
        return vacancy_list

    def delete_vacancies(self, query=None):
        """Метод удаления вакансий из файла json"""
        all_vacancies = self.read_file_json()
        update_vacancies = list()
        for vacancy in all_vacancies:
            if query:
                if query not in vacancy["description_vacancy"]:
                    update_vacancies.append(vacancy)
                else:
                    update_vacancies = all_vacancies
        self.write_file_json(update_vacancies)

    def clear_file(self):
        """Метод для удаления всех вакансий из файла"""
        with open(self.path, "w", encoding="utf-8") as file:
            return json.dump([], file)

