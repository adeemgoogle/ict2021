x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
# читаем координаты
# условия ходьбы ладьи если х1 и х2 равны ИЛИ у1 и у2 равны то есть ладья ходит вертикально и горизонтально
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')