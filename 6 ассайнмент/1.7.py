size = input("size = ")
add_p = input("add_pepperoni = ")
cheese = input("extra_cheese = ")
cnt = 0 # считает общую сумму

# проверяем все комбаниции
if size == "L" and add_p == "Y" and cheese == "Y":
    cnt = 29
elif size == "L" and add_p == "Y" and cheese == "N":
    cnt = 28
elif size == "L" and add_p == "N" and cheese == "Y":
    cnt = 26
elif size == "L" and add_p == "N" and cheese == "N":
    cnt = 25

if size == "M" and add_p == "Y" and cheese == "Y":
    cnt = 24
elif size == "M" and add_p == "Y" and cheese == "N":
    cnt = 23
elif size == "M" and add_p == "N" and cheese == "Y":
    cnt = 21
elif size == "M" and add_p == "N" and cheese == "N":
    cnt = 20

if size == "S" and add_p == "Y" and cheese == "Y":
    cnt = 18
elif size == "S" and add_p == "Y" and cheese == "N":
    cnt = 17
elif size == "L" and add_p == "N" and cheese == "Y":
    cnt = 16
elif size == "L" and add_p == "N" and cheese == "N":
    cnt = 15

print(cnt)