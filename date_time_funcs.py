from datetime import datetime

def get_curr_year_month() -> str:
    '''Returns the current year and month in the format YYYY-MM (e.g. 2026-05)'''
    now = datetime.now()
    year_month = now.strftime("%Y-%m")
    return year_month

def get_today_date() -> str:
    '''Returns the current date as YYYY-MM-DD (e.g. 2026-05-31)'''
    now = datetime.now()
    today_ymd = now.strftime("%Y-%m-%d")
    return today_ymd

def get_curr_time_mins() -> str:
    '''Returns the current time as HH:MM (where HH is 24 hour clock and MM is minutes, e.g. 15:01)'''
    now = datetime.now()
    current_time_mins = now.strftime("%H:%M")
    return current_time_mins

