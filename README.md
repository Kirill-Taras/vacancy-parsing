# Курсовой проект «Поиск вакансий»

## Содержание
- [Описание проекта](#Описание проекта)
- [Требования к реализации](#Требования к реализации)
- [Инструменты для выполнения работы](#Инструменты для выполнения работы)
- [Выходные данные](#Выходные данные)
- [Критерии выполнения курсовой работы](#Критерии выполнения курсовой работы)
- [Автор проекта](#Автор проекта)


## Описание проекта

- Программа, которая получает информацию о вакансиях с разных платформ, 
и сохраняет ее в файл и позволять удобно работать с ней: добавлять, фильтровать, удалять.

### Требования к реализации:

- Создать абстрактный класс для работы с API.
- Реализовать класс, наследующийся от абстрактного класса, для работы с платформами. 
- Определить абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,
получения данных из файла по указанным критериям и удаления информации о вакансиях. 
- Создать класс для сохранения информации о вакансиях в JSON-файл.
- Создать функцию для взаимодействия с пользователем.
- Покрыть описанный функционал тестами. 

### Инструменты для выполнения работы:

- requests
- API
- pytest
- flake8
- dotenv
- pathlib
- ООП

### Выходные данные

- Информация о вакансиях, полученная с разных платформ, сохраненная в JSON-файл.
- Отфильтрованные и отсортированные вакансии, выводимые пользователю через консоль.

### Пример использования

   ```
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
```
### Критерии выполнения курсовой работы

- Проект выложили на GitHub.
- Из файла README понятно, о чём проект и как его использовать.
- В Git есть точечные коммиты.
- Код программы грамотно разбит на функции/классы/модули/пакеты.
- Код читабельный (хороший нейминг, есть docstring, используется typing).
- В работе используются абстрактные классы (минимум один).
- В работе есть переопределение магических методов.
- Для работы с API используется библиотека requests.
- В ходе работы программы создается файл со списком вакансий.
- Пользователь может вывести из файла набор вакансий по определенным критериям.
- Код покрыли тестами (опционально).

## Автор проекта

Тарасов Кирилл Александрович
