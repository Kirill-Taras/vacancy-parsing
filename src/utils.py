from src.jobs import HeadHunterVacancy, SuperJobVacancy


def create_sj_vacancy(vacancies: list[dict]):
    all_vacancies = []
    for vacancy in vacancies:
        sj_vacancy = SuperJobVacancy(
            vacancy_name=vacancy["profession"],
            salary_from=vacancy["payment_from"],
            salary_to=vacancy["payment_to"],
            url_vacancy=vacancy["link"],
            town_job=vacancy["town"]["title"],
            description_vacancy=vacancy["work"]
        )
        all_vacancies.append(sj_vacancy)
    return all_vacancies


def create_hh_vacancy(vacancies: list[dict]):
    all_vacancies = []
    for vacancy in vacancies:
        sj_vacancy = HeadHunterVacancy(
            vacancy_name=vacancy["name"],
            salary_from=vacancy["salary"]["from"],
            salary_to=vacancy["salary"]["to"],
            url_vacancy=vacancy["url"],
            town_job=vacancy["area"]["name"],
            description_vacancy=vacancy["snippet"]["responsibility"]
        )
        all_vacancies.append(sj_vacancy)
    return all_vacancies
