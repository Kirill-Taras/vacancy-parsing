import json
from pathlib import Path
from pprint import pprint

import requests

from config import HH_URL
from src.class_api import BasicAPI


class HeadHunterAPI(BasicAPI):
    """Класс для получения вакансий с платформы hh.ru"""
    def __init__(self, query):
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


# hh = HeadHunterAPI("python")
#
# pprint(hh.get_vacancies())

    # def get_vacancies(self):
    #     keyword = input(f"Поиск по вакансиям: ")
    #     headers = {"HH-User-Agent": "GetVacancies (my@email.com)"}
    #     params = {
    #         "text": keyword,  # строка для поиска по вакансиям.
    #         "area": 113,  # код региона.
    #         "per_page": 100,  # количество вакансий.
    #         "page": None  # номер страницы.
    #               }
    #     response = requests.get(self.url, headers=headers, params=params)
    #     if response.ok:
    #         file_name = f"{params['text']}_hh.json"
    #         file_path = Path.joinpath(Path(__file__).parent.parent, "data", file_name)
    #         data_response = response.json()
    #         vacancies_info = list()
    #         try:
    #             for vacancy in data_response["items"]:
    #                 info = {
    #                     "name": vacancy.get("name"),
    #                     "location": vacancy["area"].get("name"),
    #                     "url": vacancy.get("alternate_url"),
    #                     "employer": vacancy["employer"].get("name"),
    #                     "salary_from": vacancy["salary"].get("from") if vacancy["salary"] else None,
    #                     "salary_to": vacancy["salary"].get("to") if vacancy["salary"] else None,
    #                     "description": vacancy.get("snippet").get("requirement")
    #                 }
    #                 vacancies_info.append(info)
    #             with open(file_path, "w", encoding="utf-8") as file_json:
    #                 json.dump(vacancies_info, file_json, indent=4, ensure_ascii=False)
    #             return vacancies_info
    #         except (ValueError, KeyError):
    #             print("Вакансий под ваш запрос не существует")
    #     else:
    #         print("Запрос не выполнен")