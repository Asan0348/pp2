def comp(n):
    i = 1
    while(i * i <= n):
        yield i * i
        i += 1

a = int(input("До какого числа вывести квадраты чисел ? "))
for s in comp(a):
    print(s)
