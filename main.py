meters = float(input("Введіть кількість метрів: "))
print("1. Конвертувати в милі\n2. Конвертувати в дюйми\n3. Конвертувати в ярди")
num = int(input("Ваш вибір: "))
if num == 1:
   print(meters * 0.000621371192)
elif num == 2:
   print(meters * 39.3700787)
elif num == 3:
   print(meters * 1.0936133)
else:
   print("Невірний вибір")