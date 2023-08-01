import psycopg2
import os

from src.config import config
from src.vacancy import Vacancy

class DataBase:
    '''
    Класс базы данных
    '''
    instance = None

    def __new__(cls, *args, **kwargs) -> None:
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, db_name: str) -> None:
        self.__db_name = db_name
        self.__db_data = config()
        self.__create_db()

        self.__connection = psycopg2.connect(dbname=self.__db_name, **self.__db_data)
        self.__create_tables()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.__db_name}')"

    def __str__(self) -> str:
        return f'База данных {self.__db_name}'
