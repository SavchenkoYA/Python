#1
a = "hello"
b = "students"
print(f"{a}, {b}")
num_1 = int(input("Enter any number: "))
num_2 = int(input("Enter any number one more time: "))
print(f"You have chosen the numbers {num_1} and {num_2}")
word = i  # nput("Enter any word: ")
print(f"{word} - it's good choice")

# 2

time = int(input("Введите время в секундах: "))
hours = time // 3600
minutes = time // 60 - hours * 60
seconds = time % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")

# 3

n = input("Enter an integer: ")

while n < 0
    print("I've asked for number greater than 0! Please try again!")
    n = input('Please enter number greater than 0: ')

print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")

# 4

n = abc(int(input("Введите целое положительное число ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальная цифра в числе ", max)
        break

# 5       
profit = float(input("Введите выручку фирмы: "))
costs = float(input("Введите издержки фирмы: "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f} ")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сотрудника составила {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")

# 6
a = int(input("Введите результаты пробежки первого дня в км  "))
b = int(input("Введите общий желаемый результат в км  "))
result_days = 1
result_km = a
while result_km < b:
    a = a + 0.1 * a
    result_days += 1
    result_km = result_km + a
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)