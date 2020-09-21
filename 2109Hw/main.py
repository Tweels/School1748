# 1) Определить существование треугольника по трем сторонам
a = float(input("Сторона a="))
b = float(input("Сторона b="))
c = float(input("Сторона c="))

if a + b >= c and a + c >= b and a + c >= b:
    print("Существует")
else:
    print("Не существует")

