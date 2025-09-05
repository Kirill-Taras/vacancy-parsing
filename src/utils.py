from src.jobs import HeadHunterVacancy, SuperJobVacancy, Vacancy


def create_sj_vacancy(vacancies: list[dict]):
    """Функция для приведения данных с сайта SuperJob к единому виду."""
    all_vacancies = []
    for vacancy in vacancies:
        sj_vacancy = SuperJobVacancy(
            vacancy_name=vacancy["profession"],
            salary_from=vacancy["payment_from"],
            salary_to=vacancy["payment_to"],
            url_vacancy=vacancy["link"],
            town_job=vacancy["town"]["title"],
            description_vacancy=vacancy["work"],
        )
        all_vacancies.append(sj_vacancy)
    return all_vacancies


def create_hh_vacancy(vacancies: list[dict]):
    """Функция для приведения данных с сайта HeadHunter к единому виду."""
    all_vacancies = []
    for vacancy in vacancies:
        sj_vacancy = HeadHunterVacancy(
            vacancy_name=vacancy["name"],
            salary_from=vacancy["salary"]["from"] if vacancy.get("salary") else None,
            salary_to=vacancy["salary"]["to"] if vacancy.get("salary") else None,
            url_vacancy=vacancy["url"],
            town_job=vacancy["area"]["name"],
            description_vacancy=vacancy["snippet"]["requirement"]
        )
        all_vacancies.append(sj_vacancy)
    return all_vacancies


def sort_vacancy_by_salary(vacancies: list[Vacancy]):
    return sorted(vacancies, reverse=True)
