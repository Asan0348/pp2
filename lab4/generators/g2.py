#Напишите программу, использующую генератор для вывода четных чисел от 0 до запятой, где вводится из консоли.nn
def comp(n):
    for i in range(0, n + 1):
        if(i % 2 == 0):
            yield i

num = int(input("до скольки вывести четные исла ? "))

for s in comp(num):
    print(s)
  