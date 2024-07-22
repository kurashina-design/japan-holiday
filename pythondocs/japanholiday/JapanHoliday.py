import datetime

class JapanHoliday(object):

    def __init__(self, year: int, month: int, day_of_month: int, holiday_name: str):
        self.__date = datetime.date(year, month, day_of_month)
        self.__year = year
        self.__month = month
        self.__day_of_month = day_of_month
        self.__holiday_name = holiday_name

    @property
    def date(self) -> datetime.date:
        return self.__date

    @property
    def year(self) -> int:
        return self.__year

    @property
    def month(self) -> int:
        return self.__month

    @property
    def day_of_month(self) -> int:
        return self.__day_of_month

    @property
    def holiday_name(self) -> str:
        return self.__holiday_name


    def __str__(self):
        return f'{self.__date} {self.__holiday_name}'



