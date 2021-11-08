w = input("weight = ")
h = input("height = ")

get = round(int(w) / (float(h)*float(h)))


if get < 18.5:
    print("Your BMI is " + str(get) + ",you are slightly overweight")
elif 18.5 < get < 25:
    print("Your BMI is " + str(get) + ",you have a normal weight")
elif 25 < get < 30:
    print("Your BMI is " + str(get) + ",you are slightly overweight")
elif 30 < get < 35:
    print("Your BMI is " + str(get) + ",you are obese")
elif get > 35:
    print("Your BMI is " + str(get) + ",you are clinically obese")