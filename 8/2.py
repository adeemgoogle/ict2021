n = int(input("Enter number "))  # вводим число
sum = 0  # перемменной сум присваиваем значение  так как в дальнейшем будем туда записывать сумму чисел
avg = 0  # переменная для среднего значения
for num in range(1, n + 1, 1):  # пробегаемся до всех чисел до n
    sum = sum + num  # записываем сумму
print("Sum of numbers is: ", sum)  # выводим сумму

for i in range(1, n+1):
    avg = sum / n  # находим среднее значение
print("avg:", avg)  # выводим среднее значение