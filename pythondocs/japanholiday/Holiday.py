from datetime import date

class Holiday(object):

    __slots__ = ['date', 'year', 'month', 'date', 'holiday_name']

    def __init__(self, date: date, holiday_name: str):
        self.date = date
        self.year = date.year
        self.month = date.month
        self.date = date.day
        self.holiday_name = holiday_name

    def __str__(self):
        return super().__str__()



