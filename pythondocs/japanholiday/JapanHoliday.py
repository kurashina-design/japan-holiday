import datetime

class JapanHoliday(object):

    _weekday_labels = ['月','火','水','木','金','土','日']

    def __init__(self, year: int, month: int, day_of_month: int, holiday_name: str):
        self.__raw = datetime.date(year, month, day_of_month)
        self.__year = year
        self.__month = month
        self.__day_of_month = day_of_month
        self.__holiday_name = holiday_name
        self.__weekday = JapanHoliday._weekday_labels[self.__raw.weekday()]

    @property
    def raw(self) -> datetime.date:
        return self.__raw

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

    @property
    def weekday(self) -> str:
        return self.__weekday

    def __str__(self):
        return f'{self.__raw} {self.__holiday_name}'
