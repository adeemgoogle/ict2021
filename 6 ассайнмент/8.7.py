a = int(input())
b = int(input())
c = int(input())
# cheking max of ages
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)
# cheaking min  of ages
if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)

else:
    print(c)