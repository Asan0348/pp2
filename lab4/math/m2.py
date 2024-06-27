#Напишите программу на Python для вычисления площади трапеции.
def comp(a, b, h):
    return 0.5 * (a + b) * h

a = float(input("Введите длину первого основания (a): "))
b = float(input("Введите длину второго основания (b): "))
h = float(input("Введите высоту (h): "))

area = comp(a, b, h)

print(f"Площадь трапеции: {area}")
