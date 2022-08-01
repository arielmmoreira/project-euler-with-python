"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def main():
    days_in_months = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30, 
                    'july': 31, 'august': 31, 'september': 30, 'october': 31, 'november': 30, 'december': 31}

    months = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 
            7: 'july', 8: 'august', 9: 'september', 10: 'october', 11: 'november', 12: 'december'}


    date = {'day': 1, 'month': 1, 'year': 1901, 'weekday': 2}

    sundays = 0
    while (date['year'] != 2001):
        if is_leap_year(date['year']):
            if date['month'] == 2:
                date['day'] = (date['day'] + 1) % (29 + 1)

            else:
                date['day'] = (date['day'] + 1) % (days_in_months[months[date['month']]] + 1)    
            
        else:
            date['day'] = (date['day'] + 1) % (days_in_months[months[date['month']]] + 1)

        date['weekday'] = (date['weekday'] + 1) % 7

        if date['day'] == 0:
            date['month'] = (date['month'] + 1) % 13
            date['day'] = 1

        if date['month'] == 0:
            date['year'] += 1
            date['month'] = 1

        if date['weekday'] == 0 and date['day'] == 1:
            sundays += 1

    print("Answer:", sundays, "sundays")


def is_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True

        return False

    if year % 4 == 0:
        return True

    return False

main()
