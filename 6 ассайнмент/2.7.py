year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0): # чекаем на високосный год если год делится на 4/100/400
    print('LEAP YEAR.')
else:
    print('NOT LEAP YEAR.')