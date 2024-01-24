class Vacancy:
    """Kласс для работы с вакансиями."""

    def __init__(
            self,
            vacancy_name: str,
            salary_from: int,
            salary_to: int,
            url_vacancy: str,
            town_job: str,
            description_vacancy: str
    ):
        self.vacancy_name = vacancy_name  # название вакансии
        self.salary_from = salary_from  # миниальная зарплата
        self.salary_to = salary_to  # максимальная зарплата
        self.url_vacancy = url_vacancy  # ссылка на вакансию
        self.town_job = town_job  # город для работы
        self.description_vacancy = description_vacancy  # описание работы

    @staticmethod
    def validate_salary(salary):
        if salary is None:
            return 0
        else:
            return salary


class HeadHunterVacancy(Vacancy):
    pass


class SuperJobVacancy(Vacancy):
    pass





