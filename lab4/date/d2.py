#Напишите программу на Python для печати вчера, сегодня, завтра.
from datetime import datetime, timedelta


current_date = datetime.now()
next_date = current_date + timedelta(days=1)
bef_date = current_date - timedelta(days=1)

print("Дата вчера: ", bef_date.strftime("%Y.%m.%d"))
print("Текущая дата:", current_date.strftime("%Y.%m.%d"))
print("Дата завтра: ", next_date.strftime("%Y.%m.%d"))
