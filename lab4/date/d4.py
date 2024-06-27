#Напишите программу на Python для вычисления двух разниц дат за секунды.
from datetime import datetime

date1 = datetime(2024, 1, 1, 12, 0, 0)
date2 = datetime(2024, 1, 2, 14, 30, 0)

dif = date2 - date1

dif_sec = dif.total_seconds()

print(f"Первая дата: {date1}")
print(f"Вторая дата: {date2}")
print(f"Разница в секундах: {dif_sec}")
