from datetime import datetime

def get_curr_year_month():
    now = datetime.now()
    year_month = now.strftime("%Y-%m")
    return year_month

def get_today_date():
    now = datetime.now()
    today_ymd = now.strftime("%Y-%m-%d")
    return today_ymd

def get_curr_time_mins():
    now = datetime.now()
    current_time_mins = now.strftime("%H:%M")
    return current_time_mins

def get_date_and_time():
    now = datetime.now()
    today_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return today_time
