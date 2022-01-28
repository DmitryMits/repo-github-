# Задание 1


# a = 4
# print(type(a))
# b = 8
# print(type(b))
# c = 'hello'
# print(type(c))

# Задание 2

# seconds = 54654
# minutes = seconds // 60
# hours = minutes // 60
# print(f'Час: {hours}  минут: {minutes} cекунд: {seconds}')

# Задание 3

# n = int(input("Введите значение n:"))
# p = str(n)
# p1 = p + p
# p2 = p + p + p
# r = n + int(p1) + int(p2)
# print("Получим:", r)

# Задание 4

# n = (int(input("Введите целое положительное число ")))
# max = n % 100
# while n >= 10:
#     n = n // 10
#     if n % 10 > max:
#         max = n % 10
#     if n > 9:
#         continue
#     else:
#         print("Максимальное цифра в числе ", max)
#         break

# Задание 5

# cash = int(input("Введите выручку: "))
# izd = int(input("Введите издержки: "))
# if cash > izd:
#     print(f"У фирмы есть прибыль. Рентабельность составила: {cash / izd}")
# elif cash == izd:
#     print("Фирма работает в ноль:")
# else:
#     print("Фирма работает в убыток")

# Задание 6

# cash = int(input("Введите выручку: "))
# izd = int(input("Введите издержки: "))
# if cash > izd:
#     print(f"У фирмы есть прибыль. Рентабельность составила: {cash / izd}")
#     people = int(input(" Количество работающих сотрудников: "))
#     print(f"Прибль на сотрудника составляет: {cash / people}")
# elif cash == izd:
#     print("Фирма работает в ноль:")
# else:
#     print("Фирма работает в убыток")
#     people = int(input(" Количество работающих сотрудников: "))
#     print(f"Убыток на сотрудника составляет: {cash / people}")

# Задание 7

# a = int(input('Начальный результат:'))
# b = int(input('Планируем достигнуть результата:'))
# days = 1
# result = a
# while result < b:
#          a = a + 0.1 * a
#          days += 1
#          result = result + a
# print(f"Результат достигнут на день:", days)
