marks = int(input())

if marks < 25:
    print("F")
elif marks < 45 and marks >= 25:
    print("E")
elif marks < 50 and marks >= 45:
    print("D")
elif marks < 60 and marks >= 50:
    print("C")
elif marks < 80 and marks >= 60:
    print("B")
else:
    print("A")