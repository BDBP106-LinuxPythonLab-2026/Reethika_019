import datetime

def is_magic(day, month, year):
    return day * month == year % 100


print("Magic Dates in the 20th Century")
for year in range(1900, 2000):
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                datetime.date(year, month, day)
            except ValueError:
                continue
            if is_magic(day, month, year):
                print(f"{day:02d}/{month:02d}/{year}")