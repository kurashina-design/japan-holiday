from datetime import date

class Holiday(object):

    __slots__ = ['date', 'year', 'month', 'day_of_month', 'holiday_name']

    def __init__(self, year: int, month: int, day_of_month: int, holiday_name: str):
        self.date = date(year, month, day_of_month)
        self.year = year
        self.month = month
        self.day_of_month = day_of_month
        self.holiday_name = holiday_name

    def __str__(self):
        return f'{self.date} {self.holiday_name}'



