#Реализуйте генератор, который возвращает все числа от (n) до 0.
def comp(n):
    for i in range(n, -1, -1):
        yield i

num = int(input("введите число: "))

for i in comp(num):
    print(i)
  
