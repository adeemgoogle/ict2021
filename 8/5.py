print("Enter number of terms: ", end='')
n = int(input())

n1, n2 = 0, 1
count = 0
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":") # first Fib number
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1, end=' ')
       nth = n1 + n2 # Н-ный Фиб.число
       n1 = n2 # передаем значения чтобы логика Фиб числа сохранялась
       n2 = nth
       count += 1