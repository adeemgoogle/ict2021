n = int(input()) * 100
cnt = 0

if n > 1000:
    cnt = n * 0.9 # finding 10% of all sum because n*10/100 == n*0.9
else:
    cnt = n
print(cnt)