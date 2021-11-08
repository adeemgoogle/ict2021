k = int(input())

if k % 5 == 3 or k % 5 == 0 or k % 3 == 0 or k % 3 == 2: # чекаем к шариков на делимость на 3 и 5
    print("YES")
else:
    print("NO")