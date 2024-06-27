#Реализуйте генератор, вызываемый для получения квадрата всех чисел от (a) до (b). Протестируем его с помощью цикла for и выведем каждое из полученных значений
def comp(a, b):
    for i in range(a, b + 1):
        yield i * i

print("введите диапозон : ")
num1 = int(input())
num2 = int(input())

for i in comp(num1, num2):
    print(i)
