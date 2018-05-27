import time
import datetime


def is_time(value):
    try:
        time.strptime(value, '%H:%M')
        return True
    except ValueError:
        return False


def is_date(date):
    try:
        datetime.datetime.strptime(date, '%d-%m-%Y')
        return True
    except ValueError:
        return False

