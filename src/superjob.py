import os
from pprint import pprint

import requests

from config import SJ_URL
from src.class_api import BasicAPI
from dotenv import load_dotenv

load_dotenv()


class SuperJobAPI(BasicAPI):
    """Класс для получения вакансий с платформы superjob.ru"""
    def __init__(self, query: str):
        self.query = query
        self.params = {
            "keywords": self.query,  # ключевое слово.
            "count": 100  # количество вакансий.
        }
        self.headers = {"X-Api-App-Id": os.getenv("SJ_API_KEY")}

    def get_vacancies(self, page=0) -> list[dict]:
        """
                Метод получения вакансий.
                :return: Список с вакансиями
                """
        self.params["page"] = page  # номер страницы.
        return requests.get(url=SJ_URL, params=self.params, headers=self.headers).json()["objects"]


# if __name__ == '__main__':
#     sb = SuperJobAPI("полный")
#     res = sb.get_vacancies()
#     print(len(res))
#     pprint(res)
