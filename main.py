# Список трат за неделю (7 дней)
expenses = [120, 80, 150, 200, 90, 60, 110]

# Вычисления
total = sum(expenses)
average = total / len(expenses)
minimum = min(expenses)
maximum = max(expenses)

# Кортеж (минимум, максимум, сумма)
result = (minimum, maximum, total)

# Вывод
print("Список трат:", expenses)
print("Сумма:", total)
print("Среднее:", average)
print("Минимум:", minimum)
print("Максимум:", maximum)
print("Кортеж:", result)