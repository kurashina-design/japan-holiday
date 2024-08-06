import csv
from os import PathLike

from japanholiday.JapanHoliday import JapanHoliday

holidays = {}


_csv_file = 'syukujitsu.csv'

def load(csv_file: PathLike[str] = None):
    if csv_file:
        _csv_file = csv_file

with open(_csv_file, newline='', encoding='sjis') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        if row[0][0].isnumeric():
            date_source = row[0].split('/')
            year = int(date_source[0])
            month = int(date_source[1])
            day_of_month = int(date_source[2])
            holiday_name = row[1]
            hol = JapanHoliday(year=year, month=month, day_of_month=day_of_month, holiday_name=holiday_name)
            if not holidays.get(year):
                holidays[year] = []
            holidays[year].append(hol)


def main():
    holiday = get_holiday(2024,8,11)
    print(holiday)

def get_holidays(year: int, month: int = None) -> list[JapanHoliday]:
    '''
    :param year: year
    :param month: month
    :return:
    '''
    if not month:
        return holidays.get(year)
    else:
        holiday_months = []
        all_the_year = holidays.get(year)
        if all_the_year:
            for holiday in all_the_year:
                if holiday.month == month:
                    holiday_months.append(holiday)
        return holiday_months


def get_holiday(year: int, month: int, date: int) -> JapanHoliday | None:
    all_the_year = holidays.get(year)
    if all_the_year:
        for holiday in all_the_year:
            if holiday.month == month:
                if holiday.day_of_month == date:
                    return holiday
    return None