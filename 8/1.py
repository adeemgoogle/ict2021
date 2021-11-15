print('Enter rows number: ', end='') # input
n = int(input()) # вводим кол-во строчек
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print() # чтобы выводилось каждая строчка за строчкой без этого выводится будет в ОДНУ строку