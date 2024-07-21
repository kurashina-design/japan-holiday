from datetime import date

class Holiday(object):
    def __init__(self, date: date, holiday_name: str):
        self.date = date
        self.holiday_name = holiday_name
