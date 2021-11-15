numbers = map(int, input().split())  # given numbers

for i in numbers: # 3 condition
    if i > 300:
        break
    if i > 120: # 2 condiition
        continue
    if i % 3 == 0: # main 1 condition
        print(i) # our ans for task

