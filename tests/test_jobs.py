import json

import pytest

from config import TEST_VACANCY_JSON
from src.jobs import Vacancy


@pytest.fixture()
def vacancy_object():
    with open(TEST_VACANCY_JSON, encoding="utf-8") as file:
        read_file = json.load(file)
    vacancy = [Vacancy(**vac) for vac in read_file]
    return vacancy


def test_vacancy(vacancy_object):
    vac_1 = vacancy_object[0]
    assert vac_1.vacancy_name == "Python Developer"
    assert vac_1.town_job == "Алматы"
    assert vac_1.validate_salary("None") == 0
    assert vac_1.validate_salary(1000) == 1000
    assert vac_1.validate_description("<highlighttext>Python") == "Python"
    assert vac_1.validate_description("</highlighttext>Python") == "Python"
    assert vac_1.average_salary == 2000000
    vac_2 = vacancy_object[1]
    assert vac_2 == vac_1
    assert not vac_2 > vac_1
    assert not vac_2 < vac_1

