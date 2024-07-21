import csv
import datetime

from Holiday import Holiday

holiday_years = {}



with open('syukujitsu.csv', newline='', encoding='sjis') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if row[0][0].isnumeric():
            date_source = row[0].split('/')
            year_str = date_source[0]
            year = int(year_str)
            if not holiday_years.get(year_str):
                holiday_years[year_str] = {}

            if len(date_source[1]) == 1:
                monthe_str = '0' + date_source[1]
            else:
                monthe_str = date_source[1]
            month = int(monthe_str)
            if len(date_source[2]) == 1:
                date_str = '0' + date_source[2]
            else:
                date_str = date_source[2]
            date = int(date_str)
            the_date = f'{year_str}-{monthe_str}-{date_str}'
            if not holiday_years.get(year_str):
                holiday_years[year_str] = {}
            if not holiday_years[year_str].get(month):
                holiday_years[year_str][month] = {}
            holiday_years[year_str][month][date] = {
                'date': the_date,
                'holiday_name': row[1]
            }
            hol = Holiday(date=datetime.date(year=year, month=month, day=date), holiday_name=row[1])
            print(hol)

def main():
    get_holidays(2024)

def get_holidays(year: int, month: int = None) -> list[dict]:
    print(holiday_years[str(year)])
    try:
        if month is not None:
            return list(holiday_years[str(year)][month].values())
        else:
            return list(holiday_years[str(year)].values())
    except KeyError:
        return []


def get_holiday(year: int, month: int, date: int) -> dict | None:
    try:
        return holiday_years[str(year)][month][date]
    except KeyError:
        return None


