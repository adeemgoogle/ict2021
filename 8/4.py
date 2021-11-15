print("Enter starting number: ", end='')
n = int(input())
print("Enter ending number: ", end='')
m = int(input())
print("Prime numbers between", n, "and", m, "are:")
for i in range(n, m + 1):
    ok = True
    for j in range(2, i):
        if i % j == 0: # cheaking prime number if this condit. is work so it is not prime
            ok = False
            break
    if ok:
        print(i)