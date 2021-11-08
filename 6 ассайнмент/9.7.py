all = int(input())
was = int(input())

get = (was*100)/all # cheaking how many % was student at lesson

# next cheak if attendance more than 75% student can write final
if get > 75:
    print("student can write")
else:
    print("not enought attendance")