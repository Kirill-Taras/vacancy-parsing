from abc import ABC, abstractmethod
import requests


class BasicAPI(ABC):
    """Абстрактный класс для получения API с сайтов."""

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(BasicAPI):
    """Получение вакансий с платформы hh.ru"""
    def __init__(self):
        pass

    def get_vacancies(self):
        pass


class SuperJobAPI(BasicAPI):
    """Получение вакансий с платформы superjob.ru"""
    def __init__(self):
        pass

    def get_vacancies(self):
        pass
