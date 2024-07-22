import csv

from japanholiday.JapanHoliday import JapanHoliday

holidays = {}

with open('syukujitsu.csv', newline='', encoding='sjis') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
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
    _holidays = get_holidays(2024)
    for h in _holidays:
        print(f'year: {h.year}')


def get_holidays(year: int, month: int = None) -> list[JapanHoliday]:
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