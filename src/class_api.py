from abc import ABC, abstractmethod
import requests


class BasicAPI(ABC):
    """Абстрактный класс для получения API с сайтов."""

    @abstractmethod
    def get_vacancies(self) -> list[dict]:
        pass
