a = int(input())
b = int(input())
c = int(input())
d = int(input())
# читаем переменные этого уровнения --->(ах+в):(сх+д)=0
if a == 0 and b == 0: # решение бесконечно много
    print("INF")
elif a == 0 or b * c == a * d: #
    print("NO")
elif b % a == 0: # находим х
    x = -b//a
    print(x) # выводим х
else:
    print("NO")
