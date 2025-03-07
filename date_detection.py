import re


def is_valid_date(day, month, year):
    my_date = "-".join([day, month, year])
    if int(day) > 31:
        return f"{my_date} is an invalid date"
    elif month == "04" or month == "06" or month == "11" and int(day) > 30:
        return f"{my_date} is an invalid date"
    elif int(year) % 4 == 0:
        print('Year is a leap year')
        if month == "02" and int(day) > 29:
            return f"{my_date} is an invalid date"
        elif month == "02" and int(day) > 28:
            return f"{my_date} is an invalid date"
    return f"{my_date} is a valid date"


date_matcher = re.compile(r'(\d{2})/(0\d|1[0-2])/((?:1(?:0{3})|1\d{3}|2\d{3}|2(?:9{3})))')
date = date_matcher.search("32/12/1998 is a good year")
day, month, year = date.groups()

is_date_valid = is_valid_date(day, month, year)
print(is_date_valid)
