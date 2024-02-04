import json

from src.utils import create_sj_vacancy, create_hh_vacancy, sort_vacancy_by_salary

from config import TEST_SJ, TEST_HH


def test_create_sj_vacancy():
    with open(TEST_SJ, encoding="utf-8") as file:
        list_sj = json.load(file)
        vacancy_sj = create_sj_vacancy(list_sj)
    assert len(vacancy_sj) == 5
    assert vacancy_sj[0].vacancy_name == "Маркетинговый аналитик"


def test_create_hh_vacancy():
    with open(TEST_HH, encoding="utf-8") as file:
        list_hh = json.load(file)
        vacancy_sj = create_hh_vacancy(list_hh)
    assert len(vacancy_sj) == 5
    assert vacancy_sj[0].vacancy_name == "Стажер-программист Python"
