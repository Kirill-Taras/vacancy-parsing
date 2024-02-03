import requests

from config import HH_URL
from src.class_api import BasicAPI


class HeadHunterAPI(BasicAPI):
    """Класс для получения вакансий с платформы hh.ru"""
    def __init__(self, query: str):
        self.query = query
        self.params = {
            "text": self.query,  # слово для поиска по вакансиям.
            "per_page": 100,  # количество вакансий.
            "page": None,  # номер страницы.
            "search_field": "name"  # поле для поиска.
                  }
        self.headers = {"HH-User-Agent": "GetVacancies (my@email.com)"}

    def get_vacancies(self) -> list[dict]:
        """
        Метод получения вакансий.
        :return: Список с вакансиями
        """
        return requests.get(url=HH_URL, headers=self.headers, params=self.params).json()["items"]
