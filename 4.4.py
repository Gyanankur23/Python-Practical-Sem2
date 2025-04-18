from datetime import date
cur_date=date.today()
exp_date=date(2025,9,22)
rem_days=(exp_date-cur_date).days
print(rem_days,"days")