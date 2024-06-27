import math

def comp(n, s):
    return (n * s ** 2) / (4 * math.tan(math.pi / n))

n = int(input("Введите количество сторон (n): "))
s = float(input("Введите длину стороны (s): "))

area = comp(n, s)

print(f"Площадь правильного многоугольника: {area}")
