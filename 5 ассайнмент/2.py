x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
# читаем координаты
# abc это модуль числа. сам слон ходит диагонально.
if abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')