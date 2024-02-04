import json

import pytest

from config import TEST_JSON, TEST_VACANCY_JSON
from src.engine import JsonSever
from src.jobs import Vacancy
from src.utils import create_hh_vacancy


@pytest.fixture
def dict_json():
    return {
        "vacancy_name": "Программист Python",
        "salary_from": 1300000,
        "salary_to": 0,
        "url_vacancy": "https://api.hh.ru/vacancies/91273894?host=hh.ru",
        "town_job": "Астана",
        "description_vacancy": "Опыт разработки с использованием технологий",
        "platform": "HeadHunter"
    }


@pytest.fixture()
def vacancy_object():
    with open(TEST_VACANCY_JSON, encoding="utf-8") as file:
        read_file = json.load(file)
    vacancy = [Vacancy(**vac) for vac in read_file]
    return vacancy


def test_json_sever(dict_json, vacancy_object):
    json_sever = JsonSever(TEST_JSON)
    assert json_sever.read_file_json() == []
    json_sever.write_file_json(dict_json)
    assert json_sever.read_file_json() == dict_json
    json_sever.clear_file()
    assert json_sever.read_file_json() == []
    json_sever.add_vacancies(vacancy_object)
    assert len(json_sever.read_file_json()) == 4
    assert len(json_sever.get_vacancies("опыт")) == 1
    json_sever.delete_vacancies("опыт")
    assert len(json_sever.read_file_json()) == 3
