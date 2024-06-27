#Напишите программу на Python, которая отбрасывает микросекунды от datetime.
from datetime import datetime

current_datetime = datetime.now()

datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Текущие дата и время:", current_datetime)
print("Дата и время без микросекунд:", datetime_without_microseconds)
