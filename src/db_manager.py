from src.database import DataBase

class DBManager:
    '''
    Класс для работы с данными базы данных
    '''

    def __init__(self, database: DataBase) -> None:
        self.database = database
        self.__connection = database.connection

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({type(self.database)})'

    def __str__(self) -> str:
        return 'Менеджер для работы с данными БД'