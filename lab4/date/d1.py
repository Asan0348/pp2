#Напишите программу на Python для вычитания пяти дней из текущей даты.
from datetime import datetime, timedelta


current_date = datetime.now()


new_date = current_date - timedelta(days=5)


print("Текущая дата:", current_date.strftime("%Y.%m.%d"))
print("Дата пять дней назад:", new_date.strftime("%Y.%m.%d"))
