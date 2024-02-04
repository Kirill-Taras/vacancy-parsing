from pathlib import Path

HH_URL = "https://api.hh.ru/vacancies"
SJ_URL = "https://api.superjob.ru/2.0/vacancies/"
VACANCY_JSON = Path.joinpath(Path(__file__).parent, "data", "vacancy.json")
TEST_VACANCY_JSON = Path.joinpath(Path(__file__).parent, "data", "test_vacancy.json")
TEST_SJ = Path.joinpath(Path(__file__).parent, "data", "test_sj_vacancy.json")
TEST_HH = Path.joinpath(Path(__file__).parent, "data", "test_hh_vacancy.json")
TEST_JSON = Path.joinpath(Path(__file__).parent, "data", "test_json_vacancy.json")
