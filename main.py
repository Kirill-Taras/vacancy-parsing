from pprint import pprint

from config import VACANCY_JSON
from src.class_api import HeadHunterAPI, SuperJobAPI
from src.engine import JsonSever

from src.utils import create_sj_vacancy, create_hh_vacancy, sort_vacancy_by_salary


def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    platform_hh = input("Желаете получить данные с 'HeadHunter'? y/n ").lower()
    if platform_hh == "y":
        hh_api = HeadHunterAPI(search_query)
        hh_api_vacancies = hh_api.get_vacancies()
        list_hh_vacancy = create_hh_vacancy(hh_api_vacancies)
    else:
        list_hh_vacancy = []
    platform_sj = input("Желаете получить данные с 'SuperJob'? y/n ").lower()
    if platform_sj == "y":
        sj_api = SuperJobAPI(search_query)
        sj_api_vacancies = sj_api.get_vacancies()
        list_sj_vacancy = create_sj_vacancy(sj_api_vacancies)
    else:
        list_sj_vacancy = []
    sorted_vacancy_by_salary = sort_vacancy_by_salary(list_hh_vacancy + list_sj_vacancy)
    json_sever = JsonSever(VACANCY_JSON)
    json_sever.add_vacancies(sorted_vacancy_by_salary)
    count_vacancy = int(input("Какое количество вакансий желаете получить?: "))
    description_word = input("Введите ключивое слово для поска в описании: ")
    sort_vacancy_by_word = json_sever.get_vacancies(query=description_word)
    user_answer = int(input(f"Вывести полученные данные в консоль "
                            f"или записать результат в файл?: "
                            f"\n0-файл, 1-консоль, 2-файл и консоль "))
    if user_answer == 1:
        pprint(sort_vacancy_by_word[0:count_vacancy])
    if user_answer == 0:
        json_sever.write_file_json(sort_vacancy_by_word[0:count_vacancy])
    if user_answer == 2:
        json_sever.write_file_json(sort_vacancy_by_word[0:count_vacancy])
        pprint(sort_vacancy_by_word[0:count_vacancy])
    else:
        print("Неверный ввод")


if __name__ == '__main__':
    user_interaction()
