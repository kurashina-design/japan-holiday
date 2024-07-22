import csv

from japanholiday.Holiday import Holiday

holiday_years = {}

with open('syukujitsu.csv', newline='', encoding='sjis') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    holidays = {}
    for row in spamreader:
        if row[0][0].isnumeric():
            date_source = row[0].split('/')
            year = int(date_source[0])
            month = int(date_source[1])
            day_of_month = int(date_source[2])
            holiday_name = row[1]
            hol = Holiday(year=year, month=month, day_of_month=day_of_month, holiday_name=holiday_name)
            if not holiday_years.get(year):
                holiday_years[year] = []
            holiday_years[year].append(hol)

def main():
    holidays = get_holidays(2024)
    for h in holidays:
        print(h)


def get_holidays(year: int, month: int = None) -> list[Holiday]:
    if not month:
        return holiday_years.get(year)
    else:
        holiday_months = []
        all_the_year = holiday_years.get(year)
        if all_the_year:
            for holiday in all_the_year:
                if holiday.month == month:
                    holiday_months.append(holiday)
        return holiday_months


def get_holiday(year: int, month: int, date: int) -> Holiday | None:
    all_the_year = holiday_years.get(year)
    if all_the_year:
        for holiday in all_the_year:
            if holiday.month == month:
                if holiday.day_of_month == date:
                    return holiday
    return None