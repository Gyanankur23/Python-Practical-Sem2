from datetime import datetime

cur = datetime.now()
formatted_date = cur.strftime("%d-%m-%y")
str1 = '20/02/2025'
date_parse = datetime.strptime(str1, "%d/%m/%Y")
print(date_parse)
print(formatted_date)