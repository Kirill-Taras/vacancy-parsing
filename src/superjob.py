import os
from pprint import pprint

import requests

from config import SJ_URL
from src.class_api import BasicAPI
from dotenv import load_dotenv

load_dotenv()


class SuperJobAPI(BasicAPI):
    """Класс для получения вакансий с платформы superjob.ru"""
    def __init__(self, query):
        self.query = query
        self.params = {
            "keyword": self.query,
            "count": 100
        }

    def get_vacancies(self) -> list[dict]:
        headers = {"X-Api-App-Id": os.getenv("SJ_API_KEY")}
        return requests.get(url=SJ_URL, params=self.params, headers=headers).json()["objects"]


sb = SuperJobAPI("python")
print(len(sb.get_vacancies()))
pprint(sb.get_vacancies())
