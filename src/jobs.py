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
        """Метод преобразования зарплаты"""
        if salary is None:
            return 0
        else:
            return salary

    def average_salary(self):
        """Вычислнение средней зарплаты"""
        return (self.salary_to + self.salary_from) / 2

    def __gt__(self, other):
        """Метод сравнения зарплаты"""
        return self > other

    def __lt__(self, other):
        """Метод сравнения зарплаты"""
        return self < other

    def __eq__(self, other):
        """Метод сравнения зарплаты"""
        return self == other

    def __str__(self):
        return (f"vacancy_name:{self.vacancy_name}, "
                f"salary_from: {self.salary_from}, "
                f"salary_to: {self.salary_to}, "
                f"url_vacancy: {self.url_vacancy}, "
                f"town_job: {self.town_job}, "
                f"description_vacancy: {self.description_vacancy}")


class HeadHunterVacancy(Vacancy):

    def __str__(self):
        return f"HeadHunter {super().__str__()}"


class SuperJobVacancy(Vacancy):

    def __str__(self):
        return f"SuperJob {super().__str__()}"
