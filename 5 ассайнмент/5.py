n = int(input())
# читаем переменную
if 10 <= n % 100 <= 20: # чекаем на бочЕК
    print(str(n) + " bochek")

else:
    if n % 10 == 1:  # чекаем на бочкА
        print(str(n) + " bochka")
    elif 1 <= n % 10 <= 4:
        print(str(n) + " bochki") # чекаем на бочКИ
    else:
        print(str(n) + " bochek") # чекаем на бочЕК снова