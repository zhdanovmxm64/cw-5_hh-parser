import requests
import re

from src.employer import Employer


class HHAPI:
    '''
    Класс для работы с API сайта
    https://hh.ru/
    '''

    def __init__(self, employers_id_list: list) -> None:
        self.__api = 'https://api.hh.ru/'
        self.employers_id_list = employers_id_list

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.employers_id_list})'

    def __str__(self) -> str:
        return 'API сайта https://hh.ru/'

    def get_employers(self) -> list:
        '''
        Получает список работадателей, созданных
        на основе класса Employer
        :return: список объектов класса Employer
        '''
        employer_list = []
        for employer_id in self.employers_id_list:
            response = requests.get(url=f'{self.__api}employers/{employer_id}').json()

            try:
                try:
                    pattern = r'<.*?>|&quot;'
                    description = re.sub(pattern, '', response['description'])
                except TypeError:
                    description = response['description']

                employer = Employer(
                    response['name'],
                    response['type'],
                    response['area']['name'],
                    description,
                    response['alternate_url'],
                    response['site_url'],
                    response['vacancies_url'],
                    response['open_vacancies']
                )
            except KeyError:
                raise KeyError(f'Работадателя с id {employer_id} не существует')

            employer_list.append(employer)

        return employer_list
