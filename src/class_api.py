import os
from abc import ABC, abstractmethod

import requests
from dotenv import load_dotenv

from config import HH_URL, SJ_URL

load_dotenv()


class BasicAPI(ABC):
    """Абстрактный класс для получения API с сайтов."""

    @abstractmethod
    def get_vacancies(self) -> list[dict]:
        """Метод получения вакансий."""
        pass


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
        Метод получения вакансий с платформы hh.ru.
        :return: Список с вакансиями
        """
        try:
            response = requests.get(url=HH_URL, headers=self.headers, params=self.params).json()["items"]
            return response
        except Exception as err:
            print(f"{err}: Сервис hh.ru не доступен")


class SuperJobAPI(BasicAPI):
    """Класс для получения вакансий с платформы superjob.ru"""
    def __init__(self, query: str):
        self.query = query  # ключевое слово.
        self.params = {"keywords": self.query, "count": 100}
        self.headers = {"X-Api-App-Id": os.getenv("SJ_API_KEY")}

    def get_vacancies(self, page=0) -> list[dict]:
        """
        Метод получения вакансий с платформы superjob.ru.
        :return: Список с вакансиями
        """
        self.params["page"] = page  # номер страницы.
        try:
            response = requests.get(url=SJ_URL, params=self.params, headers=self.headers).json()["objects"]
            return response
        except Exception as err:
            print(f"{err}: Сервис superjob.ru не доступен")
